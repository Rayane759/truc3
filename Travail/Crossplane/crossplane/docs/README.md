# Intégration SUGOI × Crossplane

## Principe

Deux boucles de reconciliation découplées :

1. **Boucle de token** (`auth/03-token-loop.yaml`) — un `DisposableRequest` qui
   tourne en continu, échange `client_id`/`client_secret` contre un `access_token`
   Keycloak, et écrit ce token dans le Secret `sugoi-token`.
2. **Boucle applicative** (`raw/` ou `composition/`) — chaque application est un
   `Request` provider-http qui lit le token dans `sugoi-token` (placeholder résolu
   à chaque appel) et mappe OBSERVE/CREATE/UPDATE/REMOVE sur les endpoints SUGOI.

```
  Secret sugoi-oidc                 Keycloak /token
  (client_id/secret)  ──┐        ┌──────────────────┐
                        ▼        ▼                  │ access_token
                 ┌─────────────────────┐            │
                 │ DisposableRequest    │────────────┘
                 │ sugoi-token (loop)   │
                 └─────────┬────────────┘
                           │ écrit .access_token
                           ▼
                    Secret sugoi-token ──────────┐  {{ sugoi-token:...:access_token }}
                                                 ▼
        Application (claim) ─▶ XApplication ─▶ Request ──▶  API SUGOI
                                                 (Bearer <token>)
```

## Arborescence

| Chemin | Rôle |
|---|---|
| `auth/02-oidc-credentials.example.yaml` | Gabarit du Secret client Keycloak |
| `auth/03-token-loop.yaml` | Boucle d'échange token (le cœur OIDC) |
| `composition/21-xrd.yaml` | API propre `Application` exposée aux équipes |
| `composition/22-composition.yaml` | Rendu `XApplication` → `Request` |

## Déploiement

Prérequis : un cluster avec Crossplane installé, `kubectl` configuré.

```bash
# 1. Provider
kubectl apply -f provider/00-provider.yaml
kubectl wait --for=condition=Healthy provider/provider-http --timeout=180s
kubectl apply -f provider/01-providerconfig.yaml

# 2. Auth OIDC  (édite d'abord le Secret avec tes vraies valeurs)
kubectl apply -f auth/02-oidc-credentials.example.yaml
kubectl apply -f auth/03-token-loop.yaml

# 3a. Approche BRUTE — édite <realm> et le nom d'app, puis :
kubectl apply -f raw/10-application-request.yaml

# 3b. Approche COMPOSITION
kubectl apply -f composition/20-functions.yaml
kubectl wait --for=condition=Healthy function/function-go-templating --timeout=180s
kubectl wait --for=condition=Healthy function/function-auto-ready --timeout=180s
kubectl apply -f composition/21-xrd.yaml
kubectl apply -f composition/22-composition.yaml
kubectl apply -f composition/23-application-claim.example.yaml
```

## Vérifications

```bash
# Le token est-il bien récupéré et injecté dans le Secret ?
kubectl -n crossplane-system get disposablerequest sugoi-token
kubectl -n crossplane-system get secret sugoi-token -o jsonpath='{.data.access_token}' | base64 -d | cut -c1-20

# (Debug) décoder le token pour vérifier realm/rôles/expiration
kubectl -n crossplane-system get secret sugoi-token -o jsonpath='{.data.access_token}' \
  | base64 -d | cut -d. -f2 | base64 -d 2>/dev/null | jq .

# L'Application est-elle synchronisée ?
kubectl get request                      # approche brute
kubectl get application -A               # approche composition (claim)
kubectl describe request <nom>           # voir status.response en cas d'erreur
```

## Points de vigilance

**`nextReconcile` < durée de vie du token.** Le défaut Keycloak « Access Token
Lifespan » est ≈ 5 min ; `auth/03-token-loop.yaml` est réglé à `2m`. Si tu fais
relever le lifespan côté client Keycloak (15–30 min), élargis `nextReconcile`
d'autant — moins d'appels au token endpoint.

**401 transitoires auto-réparés.** Si un token expire pile entre deux refresh, les
Requests prennent un 401 puis se rétablissent au cycle suivant (cohérence
éventuelle). Acceptable pour du control-plane ; garde `nextReconcile` avec marge.

**Bootstrap.** Au tout premier apply, une Application peut partir avant que le
Secret `sugoi-token` existe : elle échoue puis se répare une fois la boucle
token amorcée. Applique `auth/` avant `raw/`/`composition/`.

**⚠️ Le `PUT` SUGOI prend l'`Application` entière.** Le spec ne précise pas si un
UPDATE sans `groups` **préserve** ou **écrase** les groupes de l'app. À TESTER
avant la prod — c'est le premier vrai risque fonctionnel :

Si le PUT écrase les groupes, il faudra soit relire `groups` en OBSERVE et le
réinjecter dans le body d'UPDATE, soit borner strictement la responsabilité des
briques (Application ne touche jamais aux groupes). C'est aussi la frontière
naturelle avec la future brique « Groups ».

**Détection de drift limitée.** provider-http compare la réponse observée au
body désiré ; c'est moins fin qu'un provider typé. Si tu veux un vrai diff champ
par champ et une meilleure UX consommateur, c'est l'argument pour passer plus
tard à un provider natif (client Go généré depuis l'OpenAPI + `x/oauth2/clientcredentials`).

## Sécurité

- Ne committe jamais de vraies valeurs dans `sugoi-oidc` → utilise External
  Secrets Operator / Vault (bloc commenté fourni dans le gabarit).
- Les placeholders `{{ ... }}` gardent client_secret et token hors des specs,
  logs et `status`. Ils vivent uniquement dans les Secrets → durcis le RBAC
  `get/list secrets` sur `crossplane-system`.
- `deletionPolicy: Orphan` sur la boucle token : la supprimer n'entraîne aucun
  appel « delete » distant.

## Notes de version

Manifestes alignés sur provider-http `v1.0.13` (API `http.crossplane.io/v1alpha2`).
Avant prod, pinne les versions exactes (provider + functions) et valide les noms
de champs contre le schéma réel : `kubectl explain request.spec.forProvider`,
`kubectl explain disposablerequest.spec.forProvider`. La méthode HTTP des
`mappings` est déduite de l'`action` (OBSERVE=GET, CREATE=POST, UPDATE=PUT,
REMOVE=DELETE) ; certaines versions permettent de la surcharger via un champ
`method`.
