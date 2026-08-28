# ADR-012 - Indicateurs de succès et gouvernance produit

| | |
|---|---|
| **Référence** | ADR-012 |
| **Statut** | Proposé : en cours de validation |
| **Auteurs** | Équipe DevExperience |
| **Public** | ÉquipeDevExperiencee · décideurs SI |

## Contexte

Le Platform Engineering est traité comme un **produit, pas un projet**. Cela implique une gouvernance adaptée et des indicateurs de succès mesurables dès le départ.

Le constat terrain et les réflexions préliminaires (Annexe 4) ont identifié des pistes d'indicateurs :

- Nombre de mises en prod via Compas
- Nombre de tickets ouverts pour un nouvel environnement
- Nombre de tickets de run par capability team

Ces indicateurs doivent être complétés par des métriques d'adoption, d'impact et de satisfaction pour piloter le produit de manière complète.

## Décision

### Gouvernance produit

La plateforme est pilotée selon les principes suivants :

- Un **Product Owner** identifié au sein de l'équipe Platform Experience, responsable de la vision et de la priorisation du backlog
- Un **backlog produit** alimenté par trois sources :

  - Les retours utilisateurs (feedback des équipes pilotes, enquêtes, questions récurrentes sur le canal support)
  - Les capability teams (besoins d'intégration, évolutions de leurs services)
  - La stratégie DSI (cloud-first, sécurité, migrations planifiées)

- Des **itérations régulières** (sprints de 2-3 semaines) avec livraison continue
- Une **communauté de contributeurs** : les profils avancés (Persona 2 — Contributeur) peuvent enrichir le catalogue de templates et la documentation. Contribution encadrée par des conventions définies en Phase 0.

### Indicateurs de succès

Les indicateurs sont regroupés en trois catégories et mesurés dès la Phase 1.

#### Métriques d'adoption

| Indicateur | Source | Fréquence |
|------------|--------|-----------|
| Nombre de visites / utilisateurs actifs du portail | Analytics Backstage | Hebdomadaire |
| Nombre de services référencés dans le catalogue | Backstage API | Mensuel |
| Nombre de projets créés via le Golden Path | Backstage Scaffolder | Mensuel |
| Nombre de contributions au catalogue de templates | GitLab | Mensuel |
| Nombre de pages TechDocs consultées | Analytics Backstage | Mensuel |

#### Métriques d'impact

| Indicateur | Source | Fréquence | Cible |
|------------|--------|-----------|-------|
| Temps de création d'un nouveau projet | Mesure manuelle puis automatisée | Par projet | < 15 min (vs jours) |
| Temps d'onboarding d'un nouveau développeur | Enquête | Trimestriel | < 1 jour (vs semaines) |
| Nombre de tickets d'infrastructure ouverts | Ticketing | Mensuel | Tendance ↓ |
| Nombre de mises en production par projet | Compas | Mensuel | Tendance ↑ |
| Nombre de questions "à qui m'adresser" sur Tchap | Estimation manuelle | Trimestriel | Tendance ↓ |

#### Métriques de satisfaction

| Indicateur | Source | Fréquence |
|------------|--------|-----------|
| Score DevExp (enquête récurrente) | Questionnaire | Semestriel |
| Feedback qualitatif des équipes pilotes | Entretiens | Fin de chaque phase |
| Net Promoter Score interne | Questionnaire | Semestriel |

#### Métriques DORA (Phase 4+)

À terme, les métriques DORA permettront de mesurer l'impact sur le delivery :
- Fréquence de déploiement
- Lead time for changes
- Mean time to restore (MTTR)
- Change failure rate

### Principe d'alimentation du backlog par les indicateurs

Chaque question récurrente reçue sur le canal support (≥ 3 occurrences) est transformée en :
- Une page de documentation (TechDocs) si c'est un problème de connaissance
- Une automatisation ou un workflow self-service si c'est un problème d'outillage
- Un runbook si c'est un problème d'incident récurrent

## Conséquences

**Positif :**

- Pilotage factuel du produit dès le départ
- Visibilité sur l'adoption et l'impact pour les parties prenantes et le management
- Boucle de feedback continue entre indicateurs → backlog → livraison

**Négatif :**

- Certains indicateurs nécessitent une instrumentation technique (analytics Backstage, intégration Compas)
- Les métriques de satisfaction sont subjectives et dépendent du taux de réponse aux enquêtes
- Risque de suroptimiser pour les métriques au détriment de la qualité réelle de l'expérience

**Lien avec les ADR existantes :**

- Complète l'Annexe 4 (Réflexions sur les indicateurs)
