# Brique « Groups » — gestion des groupes d'une application SUGOI

Pilote le cycle de vie des **groupes d'une application** (create / update / delete),
en réutilisant l'auth OIDC et l'infra déjà en place pour la brique Application.

## Ce qui est réutilisé (rien à redéployer)

- `provider/` — provider-http + ProviderConfig `http-none`
- `auth/` — la boucle de token `sugoi-token`
- `composition/20-functions.yaml` — les mêmes functions go-templating / auto-ready

## Fichiers de cette brique

| Chemin | Rôle |
|---|---|
| `raw/30-group-request.yaml` | Un groupe en direct (approche brute, à dupliquer) |
| `composition/40-xrd-group.yaml` | API propre `Group` exposée aux équipes |
| `composition/41-composition-group.yaml` | Rendu `XGroup` → `Request` |
| `composition/42-group-claim.example.yaml` | Exemple côté consommateur |

## Modèle

Identité externe d'un groupe : **`(realm, application, groupName)`**.
Champs gérés (schéma `GroupView` du spec SUGOI) : `name`, `description`, `appName`,
`isSelfManaged`. `appName` est renseigné automatiquement depuis `application`.

Endpoints mappés :

```
OBSERVE : GET    /v2/realms/{realm}/applications/{app}/groups/{name}   200/404
CREATE  : POST   /v2/realms/{realm}/applications/{app}/groups          201/409
UPDATE  : PUT    /v2/realms/{realm}/applications/{app}/groups/{name}
REMOVE  : DELETE /v2/realms/{realm}/applications/{app}/groups/{name}
```

## Déploiement

```bash
# Approche BRUTE (édite <realm>/<application>/nom, puis) :
kubectl apply -f groups/raw/30-group-request.yaml

# Approche COMPOSITION (functions déjà installées via composition/20-functions.yaml)
kubectl apply -f groups/composition/40-xrd-group.yaml
kubectl apply -f groups/composition/41-composition-group.yaml
kubectl apply -f groups/composition/42-group-claim.example.yaml

# Vérif
kubectl get group -A
kubectl describe request <nom>
```

## Points de vigilance propres aux groupes

**Dépendance à l'application (auto-cicatrisante).** Un groupe suppose que son
application existe. Si tu appliques le groupe avant l'app, le CREATE échoue
(404) puis se répare au cycle suivant une fois l'app présente. Ce n'est donc
pas bloquant, mais pour un ordre déterministe tu peux exprimer la dépendance
au niveau composition (ex. `Usage` Crossplane) ou orchestrer via une
composition parente Application-qui-embarque-ses-Groups.

**Unicité cross-namespace — même problème, même parade.** Comme pour les
applications, `(realm, application, groupName)` est plat côté SUGOI. Deux
namespaces qui déclarent le même triplet piloteront le même groupe distant
(split-brain, provider-http adoptant tout objet existant en OBSERVE). Applique
la même règle : **prévention à l'admission** (ValidatingAdmissionPolicy /
Kyverno) — préfixe de `groupName` par équipe, ou realm/app réservé à un
namespace. Le 409 SUGOI reste un backstop, pas une garantie d'ownership.

**Frontière avec la brique Application.** C'est volontaire : l'Application ne
gère jamais `groups`, la brique Group les gère intégralement. Ça évite que le
`PUT` complet de l'Application écrase les groupes (le risque qu'on avait
identifié). Garde cette séparation stricte.

## Non couvert ici : l'appartenance des utilisateurs (membership)

Le spec expose aussi l'ajout/retrait d'utilisateurs dans un groupe :

```
PUT/DELETE /v2/realms/{realm}/applications/{app}/groups/{group}/members/{user}
GET/PUT/DELETE .../group_manager/members/{user}    (groupe des gestionnaires)
```

Je ne l'ai **pas** livré comme `Request`, pour une raison de correction, pas
d'oubli : provider-http détermine l'existence d'une ressource via le **code HTTP
de l'OBSERVE (GET)**, or il n'existe pas de GET « l'utilisateur U est-il dans le
groupe G ». Le seul moyen serait de faire GET sur le groupe et de tester
`.users[] | select(.username == U)`, c.-à-d. une existence basée sur le **corps**
de la réponse, pas sur le statut. Selon la version de provider-http, ce test
sur le corps en OBSERVE n'est pas garanti — et sans lui, la ressource serait
soit jamais créée (le GET groupe renvoie 200 → provider-http croit le membership
déjà présent et ne PUT jamais), soit jamais réparée en cas de retrait externe.

Deux façons propres de traiter le membership, à choisir selon ton besoin :

1. **Confirmer** que ta version de provider-http sait conditionner l'existence
   OBSERVE à un prédicat jq sur le corps, puis modéliser le membership en
   `Request` (CREATE=PUT member, REMOVE=DELETE member, OBSERVE=GET groupe +
   prédicat sur `.users`).
2. **Le porter dans le provider natif** (le moment venu) : un controller Go lit
   `.users[]`, décide de l'ajout/retrait, et encode une vraie sémantique
   d'appartenance — bien plus net que de contourner le modèle de provider-http.

Dis-moi si tu veux que je développe le membership selon l'option 1 (je vérifierai
d'abord le comportement exact de l'OBSERVE sur ta version), ou qu'on le garde
pour la bascule native.
