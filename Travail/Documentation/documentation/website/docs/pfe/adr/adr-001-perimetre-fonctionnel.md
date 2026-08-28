# ADR-001 - Périmètre fonctionnel de l'offre de service Platform Engineering

| | |
|---|---|
| **Référence** | ADR-001 |
| **Statut** | Proposé : en cours de validation |
| **Auteurs** | Équipe DevExperience |
| **Public** | ÉquipeDevExperiencee · équipes capabilities · architectes du SI · décideurs SI |

> L'ADR-001 délègue la définition de la frontière de responsabilité (ce qui relève ou non de l'équipe DevExperience) à [ADR-002 — Architecture fonctionnelle DevExperience](./adr-002-architecture-fonctionnelle.md), qui en est désormais la source autoritative. ADR-001 conserve son rôle propre : décrire **l'offre de service vue de la demande** (les domaines fonctionnels et les cas d'utilisation qu'ils couvrent). Voir la section « Historique » en fin de document.

## Contexte

Le constat terrain (8 interviews, 4 focus groupes, 4 SNDI) a mis en évidence 9 irritants majeurs et 18 cas d'utilisation. L'offre de service Platform Engineering doit définir un périmètre clair : ce qui est inclus et comment l'équipe Platform Experience s'articule avec les capability teams existantes.

Cet ADR répond à une question précise : **quels services l'équipe Platform Experience rend-elle, et à quels besoins terrain répondent-ils ?** Il décrit l'offre sous l'angle de la demande (les 18 UC).

Il ne redéfinit **pas** la frontière de responsabilité entre la plateforme et les capability teams : cette frontière — le découpage IN/OUT, les relations `consomme` / `fournit` / `embarque`, et le principe qui les gouverne — est établie par [ADR-002](./adr-002-architecture-fonctionnelle.md). Les deux ADR décrivent le même territoire dans deux projections complémentaires ; la section « Correspondance avec l'architecture fonctionnelle » ci-dessous établit le pont entre les deux.

Les capability teams (KubeApp, IDDA, PDD, IAHS, Observabilité, Réseau) existent déjà et ont chacune leur périmètre. La plateforme ne se substitue pas à elles : elle les rend plus accessibles en les exposant de manière unifiée.

Conformément à ADR-002, l'architecture cible est **multi-mondes** (Kubernetes, VM on-prem, Cloud souverain), rendue possible par le contrat Claim qui découple l'intention du développeur du substrat d'exécution. Le périmètre **initial** décrit ci-dessous se concentre sur le **monde Kubernetes** : il s'agit d'un choix de **phasage** à l'intérieur de cette cible, non d'une limitation de l'architecture (l'extension au monde VM est prévue en Phase 4).

## Décision

L'offre de service s'organise autour de **6 domaines fonctionnels** couvrant les 18 cas d'utilisation identifiés. Ces 6 domaines sont la projection « offre / demande » des 4 briques IN d'ADR-002 (voir la table de correspondance).

### Domaine 1 — Portail développeur & point d'entrée unique

Le portail est le point d'entrée centralisé vers l'ensemble des ressources de la plateforme.

Services proposés :

- Catalogue des services (composants, owners, dépendances, état de santé)
- Documentation centralisée et contextualisée (TechDocs, liée à chaque service)
- Annuaire des équipes et interlocuteurs
- État des services transverses (incidents, maintenances, changements planifiés)
- Feed des changements passés et à venir

Cas d'utilisation couverts : UC1 (point d'entrée unique), UC2 (interlocuteur unique), UC8 (documentation contextualisée), UC17 (feed des changements), UC18 (catalogue de services)

### Domaine 2 — Onboarding & parcours guidés

Services proposés :

- Parcours d'onboarding guidé (du setup de poste au premier déploiement)
- Documentation de démarrage rapide par profil (nouveau dev, dev existant migrant vers Kube, lead technique)
- Liens vers les formations et ressources existantes

Cas d'utilisation couverts : UC3 (onboarding guidé)

### Domaine 3 — Golden Paths & templates

Services proposés :

- Scaffolding via Spring Initializr personnalisé
- Configuration guidée avec validation et pré-remplissage des bonnes pratiques
- Catalogue de templates maintenus et évolutifs (via [Copier](https://copier.readthedocs.io/en/stable/) avec mise à jour native des projets existants)
- Contribution au catalogue par les profils avancés
- CLI de création de projet (template Spring Boot + GitLab + CI/CD + GitOps + Vault + observabilité)

Cas d'utilisation couverts : UC4 (créer un service via template), UC5 (contribuer au catalogue), UC6 (configurer sans erreur)

### Domaine 4 — CI/CD & déploiement

Services proposés :

- Pipelines CI/CD standardisés (GitLab CI templates)
- Déploiement GitOps (via ArgoCD) avec suivi en temps réel
- Visualisation du pipeline (étapes, durées, erreurs claires)
- Intégration des scans de sécurité tôt dans le pipeline (shift-left)
- Feedback rapide et messages d'erreur exploitables

Cas d'utilisation couverts : UC9 (déployer simplement), UC10 (visualiser le pipeline), UC11 (feedback rapide)

Les gates qualité et sécurité (SAST, scan des dépendances et des images, signature) ainsi que le stockage des artefacts signés relèvent de la brique **Fabrique Logicielle** (ADR-002) ; les scans eux-mêmes appliquent des règles définies par les capacités transverses Sécurité / Gouvernance, que la plateforme **outille** sans en être l'autorité.

### Domaine 5 — Environnements & infrastructure self-service

Services proposés :

- Provisionnement d'environnement via UI ou CLI (self-service, sans ticket), exprimé sous forme de **Claim** (contrat d'intention déclaré, cf. ADR-002) : le développeur décrit *ce qu'il veut*, jamais *comment le produire*
- Configuration de ressources courantes (BDD, secrets Vault, clients Keycloak) via des interfaces simplifiées
- Appui sur les outils existants des capability teams (charts Helm, modules Terraform, rôles Ansible) avec une couche d'abstraction : la plateforme **consomme et distribue** ces briques, elle ne les produit pas

Le périmètre initial cible le **monde Kubernetes**. Le routage vers d'autres substrats (VM, Cloud souverain) est porté par la brique **Orchestration self-service** (ADR-002) et activé au fil des phases ; le contrat Claim reste identique quel que soit le substrat.

Cas d'utilisation couverts : UC7 (provisionner un environnement à la demande)

### Domaine 6 — Observabilité & gestion d'incident

Ce domaine porte sur **l'exposition et l'unification** de l'observabilité au service du développeur, dans le portail. La **stack d'observabilité** elle-même (Prometheus, Grafana, Loki, Elastic), ses conventions et ses bibliothèques d'instrumentation relèvent de la capability team Observabilité, positionnée **hors périmètre** en tant que capacité transverse par ADR-002. La plateforme **consomme** cette stack et en restitue une vue cohérente ; elle ne l'opère pas.

Services proposés (par la plateforme) :

- Dashboard unifié par service (logs, métriques, alertes, état des déploiements) — restitution consolidée, alimentée par la stack de la capability team Observabilité
- Alertes pertinentes et filtrées, présentées dans le portail
- Aide au diagnostic automatisé
- Runbooks accessibles et liés au service concerné
- Identification du bon interlocuteur en cas d'escalade (via l'annuaire et le support unique)

Cas d'utilisation couverts : UC12 (santé des services), UC13 (alertes pertinentes), UC14 (diagnostic automatisé), UC15 (trouver le bon contact), UC16 (runbook accessible)

### Frontière de responsabilité (IN / OUT)

La liste de ce qui relève ou non de l'équipe Platform Experience — et surtout le **principe** qui la gouverne (« plus une brique encode une expertise de domaine, plus elle appartient à la capability team correspondante ») — est définie et fait foi dans [ADR-002 — Architecture fonctionnelle DevExperience](./adr-002-architecture-fonctionnelle.md). ADR-001 ne la duplique pas, pour éviter toute divergence entre deux sources.

En synthèse, et **à titre de rappel non normatif** (l'énoncé de référence est celui d'ADR-002) : la plateforme **consomme** les services des capability teams (exploitation Kubernetes, bases de données, identités et secrets, stack d'observabilité, réseau) et les **expose** de manière unifiée et simplifiée, sans se substituer à leur expertise. Pour toute question sur la frontière, se reporter à ADR-002.

### Correspondance avec l'architecture fonctionnelle (ADR-002)

Les 6 domaines de l'offre se projettent sur les 4 briques « dans le périmètre » d'ADR-002 comme suit. Le tableau matérialise qu'il s'agit du même territoire vu sous deux angles (l'offre côté demande ici, le modèle de responsabilité dans ADR-002).

| Domaine (ADR-001, angle offre) | Brique(s) IN (ADR-002, angle architecture) |
|---|---|
| D1 — Portail développeur & point d'entrée unique | Plateforme Expérience développeur (Portail, Catalogue de services, Info changements, Annuaire, Suivi de mes opérations, Support unique) |
| D2 — Onboarding & parcours guidés | Plateforme Expérience développeur (Portail : Découverte + Documentation / TechDocs) |
| D3 — Golden Paths & templates | Plateforme Expérience développeur (Scaffolding) + Self-Service (briques de construction réutilisables, catalogue des outils self-service) |
| D4 — CI/CD & déploiement | Fabrique Logicielle (construction, qualité/signature/sécurité, stockage des artefacts) + Orchestration self-service (déploiement GitOps) |
| D5 — Environnements & infrastructure self-service | Self-Service (Claim / contrat d'intention) + Orchestration self-service (routage, provisionnement, Day-2, cycle de vie) |
| D6 — Observabilité & gestion d'incident | Plateforme Expérience développeur (restitution unifiée, Suivi de mes opérations, Support unique) — en **consommant** la capacité transverse Observabilité (OUT) |

## Conséquences

**Positif :**

- Périmètre clair qui évite les conflits de responsabilité avec les capability teams
- Couverture des 18 UC identifiés lors du constat terrain
- Approche modulaire permettant de livrer domaine par domaine
- Une **seule source autoritative** pour la frontière IN/OUT (ADR-002), ce qui supprime le risque de divergence entre deux documents
- Alignement explicite avec l'architecture cible multi-mondes : le phasage Kubernetes-first n'entre plus en contradiction apparente avec le contrat Claim d'ADR-002

**Négatif :**

- Le périmètre initial ne couvre pas le monde VM (extension prévue en Phase 4)
- La qualité du self-service dépend de la capacité des capability teams à exposer des interfaces standardisées
- Risque de confusion si la frontière IN/OUT n'est pas clairement communiquée aux développeurs — atténué par le renvoi unique à ADR-002 et par le support unique du portail (le développeur n'a pas à connaître ce découpage de l'extérieur)
- Deux documents à maintenir de façon cohérente : toute évolution de la frontière doit se faire dans ADR-002, ADR-001 ne faisant que la refléter

**Lien avec les ADR et documents existants :**

- **Dépend de** [ADR-002 — Architecture fonctionnelle DevExperience](./adr-002-architecture-fonctionnelle.md), qui définit la frontière de responsabilité, le modèle Team Topologies, le contrat Claim et la cible multi-mondes. En cas de divergence sur le périmètre, ADR-002 fait foi.
- Complète l'Annexe 2 (Périmètres des équipes de la platformOrg) en formalisant l'offre de service côté Platform Experience.

## Historique

- **Révision (réconciliation avec ADR-002)** — Suppression de la section « Ce qui n'est PAS inclus » qui redéfinissait la frontière IN/OUT en doublon d'ADR-002 ; remplacée par un renvoi non normatif vers ADR-002. Deux incohérences résolues : (1) l'observabilité, présentée comme un domaine de la plateforme, est recadrée en *exposition/unification* (IN) consommant la stack de la capability team Observabilité (OUT) ; (2) le périmètre Kubernetes-first est reformulé en *phasage* à l'intérieur de la cible multi-mondes d'ADR-002, et non en limitation d'architecture. Ajout d'une table de correspondance 6 domaines ↔ 4 briques IN.
- **Version initiale** — Définition des 6 domaines fonctionnels et couverture des 18 UC.