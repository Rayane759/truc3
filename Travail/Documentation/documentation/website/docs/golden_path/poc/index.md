# Golden Path V0 — Guide documenté

## Principe général

La V0 de notre Golden Path prend la forme d'un guide documenté. Le développeur fait tout manuellement, mais il sait exactement quoi faire, dans quel ordre, et dispose des ressources au bon moment en cas de besoin.

-----------------------------------------------------

## Phase 0 — Initialisation

### Ce que fait le développeur

Il lance le Golden Path et répond à quelques questions :

`Nom du projet          : my-service`  
`Votre projet inclut-il un backend Java ?    [Oui/Non]`  
`Votre projet inclut-il un frontend React ?  [Oui/Non]`  
`Votre projet inclut-il une base Postgres ?  [Oui/Non]`  

### Ce que fait le Golden Path

Il adapte le guide en fonction des réponses. Par exemple, un projet sans frontend n'affichera pas les étapes liées à React.

### Ce qu'obtient le développeur

Un guide personnalisé et structuré avec uniquement ce dont il a besoin pour son projet.

-----------------------------------------------------

## Phase 1 — Initialisation du dépôt

### Étape 1.1 — Créer le dépôt GitLab

Action : Créer manuellement un nouveau dépôt GitLab dans le namespace de votre équipe.

- Documentation de nommage des dépôts : `LIEN_CONVENTIONS_NOMMAGE`
- Documentation GitLab pour créer un dépôt : `https://git-scm.com/book/fr/v2/Git-sur-le-serveur-GitLab` (Optionnel, juste on appuie sur un bouton sur Gitlab)

### Étape 1.2 — Appliquer la structure de dépôt standard

Action : Créer l'arborescence de dossiers suivante à la racine du dépôt :

`my-service/`  
├── `backend/`              ← Code source Java  
├── `frontend/`             ← Code source React (si besoin)  
├── `helm/`                 ← Charts Helm pour le déploiement  
├── `docs/`                 ← Documentation du projet  
├── `.gitlab-ci.yml`        ← Pipeline CI (créé à l'étape 4)  
├── `.editorconfig`         ← Configuration de l'éditeur  
├── `.gitignore`            ← Fichiers à ignorer  
├── `README.md`             ← Documentation  
└── `RUNBOOK.md`            ← Guide de démarrage  

- Exemple de `.editorconfig`Z : `https://github.com/spring-projects/spring-boot/blob/main/.editorconfig` (Voir si on peut compléter)
- Exemple de `.gitignore` : `https://github.com/github/gitignore/blob/main/Java.gitignore`

### Étape 1.3 — Configurer les conventions de commit

Action : Ajouter un fichier `.gitmessage` à la racine du dépôt et le configurer localement.

- Convention de commit adoptée par l'équipe : `LIEN_CONVENTIONS_COMMIT`
- Exemple de `.gitmessage` : `https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733#template-file`

*Commande à exécuter une fois après le clone :*  
`git config --global commit.template ~/.gitmessage`

-----------------------------------------------------

## Phase 2 — Initialisation du backend Java

### Étape 2.1 — Générer le squelette Spring Boot

Action : Générer le projet Java via Spring Initializr et placer le contenu dans le dossier `backend/`.

Aller sur `https://start.spring.io` et configurer avec les paramètres suivants :

- Project     : Maven
- Language    : Java
- SpringBoot  : `https://spring.io/projects/spring-boot` (Rectangle vert à côté du titre. Sinon, on peut juste mettre à jour cette section régulièrement)
- Packaging   : Jar
- Java        : 21
- Dépendances : Spring Web, Actuator, Validation, Spring Cloud Vault

Pourquoi ces dépendances ? `LIEN_DOC_CHOIX_DEPENDANCES`

### Étape 2.2 — Configurer la connexion Postgres

Action : Configurer la datasource dans `backend/src/main/resources/application.yml`.

S'inspirer du fichier de configuration standard ci-dessous, en remplaçant les valeurs `<valeur>` :

- Exemple de configuration `application.yml` avec Postgres : `https://docs.spring.io/spring-boot/reference/data/sql.html` (Un fichier exemple serait probablement mieux)

Pas de mot de passe à cette étape. Les credentials sont gérés avec Vault (voir Phase 5).

### Étape 2.3 — Configurer les health checks

Action : Vérifier que Spring Boot Actuator est bien configuré pour exposer les healths checks.

Ajouter dans `application.yml` :

- Exemple de configuration Actuator pour Kube : `EXEMPLE_ACTUATOR_CONFIG` (D'après la doc, ça auto-détecte ... L'information vient de là : `https://docs.spring.io/spring-boot/docs/2.3.0.RELEASE/reference/html/deployment.html#cloud-deployment-kubernetes`)
- Documentation de l'équipe Kubernetes sur les health checks : `https://kubernetes.gitlab-pages.insee.fr/kubeapp/documentation/guide_utilisateurs/service_supervision_observabilite/` (Il faut peut-être préciser ... A voir)

### Étape 2.4 — Configurer les logs structurés (à préciser)

Action : Configurer logs.

- Exemple de `logsXXX` : `EXEMPLE_LOGxxx`
- Documentation de l'équipe Observabilité sur les logs : `https://kubernetes.gitlab-pages.insee.fr/kubeapp/documentation/guide_utilisateurs/service_supervision_observabilite/` (Il faut peut-être préciser ... A voir)

-----------------------------------------------------

## Phase 3 — Initialisation du frontend React

Cette phase s'affiche uniquement si le projet inclut un frontend React.

### Étape 3.1 — Générer le squelette React

Action : Générer le projet React et placer le contenu dans le dossier `frontend/`.

`npm create vite@latest frontend -- --template react`

Convention de structure des projets React : `LIEN_CONVENTIONS_REACT` (Il faudrait renvoyer vers un fichier direct)

### Étape 3.2 — Configurer le Dockerfile frontend

Action : Créer un fichier `frontend/Dockerfile` en s'inspirant du modèle standard.

Exemple de Dockerfile React multi-stage (build + nginx) : `https://www.docker.com/blog/how-to-dockerize-react-app/`

Le Dockerfile utilise un build multi-stage : la première étape compile le React, la seconde sert les fichiers statiques via nginx. Cela réduit significativement la taille de l'image finale. (`https://www.docker.com/blog/how-to-dockerize-react-app/`)

-----------------------------------------------------

## Phase 4 — Containerisation

### Étape 4.1 — Créer le Dockerfile backend

Action : Créer un fichier `backend/Dockerfile` en s'inspirant du modèle standard.

Exemple de Dockerfile Java multi-stage : `https://docs.docker.com/get-started/docker-concepts/building-images/multi-stage-builds/` (Le site est bien, mais en vrai un fichier pourrait être mieux)

Image validée par l'équipe platform : `LIEN_IMAGES_BASE_VALIDEES`

### Étape 4.2 — Vérifier le build local

Action : Vérifier que l'image se construit correctement en local avant de pousser.

`# Backend :`  
`docker build -t my-service-backend ./backend`

`# Frontend (si besoin) :`  
`docker build -t my-service-frontend ./frontend`

### Étape 4.3 — Identifier le registry cible

Action : S'assurer que vous avez accès au registry GitLab de votre namespace.

- Documentation du registry GitLab de la plateforme : `https://docs.gitlab.com/user/packages/container_registry/` (Doc de GitLab, elle est bien en vraie mais ça peut changer)
- Demande d'accès si nécessaire : `LIEN_DEMANDE_ACCES_REGISTRY`

Le push vers le registry sera automatisé par le pipeline CI à l'étape suivante. Pas besoin de le faire manuellement.

-----------------------------------------------------

## Phase 5 — Pipeline CI

### Étape 5.1 — Créer le fichier `.gitlab-ci.yml`

Action : Créer le fichier `.gitlab-ci.yml` à la racine du dépôt en incluant les templates CI centralisés.

S'inspirer du fichier `.gitlab-ci.yml` standard pour un projet Java (+ React si besoin) :

- Exemple `.gitlab-ci.yml` backend Java : 
  - `https://gitlab.com/gitlab-org/project-templates/spring/-/blob/main/.gitlab-ci.yml?ref_type=heads` (Bon fichier de départ)
  - `https://gitlab.com/gitlab-examples/maven/simple-maven-example` (Pour Maven. Pas mal)
  - `https://docs.gitlab.com/ci/examples/` (Renvoie vers beaucoup d'exemples, dont celui juste au-dessus)
- Exemple `.gitlab-ci.yml` backend Java + frontend React : `EXEMPLE_GITLAB_CI_JAVA_REACT`

Lire la documentation pour comprendre ce qui est personnalisable.

Documentation des templates CI centralisés : `LIEN_DOC_CI_TEMPLATES`

### Étape 5.2 — Vérifier le premier pipeline

Action : Pousser le `.gitlab-ci.yml` sur GitLab et vérifier que le pipeline se déclenche et passe.

Si le pipeline échoue, consulter le guide de dépannage CI : `https://docs.gitlab.com/ci/debugging/`

-----------------------------------------------------

## Phase 6 — Secrets et sécurité

### Étape 6.1 — Déclarer les secrets dans Vault

Action : Créer le chemin Vault dédié à votre service et y déposer les secrets nécessaires (credentials Postgres, etc.).

- Documentation de l'équipe Vault pour créer un secret :
  - `https://gitlab.insee.fr/iahs/secrets/documentation/doc-publique` (Il faudrait probablement préciser)
  - `https://gitlab.insee.fr/iahs/secrets/documentation/doc-publique/-/wikis/home` (Il y a plus de trucs on dirait)
- Convention de nommage des chemins Vault :
  - `https://gitlab.insee.fr/iahs/secrets/documentation/doc-publique` (Il faudrait probablement préciser)
  - `https://gitlab.insee.fr/iahs/secrets/documentation/doc-publique/-/wikis/home` (Il y a plus de trucs on dirait)

`Convention de chemin :`  
`secret/data/<equipe>/<service>/<environnement>/<cle>`

`Exemple :`  
`secret/data/backend/my-service/dev/database-password`

### Étape 6.2 — Configurer l'accès Vault dans le projet

Action : Configurer Spring Cloud Vault dans `application.yml` pour qu'il récupère les secrets au démarrage.

- Exemple de configuration Spring Cloud Vault : `https://cloud.spring.io/spring-cloud-vault/reference/html/` (On peut sûrement améliorer cette source)
- Documentation technique complète : `https://spring.io/projects/spring-vault`

### Étape 6.3 — Activer GitLeaks dans le pipeline

Action : Vérifier que le template CI inclus à l'étape 5 active bien GitLeaks. Si ce n'est pas le cas, l'ajouter manuellement.

Documentation GitLeaks sur la plateforme : `https://blog.stephane-robert.info/docs/securiser/analyser-code/gitleaks/#gitlab-ci` (En vrai c'est bien, il faut tester) (Sinon, un fichier suffit / bout de code suffit)

-----------------------------------------------------

## Phase 6 2.0 (Plus détaillé)

### Étape 6.1 : Déclarer les secrets dans Vault

#### 6.1.1 : Vérifier l'accès à Vault

##### Action

Vérifier qu'on est connecté à Vault.

`vault login`

Documentation : `https://gitlab.insee.fr/iahs/secrets/documentation/doc-publique/-/wikis/home`

#### 6.1.2 : Identifier le bon chemin Vault

`Convention :`
`secret/data/<equipe>/<service>/<environnement>/<cle>`

`Exemple :`
`secret/data/backend/monservice/dev/database`

Documentation : `https://gitlab.insee.fr/iahs/secrets/documentation/doc-publique/-/wikis/home`

#### 6.1.3 : Créer les secrets

``` bash
vault kv put secret/backend/my-service/dev/database \
  username="pseudo" \
  password="mdp" \
  url="jdbc:postgresql://postgres:5432/mydb"
```

#### 6.1.4 : Vérifier le secret

Action : Vérifier que les clés et valeurs sont présentes et correctes.

`vault kv get secret/backend/my-service/dev/database`

#### 6.1.5 : Gérer les droits d'accès

`hcl`
`path "secret/data/backend/my-service/dev/*" {
  capabilities = ["read"]
}`

Puis :

`bash`
`vault policy write my-service-policy policy.hcl`

### Étape 6.2 : Configurer l'accès Vault dans Spring Boot

#### 6.2.1 : Ajouter la dépendance

Dans le fichier `pom.xml`, ajouter (si ce n'est pas déjà présent) :

``` xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-vault-config</artifactId>
</dependency>
```

#### 6.2.2 : Configurer application.yml

Ajouter dans le fichier `application.yml` :

``` yaml
spring:
  cloud:
    vault:
      uri: http://vault:8200
      authentication: KUBERNETES
      kv:
        enabled: true
        backend: secret
        default-context: backend/my-service
```

#### 6.2.3 : Mapper les secrets

``` yaml
spring:
  datasource:
    username: ${username}
    password: ${password}
```

### 6.3 : GitLeaks

``` yaml
gitleaks:
  image: zricethezav/gitleaks
  script:
    - gitleaks detect --source . --verbose
```

-----------------------------------------------------

## Phase 7 — Déploiement Kubernetes

### Étape 7.1 — Créer le chart Helm

Action : Créer la structure Helm dans le dossier `helm/` en s'inspirant du chart standard.

- Exemple de chart Helm standard pour une API Java :
  - Il faudrait mettre un fichier
  - `https://kubernetes.gitlab-pages.insee.fr/kubeapp/documentation/guide_utilisateurs/helm/premier_pas_helm/`
  - `https://kubernetes.gitlab-pages.insee.fr/kubeapp/documentation/guide_utilisateurs/helm/chart_generique/`
  - `https://helm.sh/docs/chart_template_guide/getting_started/`
- Exemple de chart Helm pour un projet Java + React + Postgres :
  - Il faudrait mettre un fichier
  - `https://kubernetes.gitlab-pages.insee.fr/kubeapp/documentation/guide_utilisateurs/helm/premier_pas_helm/`
  - `https://kubernetes.gitlab-pages.insee.fr/kubeapp/documentation/guide_utilisateurs/helm/chart_generique/`
  - `https://helm.sh/docs/topics/charts/`

Structure attendue :

helm/  
├── Chart.yaml  
├── values.yaml           ← Par défaut  
├── values-dev.yaml       ← Surcharges dev  
├── values-prod.yaml      ← Surcharges prod  
└── templates/  
    ├── deployment.yaml  
    ├── service.yaml  
    ├── ingress.yaml  
    └── configmap.yaml  

### Étape 7.2 — Référencer le service dans le dépôt

Action : Ouvrir une Merge Request sur le dépôt de la plateforme pour déclarer votre nouveau service.

1. Cloner le dépôt : `LIEN_DEPOT`
2. Créer une branche `feat/onboard-<nom-du-service>`
3. Copier votre dossier `helm/` dans le répertoire approprié du dépôt
4. Ouvrir une MR en suivant le template de MR d'onboarding : `EXEMPLE_MR_ONBOARDING`
5. Assigner la MR à l'équipe platform : `LIEN_EQUIPE_PLATFORM`

Documentation complète du processus d'onboarding Kube :

- `https://onboarding.dev.kube.insee.fr/`
- `https://demo.insee.io/`

Une fois la MR mergée, ArgoCD prendra en charge le déploiement automatiquement sur l'environnement dev. Vous n'avez rien d'autre à faire.

Documentation ArgoCD de la plateforme :

- `https://argo-cd.readthedocs.io/en/stable/`
- `https://gitops-kubernetes.developpement.insee.fr/applications` (Juste l'application, c'est pas de la doc (mais on peut accéder à la doc depuis cette page))

-----------------------------------------------------

## Phase 8 — Documentation

### Étape 8.1 — Remplir le README

Action : Compléter le fichier `README.md` en suivant le template standard.

Template README standard :

- `https://github.com/Louis3797/awesome-readme-template`
- `https://github.com/othneildrew/Best-README-Template`

Sections obligatoires :

- Description du service
- Prérequis pour démarrer en local
- Comment lancer le projet
- Variables d'environnement attendues
- Liens utiles (ArgoCD, Grafana, GitLab...)

### Étape 8.2 — Remplir le Runbook

Action : Compléter le fichier `RUNBOOK.md` en suivant le template standard.

Template Runbook standard :

- `https://www.solarwinds.com/sre-best-practices/runbook-template` (Pour avoir les étapes)
- `https://github.com/runbear-io/awesome-runbook/blob/main/docs/kubernetes/decoding-secrets.md` (Bien pour la forme)

Sections obligatoires :

- Comment démarrer / arrêter le service
- Comment consulter les logs
- Que faire en cas d'alerte
- Contacts de l'équipe

-----------------------------------------------------

## Récapitulatif des phases

- Phase 1 - Dépôt GitLab : Dépôt créé et structuré, conventions configurées
- Phase 2 - Backend Java : SpringBoot généré, Postgres configuré, Logs et Health Checks configurés
- Phase 3 - Frontend React : (si besoin) Squelette React créé
- Phase 4 - Docker : Dockerfiles créés et vérifiés en local
- Phase 5 - Pipeline CI : Premier pipeline sur GitLab
- Phase 6 - Secrets & Sécurité : Secrets dans Vault, GitLeaks actif
- Phase 7 - Déploiement Kubernetes : Chart Helm créé, MR ouverte
- Phase 8 - Documentation : README et Runbook prêts
