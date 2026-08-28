# De quoi est typiquement composé un Golden Path ?

Un Golden Path peut prendre différentes formes selon les besoins qu’il adresse.
Il cible un usage spécifique du cycle de vie logiciel.

## Typologie des Golden Paths

On peut distinguer plusieurs grandes catégories de Golden Path, chacune correspondant à un besoin particulier.

### 1. Golden Path de création de projet

Ce Golden Path permet de **créer rapidement un nouveau projet conforme aux standards**.

**Objectif :** Démarrer un projet en quelques minutes

- Éviter les décisions initiales complexes
- Garantir une base saine et homogène

**Composants typiques :**

- Templates de projet
  - Structure de dépôt
  - Organisation des dossiers
  - Conventions de nommage
- Configuration initiale
  - Gestion des dépendances
  - Configuration
  - Gestion des environnements (?)
- Pipeline CI/CD de base
  - Build
  - Tests
  - Analyse statique / dynamique
- Observabilité
  - Logs
  - Métriques
  - Health checks
- Configuration sécurité
  - Gestion des secrets
  - Gestion des dépendances (encore)
  - Bonnes pratiques par défaut
- Standards de qualité
  - Linting
  - Stratégie de tests
- Documentation de démarrage
  - README
  - Doc

---------------------------------------------------------------------------------

### 2. Golden Path de déploiement

Ce Golden Path standardise la manière dont une application est déployée et exposée.

**Objectifs :**

- Rendre les déploiements simples et fiables
- Uniformiser les environnements (dev, staging, prod)

**Composants typiques :**

- Définition des environnements
  - Variables d’environnement
  - Configuration
- Stratégies de déploiement
  - Blue/Green / Rolling update / Canary
- Configuration réseau
  - Exposition
- Gestion des versions
  - Tag
  - Versioning applicatif
- Automatisation
  - CD
  - Rollback

---------------------------------------------------------------------------------

### 3. Golden Path de développement local

Ce type de Golden Path vise à standardiser l’expérience de développement local.

**Objectifs :**

- Réduire le temps de setup
- Garantir un environnement reproductible

**Composants typiques :**

- Environnement local standardisé
  - Scripts de démarrage
  - Configuration locale
- Dépendances simulées ou embarquées
  - Bases de données locales / Mock
- Commandes simplifiées
  - Lancement de l’application
  - Exécution des tests
- Documentation
  - Doc aide
  - Debug

---------------------------------------------------------------------------------

### 4. Golden Path CI/CD

Ce Golden Path définit les standards d’intégration et de livraison continue.

**Objectifs :**

- Garantir la qualité du code
- Automatiser les processus complexes

**Composants typiques :**

- Pipelines standardisés
  - Build
  - Tests automatisés
  - Analyse statique / dynamique
- Quality gates
  - Coverage minimum
  - Linting obligatoire
  - ...
- Gestion des artefacts
  - Packaging
  - Publication
- Automatisation des déploiements
- Notifications
  - Échecs
  - Succès

---------------------------------------------------------------------------------

### 5. Golden Path d’observabilité

Ce Golden Path fournit un cadre standard pour monitorer et comprendre le comportement des services.

**Objectifs :**

- Rendre les services observables par défaut
- Faciliter le diagnostic et la maintenance

**Composants typiques :**

- Logs
- Métriques
- Dashboards prédéfinis
- Alertes
  - Seuils
  - Notifications

---------------------------------------------------------------------------------

### 6. Golden Path de sécurité

Ce Golden Path intègre les bonnes pratiques de sécurité dès le départ.

**Objectifs :**

- Réduire les risques
- Standardiser les pratiques de sécurité

**Composants typiques :**

- Gestion des identités et des accès
- Gestion des secrets
- Scans de sécurité
  - Dépendances
  - Conteneurs
- Politiques de sécurité
  - Conformité
  - Restrictions
- Bonnes pratiques
  - Principe du moindre privilège
  - Sécurisation des endpoints
  - Rôles
  - ...

---------------------------------------------------------------------------------

### 7. Golden Path : Base de données

Ce type de Golden Path cible la gestion des données et des bases de données.

**Objectifs :**

- Simplifier l’usage des bases de données
- Garantir la cohérence des pratiques

**Composants typiques :**

- Fournissement des bases de données
- Migrations
- Accès sécurisé
- Backups
- Monitoring des performances

---------------------------------------------------------------------------------

### 8. Golden Path “full stack”

Certains Golden Paths couvrent plusieurs dimensions à la fois.

**Objectifs :**

- Fournir un parcours complet de bout en bout
- Minimiser les interactions entre équipes

**Composants typiques :**

- Template de service
- Pipeline CI/CD
- Déploiement
- Observabilité
- Sécurité intégrée
- Documentation complète

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

## Composants transverses à tous les Golden Paths

Quel que soit leur type, les Golden Paths partagent souvent des éléments en commun.

### 1. Templates

- Scaffolding de projet
- Génération automatique de code / configuration

---------------------------------------------------------------------------------

### 2. Automatisation

- Scripts
- Pipelines
- Actions reproductibles

---------------------------------------------------------------------------------

### 3. Documentation

- Guides de démarrage rapide
- Exemples concrets
- Cas d’usage

---------------------------------------------------------------------------------

### 4. Standards et conventions

- Nommage
- Organisation
- Bonnes pratiques

---------------------------------------------------------------------------------

### 5. Interfaces d’accès (???)

- CLI
- Portail développeur
- API internes

---------------------------------------------------------------------------------

### 6. Intégrations avec l’écosystème

- Outils de CI/CD
- Plateforme de déploiement
- Outils d’observabilité
- Systèmes de sécurité

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

## Granularité des Golden Paths

On peut avoir :

- Des Golden Paths unitaires
  - Exemple : uniquement l'observabilité
- Des Golden Paths combinés
  - Exemple : Observabilité + Sécurité
- Des Golden Paths complets
  - Exemple : Golden Path "full stack"

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

## Conclusion

Un Golden Path peut couvrir différents aspects du développement d'une application :

- Création du projet
- Développement
- CI/CD
- Déploiement
- Observabilité
- Sécurité
- Données

Chaque type repose sur un ensemble de composants récurrents :

- Templates
- Automatisation
- Standards
- Documentation
- Intégrations

Ces éléments permettent de proposer des parcours cohérents, adaptés aux différents besoins des développeurs, tout en garantissant l’alignement global du SI.
