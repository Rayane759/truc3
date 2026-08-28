# Feuille de route — Platform Engineering à l'Insee

**Un phasage progressif, du quick win à la maturité continue.**

**Statut** : Cadrage organisationnel validé ([ADR-003](./../pfe/adr/adr-003-insertion-equipe.md)) — le phasage détaillé ci-dessous (quoi livrer, dans quel ordre, avec quels critères de sortie) est en cours de confirmation avec l'équipe IDDA.
**Dernière mise à jour** : Août 2026

> L'approche de mise en œuvre (itérative vs Big Bang) est documentée dans [ADR-011](./../pfe/adr/adr-011-approche-de-mise-en-œuvre.md).
> La priorisation de la Phase 1 (documentation d'abord) est documentée dans [ADR-010](./../pfe/adr/adr-010-priorisation-doc.md).
> Le détail des indicateurs et de la gouvernance produit est posé dans [ADR-012](./../pfe/adr/adr-012-indicateurs-gouvernance.md).
> Le Mois 1 de la Phase 0 correspond au démarrage réel en **septembre 2026**, porté par l'équipe IDDA (voir [ADR-003](./../pfe/adr/adr-003-insertion-equipe.md)).

---

## Où on en est

- **✅ Diagnostic** : 9 irritants majeurs, 3 personas, 18 cas d'utilisation identifiés sur le terrain.
- **✅ Offre & organisation** : Option C validée, démarrage porté par IDDA dès septembre 2026.
- **✅ POC** : Backstage et Crossplane expérimentés et retenus.

Reste à valider : **dans quel ordre on livre**.

## Ce que cette feuille de route ne fait pas

Elle ne revient pas sur le **cadrage organisationnel** ([ADR-003](./../pfe/adr/adr-003-insertion-equipe.md), déjà validé) : équipe, positionnement vis-à-vis des capability teams, démarrage IDDA. Elle ne porte que sur le **phasage** — quoi livrer, dans quel ordre, avec quels critères de sortie.

**Principe directeur** : approche **itérative**, pas Big Bang. Chaque phase livre de la valeur mesurable avant d'attaquer la suivante.

---

## Vue d'ensemble

Cinq phases, du quick win à l'amélioration continue.

![](./assets/roadmap.png)

| Phase | Promesse | En bref |
|-------|----------|---------|
| **0** | Fondations | Équipe, backlog, état des lieux |
| **1** | Portail & doc | Quick win, tous les devs |
| **2** | Golden Path Kube | MVP de bout en bout |
| **3** | Self-service | Industrialisation |
| **4** | Maturité | Amélioration continue |

---

## Phase 0 — Fondations (Mois 1-2, sept.–oct. 2026)

**Objectif** : Poser les bases organisationnelles et techniques avant de livrer de la valeur.

- **Organisationnel** : une équipe DevExperience montée en compétence, un backlog défini, des équipes pilotes engagées et un canal de retour utilisateur en place.
- **Technique** : une vision claire de la documentation existante à intégrer, un premier Backstage accessible pour commencer à construire dessus.

### Découpage en US techniques

| Priorité | User story |
|----------|------------|
| **Forte** | Installer Backstage (vanilla) en environnement de dev |
| **Forte** | Cartographier la documentation existante nécessaire aux développeurs, équipe par équipe |
| **Forte** | Définir le backlog initial de l'équipe DevExperience |
| **Moyenne** | Identifier et engager 2-3 équipes pilotes volontaires |
| **Moyenne** | Mettre en place un forum utilisateur (retours développeurs) |
| **Moyenne** | Identifier les besoins de formations / accompagnement |

### Critères de sortie

- Équipe constituée et opérationnelle
- Backstage accessible en environnement de dev
- Équipes pilotes identifiées et engagées
- Cartographie de la documentation existante réalisée
- Le contact avec les prestataires a été réalisé

---

## Phase 1 — Portail, doc & découvrabilité (Mois 2-5)

Quick win — tous les devs, tous les SNDI.

**Objectif** : Résoudre l'irritant n°1 du constat terrain : documentation dispersée et syndrome « Martine ».

- **Trouver le bon service et son propriétaire en un clic** : catalogue centralisé de tous les composants
- **Ne plus chercher la doc au bon endroit** : documentation des capability teams centralisée et à jour
- **Savoir qui contacter, sans deviner** : annuaire des équipes et interlocuteurs
- **Voir ce qui a changé ou va changer** : feed des changements et incidents
- **Trouver l'info en cherchant, pas en naviguant** : moteur de recherche intégré

**BONUS** : un parcours d'onboarding pour prendre en main l'outil.

### Découpage en US techniques

| Priorité | User story |
|----------|------------|
| **Forte** | Déployer Backstage en production |
| **Forte** | Déployer le Software Catalog Backstage (composants, owners, dépendances) |
| **Forte** | Migrer la documentation des capability teams vers TechDocs (docs-as-code) |
| **Forte** | Développer l'annuaire des équipes et interlocuteurs |
| **Forte** | Documenter l'utilisation pour les différents utilisateurs |
| **Moyenne** | Documenter les choix d'architecture et d'implémentation (Homologation) |
| **Moyenne** | Mettre en place le feed des changements et incidents |
| **Moyenne** | Identifier un moteur de recherche pour le portail (solution interne backstage / externe / IA) |
| **Moyenne** | Déployer le moteur de recherche pour le portail |
| **Moyenne** | Collaborer avec l'urbanisation afin d'identifier le rôle de Backstage par rapport à Oscar |
| **Moyenne** | Initier l'intégration des briques des développeurs dans le catalogue |
| **Bonus** | Construire le parcours d'onboarding |

### Critères de sortie

- Portail accessible à tous les devs, tous SNDI
- Documentation d'au moins **80 %** des capability teams intégrée dans TechDocs
- Au moins **50 %** des services/outils (de la prod) référencés dans le catalogue
- Trafic portail en croissance mois sur mois
- Réduction mesurable des questions « à qui je m'adresse ? » sur Tchap
- Demo de la solution en DevOpsAcc + des démos d'avancements régulières
- Un dossier d'archi est initialisé et complété
- Les équipes pilotes ont intégré une grande part de leur service dans le catalogue

---

## Phase 2 — Premier Golden Path Spring Boot sur Kubernetes (Mois 4-7)

Chevauche la fin de la Phase 1.

**Objectif** : Livrer un premier parcours standardisé de bout en bout pour les applications Spring Boot sur Kubernetes.

- **Créer un service Spring Boot en quelques clics** : repo, pipeline et déploiement générés automatiquement, sans partir d'une page blanche
- **Obtenir son infrastructure sans ticket** : client Keycloak, policy Vault, bucket… disponibles en self-service, brique par brique
- **Trouver et comprendre le Golden Path sans aide extérieure** : parcours et documentation découvrables directement depuis le portail

### Découpage en US techniques

| Priorité | User story |
|----------|------------|
| **Forte** | Scaffolder un service Spring Boot (repo + pipeline CI/CD) depuis Backstage |
| **Forte** | Déployer automatiquement le service généré sur l'environnement Kube (GitOps) |
| **Forte** | Demander un client Keycloak via une Claim Crossplane |
| **Forte** | Demander une policy Vault via une Claim Crossplane |
| **Forte** | Demander un bucket via une Claim Crossplane |
| **Moyenne** | Documenter le Golden Path dans TechDocs, référencé dans le catalogue |
| **Moyenne** | Standardiser le pipeline avec des Components CI (To Be Continuous) |
| **Moyenne** | Documenter comment intégrer le Golden Path si j'ai déjà une application existante |

### Critères de sortie

- Au moins **3 projets créés** via le Golden Path par les équipes pilotes
- Feedback collecté et intégré dans le backlog
- Temps de création d'un nouveau projet **< 15 minutes** (vs jours actuellement)

---

## Phase 3 — Self-service, observabilité & industrialisation (Mois 6-10)

**Objectif** : Étendre le self-service, intégrer l'observabilité, généraliser au-delà des équipes pilotes.

- **Self-service** : provisionner un environnement sans ticket, être protégé par défaut, ne plus être seul face à un incident.
- **Observabilité** : voir la santé de son service en un coup d'œil, être alerté seulement quand c'est pertinent.

Axes portés par cette phase :

- **Proposer d'autres Golden Paths** : capitaliser sur les outils mis en place pour le premier Golden Path afin d'en proposer d'autres (React / Python)
- **Profiter des évolutions du Golden Path sans tout refaire** : mise à jour des templates propagée automatiquement
- **Consommer les capability teams sans changer d'outil** : intégration étendue (PDD, IAHS, Observabilité)
- **Contribuer, pas seulement consommer** : catalogue ouvert aux équipes avancées

### Découpage en US techniques

| Priorité | User story |
|----------|------------|
| **Forte** | Provisionner un environnement via UI (ou as code), sans ticket |
| **Forte** | Étudier les mécanismes de sécurité à intégrer dans le pipeline |
| **Forte** | Construire le dashboard de santé des services (plugins ArgoCD et Elastic, intégration aux outils analyzer…) |
| **Moyenne** | Générer des alertes pertinentes et filtrées |
| **Moyenne** | Intégrer des runbooks et une aide au diagnostic dans le portail |
| **Moyenne** | Propager les mises à jour de template aux projets existants (`copier update`) |
| **Moyenne** | Étendre l'intégration aux capability teams PDD, IAHS, Observabilité |
| **Faible** | Ouvrir la contribution au catalogue de templates |

### Critères de sortie

- Adoption mesurable **au-delà** des équipes pilotes
- Réduction mesurable du nombre de tickets d'infrastructure
- Satisfaction développeur en hausse (enquête DevExp)

---

## Phase 4 — Maturité & évolution continue (Mois 10+)

Sans fin définie.

### Axes d'évolution

- **Extension au monde Cloud et VM** (selon résultats du questionnaire cloud prévu juin 2026)
- **Automatisation avancée** : assembler l'ensemble des claims as a service en une macro claim (par exemple `SpringBootApp`)
- **Intégration IA** : aide au diagnostic, suggestion de résolution
- **Métriques DORA** : fréquence de déploiement, lead time, MTTR, taux d'échec
- **Contribution communautaire active** (inner source)

> La plateforme est un **produit**, pas un projet : cette phase n'a pas vocation à se terminer.

---

## Piloter la trajectoire

Comment on mesure qu'on avance :

- **📈 Adoption** : visites portail, services catalogués, projets créés via Golden Path
- **🎯 Impact** : temps de création de projet, temps d'onboarding, tickets d'infra, questions « à qui m'adresser »
- **😊 Satisfaction** : score DevExp, feedback qualitatif des pilotes, NPS interne

Le détail des indicateurs et de la gouvernance produit est posé dans [ADR-012](./../pfe/adr/adr-012-indicateurs-gouvernance.md).

---

# En résumé :

<embed src="../autres/presentations/assets/roadmap/index.pdf" type="application/pdf" width="100%" height="600px" />
