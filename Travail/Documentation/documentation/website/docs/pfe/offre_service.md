# L'Offre de service Platform Engineering

L'offre de service Platform Engineering de l'INSEE est un ensemble de services destinés aux équipes réalisant du développement à l'INSEE, permettant de réduire la charge cognitive liée à la plomberie technique tout en bénéficiant de parcours standardisés (Golden Paths), de self-service outillé le tout intégrant sécurité et observabilité *by default*. Elle permet aux équipes projets de se concentrer sur leur code métier, sans avoir à maîtriser individuellement l'ensemble des outils et plateformes sous-jacents (Kubernetes, CI/CD, GitOps, gestion des secrets...).

## Périmètre de l'offre de service

Cette offre s'adresse à tous les développeurs de l'Insee qui le souhaitent, avec une priorisation initiale sur les équipes travaillant dans le **monde Kubernetes**.

Les trois personas identifiés lors du constat terrain sont ciblés :

- **Le Consommateur** : veut que ça marche sans "réfléchir" — cible principale du self-service et des Golden Paths
- **Le Contributeur** : veut comprendre et contrôler — cible des interfaces avancées et de la contribution au catalogue
- **Le Manager/Lead** : veut piloter sans être dans le détail — cible des dashboards et de la visibilité transverse

Le détail des services proposés à ces publics est présenté ci-dessous, dans la section [Ambition et Services](#ambition-et-services).

## Ambition et Services

L'ambition de cette offre est de proposer aux équipes projets un catalogue de services large et complet, permettant d'automatiser le déploiement et l'exploitation tout en réduisant la charge cognitive et en garantissant les standards de qualité et de sécurité.

Le service DevExperience — portée par l'équipe [IDDA](./organisation.md) au démarrage, avant la mise en place d'un équipe dédiée, anime cette offre et accompagne les équipes projets dans son adoption.

La plateforme s'organise autour de **6 domaines fonctionnels**, couvrant les 18 cas d'utilisation identifiés lors du constat terrain :

* **Portail développeur & point d'entrée unique** :
  point d'entrée centralisé vers l'ensemble des ressources de la plateforme
    * Catalogue des services (composants, owners, dépendances, état de santé)
    * Documentation centralisée et contextualisée (TechDocs, liée à chaque service)
    * Annuaire des équipes et interlocuteurs
    * État des services transverses (incidents, maintenances, changements planifiés)
    * Feed des changements passés et à venir

  *Cas d'utilisation couverts : UC1 (point d'entrée unique), UC2 (interlocuteur unique), UC8 (documentation contextualisée), UC17 (feed des changements), UC18 (catalogue de services)*

* **Onboarding & parcours guidés** :
  accompagnement des nouveaux développeurs et des nouvelles équipes
    * Parcours d'onboarding guidé (du setup de poste au premier déploiement)
    * Documentation de démarrage rapide par profil (nouveau dev, dev existant migrant vers Kube, lead technique)
    * Liens vers les formations et ressources existantes

  *Cas d'utilisation couverts : UC3 (onboarding guidé)*

* **Golden Paths & templates** :
  parcours standardisés pour les opérations courantes de création et de configuration
    * CLI de création de projet (template Spring Boot + GitLab + CI/CD + GitOps + Vault + observabilité)
    * Catalogue de templates maintenus et évolutifs (via Copier avec mise à jour native des projets existants)
    * Scaffolding via Spring Initializr personnalisé
    * Configuration guidée avec validation et pré-remplissage des bonnes pratiques
    * Contribution au catalogue par les profils avancés

  *Cas d'utilisation couverts : UC4 (créer un service via template), UC5 (contribuer au catalogue), UC6 (configurer sans erreur)*

* **CI/CD & déploiement** :
  simplification et fiabilisation du pipeline de livraison
    * Pipelines CI/CD standardisés (GitLab CI templates)
    * Déploiement GitOps via ArgoCD avec suivi en temps réel
    * Visualisation du pipeline (étapes, durées, erreurs claires)
    * Intégration des scans de sécurité tôt dans le pipeline (shift-left)
    * Feedback rapide et messages d'erreur exploitables

  *Cas d'utilisation couverts : UC9 (déployer simplement), UC10 (visualiser le pipeline), UC11 (feedback rapide)*

* **Environnements & infrastructure self-service** :
  provisionnement d'environnements et de ressources en autonomie
    * Provisionnement d'environnement Kubernetes via UI ou CLI (self-service, sans ticket)
    * Configuration de ressources courantes (bases de données, secrets Vault, clients Keycloak) via des interfaces simplifiées
    * Appui sur les outils existants des capability teams (KubeApp, PDD, IAHS) avec une couche d'abstraction

  *Cas d'utilisation couverts : UC7 (provisionner un environnement à la demande)*

* **Observabilité & gestion d'incident** :
  visibilité sur la santé des applications et aide au diagnostic
    * Dashboard unifié par service (logs, métriques, alertes, état des déploiements)
    * Alertes pertinentes et filtrées
    * Aide au diagnostic automatisé (premières pistes de recherche en cas d'incident)
    * Runbooks accessibles et liés au service concerné
    * Identification du bon interlocuteur en cas d'escalade

  *Cas d'utilisation couverts : UC12 (santé des services), UC13 (alertes pertinentes), UC14 (diagnostic automatisé), UC15 (trouver le bon contact), UC16 (runbook accessible)*

### Ce qui n'est PAS inclus

La plateforme ne se substitue pas aux capability teams existantes. Elle s'interface avec elles.

Hors périmètre de l'équipe DevExperience :

- L'exploitation Kubernetes (gestion des clusters, ingress, scaling, operators) → Équipe Runtime / KubeApp
- La gestion des bases de données (provisionnement, backup, monitoring BDD) → Équipe Data Services / PDD
- La gestion des identités et secrets (OIDC, IAM, coffres Vault) → Équipe Security / IAHS
- La stack d'observabilité (Prometheus, Grafana, Loki) → Équipe Observabilité
- Le réseau (exposition, certificats) → Équipe Réseau

La plateforme **consomme** les services de ces équipes et les expose de manière unifiée et simplifiée aux développeurs. Chaque capability team reste responsable de son périmètre technique.

## Bénéfices de l'offre

L'offre de service Platform Engineering porte plusieurs bénéfices, elle permet de :

- **Réduire la charge cognitive** : en centralisant, simplifiant et automatisant les interactions avec l'infrastructure et les outils de production, les développeurs se concentrent sur le code métier plutôt que sur la plomberie technique.
- **Accélérer le déploiement** : les Golden Paths et le self-service réduisent significativement le temps et l'effort nécessaires pour créer, configurer et déployer un nouveau service.
- **Garantir la sécurité et l'observabilité *by default*** : chaque parcours proposé intègre nativement les scans de sécurité, la mise en conformité et l'observabilité, sans effort supplémentaire pour les équipes projets.
- **Favoriser la découvrabilité** : le portail centralise les services, les équipes, les dépendances et l'état du SI, réduisant la dépendance à une poignée de sachants.
- **Fiabiliser les opérations courantes** : la standardisation des templates et des pipelines CI/CD réduit les erreurs de configuration et améliore la reproductibilité des déploiements.

## Qualité de service et engagements

### Qualité de service

Les équipes projets bénéficient d'un accompagnement par l'équipe DevExperience, portée par l'équipe IDDA au démarrage à partir de septembre 2026, avant la mise en place d'un service DevExperience dédié (voir [ADR-003](./adr/adr-003-insertion-equipe.md)).

Le modèle d'interaction privilégie le **self-service en premier niveau** : la plateforme (portail, CLI, templates, documentation) doit permettre aux équipes de trouver et de faire ce dont elles ont besoin en autonomie. Un **canal unique** (Tchap dédié + ticketing) sert de recours lorsque le self-service ne suffit pas ; l'équipe DevExperience qualifie alors le besoin et redirige si nécessaire vers la capability team concernée.

### Engagement

L'offre étant en cours de construction (démarrage prévu en septembre 2026), les niveaux de service (DIMA/PDMA) ne sont pas encore définis pour l'ensemble de la plateforme. Ils seront formalisés progressivement, domaine fonctionnel par domaine fonctionnel, au fur et à mesure de la mise en production des services, et en cohérence avec les engagements déjà pris par les capability teams sous-jacentes (KubeApp, PDD, IAHS, Observabilité, Réseau) sur leur propre périmètre.
