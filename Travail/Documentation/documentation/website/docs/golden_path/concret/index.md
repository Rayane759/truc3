# En quoi consiste notre Golden Path ?

## Objectif

Ce Golden Path vise à permettre la **création rapide et standardisée d'un nouveau projet applicatif**.

Il permet de :

- Démarrer un projet rapidement
- Éviter les décisions techniques initiales complexes
- Garantir une base homogène, maintenable et conforme aux standards internes

Ce Golden Path cible principalement les **applications Java basées sur Spring Boot**, prêtes à être déployées dans un environnement Kubernetes.

------------------------------------------------------------------------
------------------------------------------------------------------------

## Vue d'ensemble

Le fonctionnement global du Golden Path peut être résumé comme une chaîne allant de la création du projet jusqu'à sa mise en production :

Initialisation -> Développement -> Intégration -> Déploiement -> Exploitation

Avec les outils associés :

Code : GitLab + Conventional Commits  
Build : Maven + GitLab CI  
Qualité : SonarQube + Checkstyle + Spotless + JaCoCo  
Sécurité : Vault + Keycloak + OWASP + GitLeaks  
Deploy : ArgoCD + Helm + Kubernetes  
Observabilité : Micrometer + Loki + Prometheus + Grafana

------------------------------------------------------------------------
------------------------------------------------------------------------

## Fonctionnement

Le Golden Path s'utilise comme un **parcours guidé en plusieurs étapes**, depuis la création du projet jusqu'à son exploitation.

### 1. Initialisation du projet

Le développeur crée un nouveau service à partir d'un template standardisé.

- Résultat
  - Un dépôt initialisé
  - Une structure de projet clé en main
  - Une configuration conforme aux standards

- Outils
  - GitLab (création du repository)
  - Spring Initializr (personnalisé)
  - Templates internes configurés

------------------------------------------------------------------------

### 2. Développement

Le développeur implémente le dode applicatif en s'appuyant sur une base déjà configurée.

- Résultat
  - Code structuré et cohérent
  - Respect des conventions de développement

- Outils
  - Conventional Commits
  - `.editorconfig` (<https://editorconfig.org/>)
  - Pre-commit hooks

------------------------------------------------------------------------

### 3. Intégration continue (CI)

Chaque commit déclenche automatiquement une pipeline CI.

- Résultat
  - Code compilé et testé
  - Qualité mesurée
  - Sécurité vérifiée

- Outils
  - GitLab CI
  - Maven
  - JUnit 5 + Mockito
  - JaCoCo (Couverture de code)
  - SonarQube (Qualité du code)
  - Checkstyle + Spotless (Linting + Formatting)
  - OWASP Dependency-Check
  - GitLeaks

------------------------------------------------------------------------

### 4. Déploiement continu (CD)

Une fois validé, le commit est déployé automatiquement.

- Résultat
  - Application déployée sur Kubernetes
  - Environnements cohérents

- Outils
  - ArgoCD
  - Helm
  - GitLab Container Registry / Nexus

------------------------------------------------------------------------

### 5. Exploitation et observabilité

La modification est observable dès son déploiement.

- Résultat
  - Monitoring actif
  - Diagnostic facilité

- Outils
  - Prometheus (+ Micrometer)
  - Grafana
  - Logback + Loki (mais on a ELK ???)
  - Spring Boot Actuator

------------------------------------------------------------------------

### 6. Sécurité intégrée

La sécurité est présente à chaque étape.

- Résultat
  - Gestion des secrets
  - Identification
  - Sécurité des dépendances
  - Secrets dans le code

- Outils
  - Vault + Spring Cloud Vault
  - Keycloak + Spring Security
  - OWASP Dependency-Check
  - GitLeaks

------------------------------------------------------------------------

### 7. Documentation

La documentation est présente dès le début du projet.

- Outils
  - README template
  - Runbook

------------------------------------------------------------------------
------------------------------------------------------------------------

## Résumé

Ce Golden Path fournit un **parcours complet, intégré et automatisé** permettant de :

- Créer un projet rapidement
- Garantir qualité et sécurité
- Déployer automatiquement
- Assurer une observabilité immédiate
- Avoir une documentation complète

------------------------------------------------------------------------
------------------------------------------------------------------------

## Réalisation

### Priorité des composants

Dans cette partie, nous allons définir les différents niveaux de priorité de chaque composant de notre Golden Path.

Ces priorités seront divisés en 3 niveaux :

- Priorité forte
- Priorité moyenne
- Priorité faible

#### 1. Priorité forte

Les composants listés dans cette partie sont les composants nécessaires pour que le Golden Path soit utilisable.

- Structure du dépôt
- Configuration du projet
- Code structuré et cohérent
- Respect des conventions de développement
- Pipeline CI
- ArgoCD
- JUnit 5 + Mockito
- Health Checks
- Logs
- Vault
- GitLeaks
- README
- Runbook

#### 2. Priorité moyenne

- Nexus / GitLab Packages
- JaCoCo
- SonarQube
- Checkstyle + Spotless
- Micrometer, Prometheus et Grafana
- Loki, LogBack (ou ELK)
- KeyCloak + Spring Security
- OWASP Dependancy-Check
- Pre-commit hooks

#### 3. Priorité faible

bla

------------------------------------------------------------------------

### MVP

#### Définition du MVP

Nous visons d'inclure dans notre **MVP** toutes les features présentes dans la liste des composants à **Priorité forte**.

#### Objectif du MVP

Le MVP que nous essayons d'atteindre a pour objectif de :

- Créer un repo GitLab structuré et prêt
- Créer un projet Spring Boot buildable (Maven ou Gradle)
- Créer une image Docker buildée et poussée automatiquement
- Gérer un déploiement ArgoCD
- Créer des health checks fonctionnels
- Gérer des logs JSON structurés dès le premier démarrage
- Gérer les secrets via Vault
- Avoir GitLeaks actif dans le pipeline
- Créer un README et un runbook pour démarrer seul

#### Fonctionnement global du MVP

Notre MVP fonctionnera de la manière suivante :

##### 1 - Interaction avec le CLI

Le développeur lance la commande `blabla` dans son terminal.

Le terminal affiche des questions une à une auxquelles doit répondre le développeur (exemple : Nom de l'application).

Une fois les informations saisies, les données sont enregistrées pour la suite

##### 2 - Génération du squelette du projet

Le Golden Path appelle l'API Spring Initializr avec un ensemble de dépendances déterminées à l'avance par le Golden Path. Il récupère ensuite un fichier ZIP avec la structure Maven.

##### 3 - Application des templates

Le Golden Path applique des templates en injectant les variables entrées par le développeur dans le CLI.

Le premier template sert à générer le contenu du dossier de l'application et sera alors fusionné avec le squelette généré auparavant.

Le deuxième template va lui s'occuper de générer les fichiers liés à la partie GitOps. (????)

##### 4 - Création du dépôt GitLab

Le Golden Path va :

- Créer le dépôt GitLab avec le namespace de l'équipe (entré par le développeur dans le CLI)
- Configure le dépôt : ??????
- Pousse le code généré auparavant sur la branche main (avec un commit standard)
- Configure les variables CI/CD du dépôt

Le développeur obtient alors un dépôt GitLab fonctionnel et accessible.

##### 5 - Pipeline CI

Le fichier `.gitlab-ci.yml` généré auparavant permet de déclencher la pipeline qui réalise les tâches suivantes :

- Build : Maven
- Tests : JUnit 5
- Build de l'image Docker : ...
- GitLeaks

Le développeur obtient alors un premier pipeline CI qui tourne (et qui devrait marcher pour le commit initial ...).

##### 6 - Merge Request

Le Golden Path :

- Clone le dépôt Git existant
- Crée une branche dédiée
- Applique la configuration GitOps (???)
- Pousse la branche sur le dépôt
- Ouvre une Merge Request avec un format standard
- (La Merge Request est validée par un responsable désigné par le Golden Path ?)

#### Composants du Golden Path

- CLI : Python (Typer)
- Templates : Git + Jinja / copier
  - Jinja :
    - Simple à démarrer
    - On doit gérer le moteur de rendu
    - Il faut implémenter les mises à jours des templates manuellement
    - Pas de format standard
    - Totalement flexible
  - Copier :
    - Coût d'entrée non nul
    - Moteur géré par Copier
    - Mise à jour des templates : Natif dans Copier (`killer feature`)
    - Format standardisé et documenté
    - Très flexible tant qu'on reste dans le cadre de ce que permet Copier
  - Copier permet de propager des changements de template sur des projets déjà générés (copier update). Avec Jinja, on doit le coder nous-mêmes.
- GitLab API : python-gitlab
- Scaffolding : Spring Initializr API
- GitOps : repo Git + MR auto
- CI : GitLab CI templates

#### Notes

##### Technologies essayées

###### Initialisation du projet

- Hébergement Git :
  - Gitlab
  - Github
  - Bitbucket
  - Gitea
  - Azure DevOps / AWS CodeCommit

- Génération du projet :
  - Spring Initializr
  - Bootify (Moins bien : Moins maintenu)
  - JHipster (Moins bien : Trop lourd)

- Template de dépôt
  - Yeoman
  - Cookiecutter

###### Développement

- Conventions de commit :
  - Conventional Commits
  - Guidelines GitHub (Commitizen / Semantic-Release) (Plus pour les release automatiques que pour les conventions de commit)

- Configuration de l'éditeur (`.editorconfig`) :
  - .editorconfig
  - Formateurs / Linters configurables
    - Prettier (Pas en Java du coup)
    - Google Java Format

- Pre-Hooks
  - GitLab / GitHub Hooks (intégrés)
  - Framework pre-commit
  - Lefthook

###### Intégration Continue (CI)

- CI :
  - GitLab CI (surtout ça)
  - Jenkins (Pourquoi pas)
  - GitHub Actions (Pourquoi pas)
  - Moins pertinents :
    - Travis CI
    - Circle CI
    - Azure Pipelines
    - TeamCity
    - Bamboo
    - Bitbucket Pipelines
    - Buildkite
    - Concourse
    - Drone
    - CircleCI

- Gestionnaire de dépendances et build :
  - Maven
  - Gradle
  - Ant (Obsolète ?)
  - Bazel (Pas pertinent sauf si on est en très gros mono-repo)
  - Bucl (Pas pertinent)

- Frameworks de tests :
  - Tests unitaires :
    - JUnit 5
    - TestNG
    - Spock (Si on utilise Groovy, mais pas pertinent en Java pur)
    - Cucumber (Tests d'intégration / BDD ?)
  - Mock :
    - Mockito
    - EasyMock
    - JMockit
    - PowerMock

- Couverture de code :
  - JaCoCo
  - Cobertura (Obsolète)
  - Clover (Atlassian) (Non maintenu,Propriétaire)
  - Emma (Obsolète)
  - JCov

- Analyse statique :
  - SonarQube
  - Checkstyle (?)
  - Codacy (Saas externe : Confidentialité ?)
  - DeepSource (Saas externe : Confidentialité ?)
  - Coverity Scan (Cher)
  - Checkmarx (Cher)
  - CodeQL

- Linter / Formatter :
  - Checkstyle
  - PMD (Déjà "inclus" avec SonaQube ?)
  - SpotBugs (Déjà "inclus" avec SonaQube ?)
  - Spotless
  - Google Java Format

- Sécurité des dépendances :
  - OWASP Dependancy-Check
  - Snyk
  - Trivy
  - Sonatype Nexus Lifecycle
  - Mend/WhiteSource (Cher)
  - Black Duck (Synopsys) (Cher)
  - JFrog Xray
  - FOSSA (Plus pour la gestion des licences open source)
  - Checkmarx SCA

- Détéction de secrets :
  - GitLeaks
  - GitLab Secret Detection
  - TruffleHog
  - GitGuardian
  - Yelp Detect-Secrets (Moins maintenu)
  - Talisman
  - SpectralOps (Payant)
  - GitHub (scanners intégrés ?)

###### Déploiement Continu (CD)

- GitOPS / CD :
  - ArgoCD
  - FluxCD
  - Jenkins X (Peu maintenu)
  - Spinnaker (Très lourd)
  - CodeFresh
  - Harness
  - Octopus Deploy (Non pertinent)
  - GitLab CI/CD
  - Tekton (Bien pour Kube natif, mais redondant avec ArgoCD dans notre contexte)
  - GitHub Actions + GitHub Deployment

- Gestion des manifests Kubernetes :
  - Helm
  - Kustomize
  - Skaffold
  - Jsonnet/Tanka (Trop complexe)
  - Kapitan (Très confidentiel)
  - CDK8s

- Gestion des artefacts :
  - DockerHub
  - Amazon ECR / Azure Container Registry / Google Artifact Registry (Spécifiques)
  - GitHub Packages
  - Harbor
  - Sonatype Nexus Repository
  - JFrog Artifactory
  - Quay (Red Hat)

###### Observabilité

- Métriques :
  - Prometheus
  - Graphite (avec StatsD) (Remplacé par Prometheus)
  - InfluxDB (avec Telegraf/Chronegraf)
  - VictoriaMetrics
  - Cortex / Mimir (Backends Prometheus distribués, pertinents si on a besoin de scalabilité sur Prometheus)
  - AWS CloudWatch / Azure Monitor / Google Cloud Monitoring (Spécifiques)

- Dashboards :
  - Grafana
  - Kibana (avec ElasticSearch / OPensearch pour les logs)
  - Chronograf (avec InfluxDB au-dessus)

- Logs :
  - ELK / EFK (ElasticSearch ; Logstash / Fluentd ; Kibana)
  - Loki / Logback
  - Graylog
  - **FluentBit** + ElasticSearch + Kibana

- Surveillance :
  - Spring Boot Actuator (santé et métriques, avec Micrometer)
  - MicroProfile Health/Metric (Pertinent si on utilise Quarkus ou Micronaut, mais pas avec SpringBoot)
  - Dropwizard Metrics (Remplacé par Micrometer)
  - Services APM (New Relic, Datadog APM, Instana, Dynatrace, ...) (Fait tout, mais cher)

###### Sécurité

- Gestion des secrets :
  - Vault / Keycloak

- Authentification :
  - Keycloak

- Analyse de sécurité :
  - OWASP Dependancy-Check ; GitLeaks

###### Documentation

- README :
  - MkDocs
  - Docusaurus
  - Antora (AsciiDoc)
  - GitBook (Version gratuite assez limitée)
  - Sphinx (Orienté Python)
  - Swagger/OpenAPI (Documentation API ; "SpringDoc")
  - Wiki Git (GitLab Wiki ; GitHub Wiki)

- Runbook :
  - Confluence
  - GitLab Pages
  - Notion

##### Difficultés rencontrées

bla

------------------------------------------------------------------------

### Itérations

Dans cette partie, nous allons lister les différentes itérations faites au Golden Path.

En effet, comme dit auparavant, un Golden Path est en constante évolution. Ainsi, nous modifierons au fil de l'eau notre Golden Path selon les retours et les besoins des développeurs.

Ces modifications seront réalisées sous forme d'**itération** que nous listerons ci-dessous.

#### Itération 1

bla
