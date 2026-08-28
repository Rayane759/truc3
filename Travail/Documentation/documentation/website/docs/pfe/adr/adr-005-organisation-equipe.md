# ADR-005 - Composition et organisation de l'équipe plateforme

| | |
|---|---|
| **Référence** | ADR-005 |
| **Statut** | Proposé : en cours de validation |
| **Auteurs** | Équipe DevExperience |
| **Public** | Équipe DevExperience ·  décideurs SI |

## Contexte

Le constat terrain montre que les développeurs sont aujourd'hui leur propre orchestrateur : ils identifient eux-mêmes les équipes à contacter, coordonnent les demandes entre capability teams, et s'appuient sur quelques sachants pour débloquer les situations complexes. La disparition des RIAPs a amplifié ce phénomène.

La mise en place d'une équipe Platform Experience nécessite de définir sa composition, son dimensionnement et son articulation avec les capability teams existantes (KubeApp, PDD, IAHS, Observabilité, Réseau, STD).

L'évaluation de la maturité Team Topologies des équipes existantes montre des niveaux hétérogènes en termes d'API, de self-service et de mesure d'adoption.

## Décision

### Composition de l'équipe Platform Experience

L'équipe est composée de **6 personnes** avec trois profils complémentaires :

**2 profils Dev :**

- Développement du portail (Backstage), des templates, de la CLI
- UX développeur et intégration front
- Maintien du catalogue de composants et de la documentation TechDocs

**2 profils Ops :**

- Intégration avec les outils existants (Kubernetes, ArgoCD, Vault, GitLab CI, Nexus)
- Automatisation des workflows d'infrastructure
- Liaison technique avec les capability teams

**2 profils DevOps :**

- Conception et maintenance des Golden Paths
- Pipelines CI/CD standardisés
- GitOps et déploiement continu
- Pont entre les besoins dev et les contraintes ops

### Articulation avec les capability teams

L'équipe Platform Experience ne remplace pas les capability teams. Elle s'en nourrit :

- Chaque capability team **contribue** avec ses modules, templates et documentation dans les outils de la Platform Experience
- L'équipe Platform Experience **assemble** les briques et est responsable de leur intégration dans le portail et les Golden Paths
- La consommation des capabilities par la plateforme n'est pas obligatoire pour le développeur

**Capability teams concernées :**

| Équipe | Périmètre | Maturité self-service |
|--------|-----------|----------------------|
| KubeApp / Runtime | Kubernetes, GitOps, ingress, scaling | ✅ Self-service existant |
| IDDA | Infrastructure VM, déploiement applicatif | ✅ API + self-service |
| PDD / Data Services | BDD as code, S3, accès données | ⏳ Via IDDA principalement |
| IAHS / Security | OIDC, secrets Vault, IAM | ⏳ Tickets encore fréquents |
| Observabilité | Stack monitoring, alerting, supervision | ❌ Tickets |
| Réseau | Exposition, certificats | — |
| STD | Standards et socle technique | — |

### Modèle de montée en puissance

La stratégie consiste à commencer par les capability teams les plus matures (KubeApp, IDDA) et progressivement intégrer les autres à mesure qu'elles exposent des interfaces standardisées.

## Conséquences

**Positif :**

- Équipe pluridisciplinaire capable de couvrir le portail, les Golden Paths et l'intégration infra
- Pas de rupture avec l'organisation existante : les capability teams conservent leur périmètre
- Taille d'équipe réaliste pour un démarrage (6 personnes)

**Négatif :**

- 6 personnes pour 250 devs implique une forte dépendance au self-service et à la contribution communautaire
- L'intégration avec les capability teams les moins matures (Observabilité, IAHS) prendra du temps
- Besoin de trouver les bons profils (le DevOps reste une espèce rare, comme observé lors du constat terrain)

**Lien avec les ADR existantes :**

- S'appuie sur l'ADR 001 (Périmètre fonctionnel de l'équipe) et l'ADR 003 (Modèle d'insertion de la plateforme dans le SI (positionnement vis-à-vis des capability teams))
