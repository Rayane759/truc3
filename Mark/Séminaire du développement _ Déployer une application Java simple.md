# Séminaire du développement : Déployer une application Java simple


## Introduction à Kubernetes

[Présentation de Kubernetes](https://presentations-kubernetes-kubeapp-exemples-semina-1717a3cf5bc9b7.gitlab-pages.insee.fr/seminaire-dev-2026/README.html#1)


## Objectif du jour
Le but de l'atelier du jour est d'arriver à déployer et mettre à disposition une application sur le cluster interne Insee KubeDev.\
\
Pour y parvenir, vous avez à votre disposition:

* une image

* un namespace individuel

* un mode d'emploi vraiment super

Nous observerons ensuite d'autres syntaxes de déploiement plus adaptées à une mise en production durable (Helm et dépendance)

## L'application à déployer

Le dépôt de code de l'application à déployer se trouve [ici](https://gitlab.insee.fr/kubernetes/kubeapp/exemples/seminaire-dev/2026/creation-image).

S'il fallait déployer cette application sur une vm, on lancerait le build de l'application via un pipeline CICD sur gitlab. Ensuite on fournirait le paquet sous forme de jar ou de war à Majiba pour que l'application soit déployée.

Dans le monde kubernetes on ne travaille pas avec une archive mais avec une image qui permettra d'instancier notre application sur kubernetes.

L'image est décrite via un fichier nommé [Dockerfile](https://gitlab.insee.fr/kubernetes/kubeapp/exemples/seminaire-dev/2026/creation-image/-/blob/main/Dockerfile?ref_type=heads).

Ensuite dans le fichier [.gitlab-ci.yml](https://gitlab.insee.fr/kubernetes/kubeapp/exemples/seminaire-dev/2026/creation-image/-/blob/main/.gitlab-ci.yml?ref_type=heads) on va retrouver les étapes habituelles de build d'application Java avec en plus des étapes de build docker afin de créer l'image.

Enfin une fois le pipeline terminé, l'image est accessible via le [container registry](https://gitlab.insee.fr/kubernetes/kubeapp/exemples/seminaire-dev/2026/creation-image/container_registry/2794).

## C'est parti!

> **Convention** : partout où vous lisez `<mon-idep>`, remplacez par votre identifiant Insee

### Préparation de la structure de déploiement

Les namespaces individuels ont été configurés de manière à déployer les applications définies dans `https://gitlab.insee.fr/<mon-idep>/gitops-template/argocd-apps/kubedev`

Commencez par faire un fork [du projet exemple de structure de déploiement](https://gitlab.insee.fr/kubernetes/kubeapp/exemples/seminaire-dev/2026/gitops-template) dans votre espace gitlab personnel. Pensez à retirer la dépendance de votre fork au projet initial.

> 💡Le mode de déploiement utilisé ici est appelé **app-of-apps**.\
\
Le principe est d’avoir un dépôt principal qui référence les applications à déployer sur votre namespace. Chaque application possède ensuite sa propre configuration de déploiement.\
\
Ce fonctionnement permet de centraliser la liste des applications déployées tout en laissant chaque application évoluer indépendamment.\
\
À l’Insee, la configuration de base des namespaces est gérée par l’équipe KubeApp. Le modèle *app-of-apps* permet ensuite aux équipes utilisant ces namespaces de gérer elles-mêmes les applications qu’elles souhaitent y déployer, sans modifier directement la configuration du namespace.


### Comprendre la structure du dépôt

Ce projet gitops-template présente la structure suivante:

```
.
├── apps
│   ├── app-simple
│   ├── chart-dependance
│   └── chart-simple
└── argocd-apps
    └── kubedev
        ├── app-simple.yaml
        ├── chart-dependance.yaml
        └── chart-simple.yaml
```

Les namespace étant configurés pour déployer les applications définies dans `./argocd-apps/kubedev`, nous allons déployer ici ce qui est décrit dans les 3 fichiers `yaml`.\
\
Il faut donc modifier ces fichiers pour les adapter à votre dépôt :

```yaml=
# app-simple.yaml\
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: app-simple
  namespace: projet-<mon-idep> # A Modifier
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  destination:
    namespace: projet-<mon-idep> # A Modifier
    name: in-cluster
  project: projet-<mon-idep> # A Modifier
  source:
    path: apps/app-simple
    repoURL: https://gitlab.insee.fr/<mon-idep>/gitops-template.git # A Modifier
    targetRevision: main
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

Ces fichiers décrivent chacun une application qui sera à son tour déployée.

###  ArgoCD : Voir mes déploiements

L'outil qui va permettre de mettre en relation Gitlab et le cluster Kubernetes s'appelle ArgoCD. Il en existe plusieurs instances à l'Insee. Celle que nous allons utiliser aujourd'hui est celle dédiée aux applications utilisateurs du cluster de développement Kubedev.

Son url : [https://gitops-kubernetes.developpement.insee.fr](https://gitops-kubernetes.developpement.insee.fr)

Vous devriez pouvoir observer les trois applications `app-simple`, `chart-simple` et `chart-dependance`. Les dossiers liés à ces applications étant vides, les applications résultantes dans ArgoCD le sont naturellement aussi.




###  Mon premier déploiement kube 

C'est l'application **la plus basique** : trois fichiers YAML qu'ArgoCD appliquera tels quels.

Copiez ces trois fichiers dans `apps/app-simple/` :

#### `apps/app-simple/deployment.yaml`

```yaml=
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-simple
spec:
  replicas: 1
  selector:
    matchLabels:
      app: app-simple
  template:
    metadata:
      labels:
        app: app-simple
    spec:
      containers:
        - name: app-simple
          image: # A compléter
          ports:
            - name: http
              containerPort: 8080
```

#### `apps/app-simple/service.yaml`

```yaml=
apiVersion: v1
kind: Service
metadata:
  name: app-simple
spec:
  type: ClusterIP
  selector:
    app: app-simple
  ports:
    - name: http
      port: 8080
      targetPort: http
```

#### `apps/app-simple/ingress.yaml`

```yaml=
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-simple
  annotations:
    cert-manager.io/cluster-issuer: developpement-insee-fr
spec:
  ingressClassName: nginx
  rules:
    - host: <mon-url> # A compléter
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: app-simple
                port:
                  number: 8080
  tls:
    - hosts:
        - <mon-url> # A compléter
      secretName: app-simple
```


Une fois qu'argocd aura vu le nouveau commit, vous pouvez retrouver les nouveaux objets Kube définis dans l'application `app-simple` sur [ArgoCD](https://gitops-kubernetes.developpement.insee.fr).

#### Améliorations

La configuration de ce déploiement est en revanche ici très simpliste. Dans beaucoup de cas, il faudra ajouter d'autres choses, comme des informations sur les ressources disponibles, sur les variables d'environnement à intégrer aux pods, ou encore sur les règles de sécurité à observer.


Essayons d'ajouter cela en complétant le bloc `spec.template.spec.containers` du fichier `apps/app-simple/deployment.yaml`.

Dans le conteneur `app-simple`, ajoutez d'abord une variable d'environnement :

```yaml=
env:
  - name: MON_ENV
    value: "Bonjour"
```

Ajoutez ensuite un securityContext :

```yaml=
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
```


Enfin, ajoutez des ressources faibles pour limiter la consommation du conteneur :

```yaml=
resources:
  requests:
    cpu: "50m"
    memory: "64Mi"
  limits:
    cpu: "100m"
    memory: "128Mi"
```

Après avoir fait le commit des modifications, on peut vérifier sur ArgoCD la bonne prise en compte de la configuration.

###  Factoriser la configuration avec Helm 

On va décrire **la même application** que `app-simple`, mais cette fois sous forme de **chart Helm** : les manifests deviennent des *templates*, et les valeurs paramétrables sont sorties dans un `values.yaml`.
L'idée de Helm est de pouvoir factoriser le code pour pouvoir le réutiliser dans differents environnement en limitant la réécriture au values.yaml

Créez l'arborescence suivante dans votre fork :

```
apps/chart-simple/
├── Chart.yaml
├── values.yaml
└── templates/
    ├── deploy.yaml
    ├── service.yaml
    └── ingress.yaml
```

Puis copiez le contenu de chaque fichier ci‑dessous.

#### `apps/chart-simple/Chart.yaml`

Métadonnées du chart : son nom, sa version, son type.

```yaml=
apiVersion: v2
name: chart-simple
type: application
version: 0.0.1
appVersion: "0.1.0"
```

#### `apps/chart-simple/values.yaml`

**Le fichier central** : toutes les valeurs qu'on veut pouvoir changer sans toucher aux templates.

```yaml=
replicaCount: 1

image:
  repository: gitlab-registry.insee.fr/kubernetes/kubeapp/exemples/seminaire-dev/2026/creation-image
  tag: main

service:
  type: ClusterIP
  port: 8080

ingress:
  className: nginx
  clusterIssuer: developpement-insee-fr
  host: chart-simple-<mon-idep>.developpement.insee.fr
```

#### `apps/chart-simple/templates/deploy.yaml`

Comparez avec le `deployment.yaml` brut du premier déploiement: la structure est identique, mais toutes les valeurs en dur ont été remplacées par des expressions Go template `{{ .Values.xxx }}`.

```yaml=
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
spec:
  replicas: {{ .Values.replicaCount }}

  selector:
    matchLabels:
      app: {{ .Chart.Name }}

  template:
    metadata:
      labels:
        app: {{ .Chart.Name }}

    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"

          ports:
            - name: http
              containerPort: {{ .Values.service.port }}
```

>   **Trois sources de variables** dans Helm :
> - `.Values.xxx` → vient de votre `values.yaml`
> - `.Chart.xxx` → vient de `Chart.yaml` (nom, version…)
> - `.Release.xxx` → injecté à l'installation (nom de la release, namespace cible…)

#### `apps/chart-simple/templates/service.yaml`

```yaml=
apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}

spec:
  type: {{ .Values.service.type }}

  selector:
    app: {{ .Chart.Name }}

  ports:
    - name: http
      port: {{ .Values.service.port }}
      targetPort: http
```

#### `apps/chart-simple/templates/ingress.yaml`

```yaml=
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}

  annotations:
    cert-manager.io/cluster-issuer: {{ .Values.ingress.clusterIssuer }}

spec:
  ingressClassName: {{ .Values.ingress.className }}

  rules:
    - host: {{ .Values.ingress.host }}

      http:
        paths:
          - path: /
            pathType: Prefix

            backend:
              service:
                name: {{ .Release.Name }}

                port:
                  number: {{ .Values.service.port }}

  tls:
    - hosts:
        - {{ .Values.ingress.host }}

      secretName: {{ .Release.Name }}
```

**Comparez avec `app-simple`** : c'est *fonctionnellement* la même chose, mais ici :

- les valeurs spécifiques (`replicaCount`, `image.tag`, `ingress.host`…) sont **extraites** dans `values.yaml` ;
- les templates utilisent la syntaxe Go (`{{ .Values.replicaCount }}`) pour réinjecter ces valeurs ;
- on peut **réutiliser** le même chart sur plusieurs environnements en ne changeant que `values.yaml`.

C'est l'apport principal de Helm : **séparer la structure des manifests** (templates, stables) **de leurs paramètres** (values, variables).


Une fois qu'argocd aura vu le nouveau commit, vous pouvez retrouver votre application ici:
https://gitops-kubernetes.developpement.insee.fr/applications/projet-<mon-idep>/chart-simple


### L'utilisation du chart KubeAPP pour déployer une application 

Dernier niveau : on ne réécrit plus du tout les templates, on **consomme un chart déjà packagé** (`helm-example`) et on se contente de surcharger ses valeurs.

Créez l'arborescence suivante — **seulement deux fichiers, pas de dossier `templates/`** :

```
apps/chart-dependance/
├── Chart.yaml
└── values.yaml
```

#### `apps/chart-dependance/Chart.yaml`

La nouveauté est le bloc `dependencies:` qui pointe vers un chart publié sur un registre Helm.

```yaml=
apiVersion: v2
name: chart-dependance
type: application
version: 0.0.1
appVersion: "0.1.0"
dependencies:
  - name: helm-example
    repository: https://gitlab.insee.fr/api/v4/projects/10954/packages/helm/stable
    version: 3.0.2
    alias: chart-dependance
```

>  L'`alias: chart-dependance` permet d'adresser les valeurs du chart dépendant sous la clé `chart-dependance:` dans `values.yaml` (au lieu de `helm-example:`). C'est purement un confort de nommage.

#### `apps/chart-dependance/values.yaml`

On **surcharge** uniquement les valeurs qui nous intéressent ; tout ce qu'on n'écrit pas garde la valeur par défaut du chart `helm-example`.

```yaml=
chart-dependance: 
  image: 
    repository: gitlab-registry.insee.fr/kubernetes/kubeapp/exemples/seminaire-dev/2026/creation-image
    tag: main
  ingress:
    url: chart-dependance-<mon-idep>.developpement.insee.fr
  replicaCount: 1
  securityContext:
    readOnlyRootFilesystem: false
  resources: 
    limits:
      cpu: 500m
      ephemeral-storage: 100Mi
      memory: 256Mi
    requests:
      cpu: 100m
      ephemeral-storage: 1Mi
      memory: 128Mi
```



Une fois qu’ArgoCD aura détecté le nouveau commit, l’application sera automatiquement visible dans ArgoCD.

L’idée avec Helm, c’est de pousser au maximum la réutilisation de charts standardisés plutôt que de réécrire les manifests à chaque projet. Si l’équipe kubeapp fait évoluer le chart helm-example (ajout de NetworkPolicies, renforcement de la sécurité, etc.), il suffit simplement de mettre à jour la version dans le Chart.yaml pour profiter des améliorations.
