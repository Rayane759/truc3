# Modèle opérationnel

<embed src="./../../autres/presentations/assets/offre-et-organisation/index.pdf" type="application/pdf" width="100%" height="600px" />

## Organisation cible

L'organisation s'inspire du modèle Team Topologies avec une **équipe DevExperience** centrale qui s'appuie sur les **capability teams** existantes.

**Composition équipe DevExperience (6 personnes dans la littérature) :**

- Profils Dev — développement du portail, des templates, de la CLI, de l'UX développeur
- Profils Ops — intégration avec les outils existants (Kube, ArgoCD, Vault, GitLab CI), automatisation infra
- Profils DevOps — Golden Paths, pipelines standardisés, GitOps, pont entre dev et ops

Le nombre de profils sera déterminé au fur et à mesure que le service DevExperience verra son offre enrichie.

**Capability teams (existantes) :**

- KubeApp / Runtime — Kubernetes, GitOps, ingress, scaling
- PDD / Data Services — BDD as code, S3, accès
- IAHS / Security — OIDC, secrets, IAM
- Observabilité — Stack monitoring, alerting, supervision
- Réseau — Exposition, certificats
- STD — Standards et socle technique

Chaque capability team contribue avec ses modules/templates dans les outils de la Platform Experience. L'équipe DevExperience assemble les briques et est responsable de leur intégration dans le portail et les Golden Paths.

## Démarrage : IDDA, septembre 2026

La cible reste un service DevExpérience dédié (PO et roadmap propres). En attendant que cette mise en place soit effective, le démarrage est porté dès **septembre 2026** par l'équipe **IDDA** : un nouveau service DevExpérience est créé dans la roue de la prod, avec une roadmap co-construite par le CPO et les deux PO d'IDDA (voir [ADR-003](./adr/adr-003-insertion-equipe.md)).

Il est important de garder à l'esprit trois natures différentes, souvent confondues : **IDDA** est une équipe (qui héberge temporairement les ressources DevExpérience, en gardant son propre backlog IDDA) ; le **Service DevExpérience** est un produit (la couche expérience + intégration, distincte du backlog IDDA) ; la **Plateforme** est l'offre finale vue du développeur (le service DevExpérience *plus* toutes les capabilities distribuées à travers lui).

## Modèle d'interaction

L'équipe DevExperience devient le **point d'entrée principal** pour les développeurs :

1. **Self-service d'abord** : la plateforme doit être suffisamment bien conçue pour que les développeurs trouvent et fassent ce dont ils ont besoin en autonomie (portail, CLI, templates, documentation).

2. **Interlocuteur unique en fallback** : quand le self-service ne suffit pas, un canal unique (Tchap dédié + ticketing) permet de poser des questions. L'équipe DevExperience qualifie le besoin et redirige si nécessaire vers la bonne capability team.

3. **Les capability teams exposent leurs capacités via des interfaces standardisées** (APIs, Infrastructure as Code, services automatisés) consommées par la plateforme.

L'objectif est de passer de l'organigramme actuel (250 devs → Anatole) à un modèle structuré (devs → plateforme self-service → équipe DevExperience → capability teams).

### Gouvernance produit

La plateforme est traitée comme un **produit, pas un projet**. Cela implique :

- Un **Product Owner** identifié au sein de l'équipe DevExperience
- Un **backlog produit** alimenté par les retours utilisateurs, les capability teams et la stratégie DSI
- Des **itérations régulières** (sprints de 2-3 semaines) avec livraison continue
- Des **métriques d'adoption et de satisfaction** suivies dès le début (voir section 5)
- Une **communauté de contributeurs** : les profils avancés (Persona 2 — Contributeur) peuvent enrichir le catalogue de templates et la documentation

