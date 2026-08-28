# Panorama des outils de la stack par couches fonctionnelles.

Afin d’éviter une simple liste d’outils et de refléter la réalité d’usage des équipes de développement, la stack technique est présentée par **couches fonctionnelles**. Chaque couche représente une étape ou une responsabilité dans le parcours d’une application, du poste du développeur à la production.

## Cycle de vie d’une application (de l’idée à la production)

Le parcours théorique d’un développeur pour créer et déployer une nouvelle application suit plusieurs étapes clés. Peu importe la technologie utilisée pour déployer les développeurs font à minima:

- Initialisation du projet:
  - Création du repository Git et configuration des conventions internes (naming, branches, pipelines).
  - Sélection des dépendances et du framework à utiliser.
- Développement et tests locaux
  - Implémentation des fonctionnalités et tests unitaires.
  - Simulation d’accès aux services externes (bases de données, API internes).
- Intégration continue
  - Mise en place des pipelines CI:
    - Validation des tests d’intégration
    - Validation qualité du code.
    - Scan vulnérabilité
    - Construction et dépôt du livrable dans un registre
- Configuration des environnements
  - Dépendra de la technologie cible choisi
  - Mise en place client OIDC
- Déploiement en staging / production
  - Dépendra de la technologie cible choisie
- Monitoring et maintenance
  - Mise en place de l’observabilité (logs, métriques, alerting).
  - Suivi et correction des incidents post-déploiement.

## Couches identifiées

Les besoins fonctionnels identifiés sont :

- **Développement applicatif**  
  Langages, frameworks, pratiques de développement.

- **Build & packaging**  
  Transformation du code source en artefacts déployables.

- **CI/CD**  
  Automatisation des tests, contrôles qualité et déploiements.

- **Exécution & orchestration**  
  Environnements d’exécution, conteneurisation, orchestration.

- **Observabilité**  
  Logs, métriques, traces et supervision.

- **Sécurité & conformité**  
  Gestion des accès, secrets, scans et politiques.

- **Données & messaging**  
  Bases de données, caches, systèmes de messages.

## Développement applicatif

### Langages et frameworks

- Langages majoritairement utilisés :
  - Java (11 :arrow-right: 25):
  - React: JavaScript / TypeScript (ViteJs/NodeJs)
  - Python (un jour) : FastApi
  - R (4.?.?)

!!!info

    Plusieurs générations technologiques coexistent.

- Frameworks dominants :
  - Frameworks backend
    - Java:
      - Spring Boot (ecosysteme SpringData, SpringSecurity)
      - Spring/Hibernate avec JSP (legacy)
      - Struts avec ou sans Hibernate (legacy +++)
    - Java Batch:
      - Spring Batch
      - implémentation batch manuelle
  - Frameworks frontend (React):
    - Couche Authentification :
      - AxaOIDC
      - OIDC-SPA
    - Couche UI :
      - Material-UI
      - DSFR
    - Moteur d'execution:
      - Vite
      - Webpack (legacy)

### Packaging et build

- Java:
  - Compileur :
    - Maven
- React:
  - Compileur:
    - npm
    - yarn
    - pnpm
- Image Docker:
  - Construction image:
    - kaniko
  - Publication image:
    - crane
- Registre de livrable:
  - Nexus
  - Harbor
  - Gitlab Registry

!!!info

    3 registres :

    - Nexus en tant que proxy internet + registre pour les livrables legacy
    - Gitlab Registry : pour les livrables de type docker
    - Harbor : non accessibles aux utilisateurs, utilisés pour des garanties de disponibilités.

### Tests

- Java:
  - Test interface : selenium
  - Test fonctionnel : cucumber
  - Test unitaire: Junit
- React:
  - Test interface : cypress, Playwright
  - Test unitaire : Jest / vitest

!!!info

    Couverture de tests et pratiques de tests trés hétérogènes. https://tableau-de-bord-applications.insee.fr/indicateur/qualiteTable

### Lint et Scan

- Linter :
  - Java:
    - Spotless
  - React:
    - prettier
    - eslint
  - Docker:
    - hadolint
- transverses:
  - Scan de bonne pratique de développement:
    - sonar
    - hadolint
  - Scan de cve:
    - trivy

## CI/CD, automatisation, déploiement

- Outils CI utilisés :
  - GitLab CI
- Pratiques observées :
  - pipelines définis par projet:
    - ~~pas de gitflow commun~~ :arrow-right: branche main protégé, passage par mr, des steps dans le pipeline qui n'arrive pas au même moment
    - release flow différent: tag vs click
    - usage de snippets / templates / components
- Deploiement:
  - pipeline de promotion + GitOps
  - majiba3

## Environnements d’exécution et production

Environnement:

- Monde Kube:
  - Ordonnanceur :
    - Argoworkflow
    - Cronjob
  - Conteneurisation :
    - Docker
  - Orchestration :
    - Kubernetes comme standard
    - clusters mutualisés
  - Création environnement / Déploiement :
    - Manifests Kubernetes custom
    - Chart Helm
    - Chart Helm KubeApp (Générique/Workflows)
    - Pipeline de promotion
  - Gestion:
    - Développeur responsable de ses images et de leur MCO
    - Ops responsable de fournir l'environnement d'execution
- Monde VM:
  - Ordonnanceur:
    - Rundeck
  - Création environnement :
    - Automate maison (rainette)
    - iac
  - Configuration moteur applicatif
    - puppet
    - ansible
  - Deploiement:
    - majiba3
  - Gestion :
    - Développeur responsable du jar, de la gestion simple de la plateforme (cpu/ram/stockage + FDS) par le biais des outils maison fourni par les ops
    - Ops responsable de fournir l'environnement d'execution du déploiement (par le biais des outils) et du MCO de l'environnement (mise à jour)

!!!info

    Actuellement: double runtime complet. Un runtime legacy et un runtime CloudReady. La DSI a une stratégie KubeFirst.

## Observabilité

- Logs :
  - Elastic (VM)
  - loki (Kubernetes)
- Metrics :
  - Prometheus (Kubernetes)
  - Elastic (VM)
- Traces :
  - Rien (Kubernetes)
  - Elastic (VM)
- UI :
  - elastic (VM)
  - Grafana (Kubernetes)

!!!info

    Actuellement: double stack de monitoring à la cible une seule (Elastic)

## Sécurité et conformité

- Stockage des secrets :
  - Vault (VM/Kubernetes)
  - Secret Kubernetes
- Chiffrement de secrets
  - SealedSecrets
  - Hiera
- Sécurité applicatives:
  - Keycloak

## Données et messaging

- Stockage:
  - applishare
  - S3
- Base de données:
  - postgres (Beaucoup)
  - elastic
  - MongoDB (percona)