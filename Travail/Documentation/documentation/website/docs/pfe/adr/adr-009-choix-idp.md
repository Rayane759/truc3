# ADR-009 - Choix de Backstage comme IDP

| | |
|---|---|
| **Référence** | ADR-009 |
| **Statut** | Proposé : en cours de validation |
| **Auteurs** | Équipe DevExperience |
| **Public** | Équipe DevExperiencee · équipes capabilities · architectes du SI · utilisateurs |

## Contexte

L'[ADR-008](./adr-008-format-plateforme.md) a établi qu'un Internal Developer Platform (IDP) constituera l'interface principale de la plateforme, en complément de GitOps, API/CLI et Libraries. Il reste à choisir l'outil concret qui matérialisera cet IDP.

Le marché des IDP est en pleine structuration. Plusieurs solutions existent, avec des positionnements et des modèles économiques différents.

### Cartographie du marché (analyse interne)

L'analyse du paysage des IDP, formalisée lors de la phase de cadrage, positionne les principaux acteurs selon deux axes (capacité d'exécution / vision produit) :

| Quadrant | Acteurs |
|----------|---------|
| **Leaders** | Backstage, GitLab |
| **Challengers** | Microsoft DevBox, AWS Proton |
| **Visionaries** | Port, Harness |
| **Niche Players** | Pulumi |

### Contraintes spécifiques à l'Insee

Le contexte de l'Insee impose plusieurs contraintes :

- **Souveraineté et hébergement** : les outils doivent pouvoir être hébergés sur l'infrastructure on-premise de l'Insee (pas de SaaS pour les données sensibles)
- **Open source** : préférence forte du secteur public pour les solutions open source, pour des raisons de transparence, de pérennité et de coût
- **Pas de vendor lock-in** : éviter les dépendances fortes à un éditeur ou un cloud provider
- **Compatibilité avec l'existant** : GitLab self-hosted, ArgoCD, Helm, Vault, Kubernetes — l'IDP doit s'intégrer sans rupture
- **Coût maîtrisé** : pas de licences récurrentes proportionnelles au nombre d'utilisateurs (250 développeurs)
- **Adaptabilité** : pouvoir adapter l'outil aux spécificités Insee (composants custom, intégrations maison)

## Options envisagées

### Option A — Backstage (Leader)

Plateforme open source créée par Spotify, projet diplômé de la CNCF.

**Avantages** :
- 100% open source (Apache 2.0), pas de coût de licence
- Self-hosted, contrôle total sur les données
- Écosystème de plugins très riche (ArgoCD, Grafana, GitLab, Kubernetes, Vault…)
- CNCF Graduated → maturité reconnue, gouvernance ouverte, communauté active
- Adopté par de grandes organisations (Spotify, Expedia, Netflix, American Airlines, EDF…)
- Pas de vendor lock-in
- Extensible : possibilité de développer des plugins custom pour les besoins Insee

**Inconvénients** :
- Construction nécessite des compétences front (React/TypeScript) et back (Node.js)
- Maintenance à la charge de l'équipe Platform Experience
- Pas de support commercial inclus (mais offres tierces existent : Roadie, Spotify Portal)
- Courbe d'apprentissage initiale

### Option B — GitLab (Leader)

GitLab propose des fonctionnalités s'apparentant à un IDP (catalogue de projets, CI/CD, déploiements).

**Avantages** :
- Déjà déployé à l'Insee
- Pas d'outil supplémentaire à maintenir
- Intégration native avec le CI/CD existant

**Inconvénients** :
- Couverture IDP partielle : pas de Software Catalog complet, pas de TechDocs unifiés, pas de Scaffolder équivalent
- Scope produit centré sur le CI/CD, pas sur l'expérience développeur globale
- Pas de système de plugins extensible comparable à Backstage
- Ne couvre pas certains UC clés (catalogue de services avec dépendances, dashboards transverses, annuaire d'équipes)

### Option C — Port (Visionary)

IDP SaaS commercial avec une approche no-code.

**Avantages** :
- Mise en place rapide
- UX moderne
- Pas de développement à faire

**Inconvénients** :
- **SaaS uniquement** → incompatible avec les contraintes de souveraineté
- Modèle commercial avec licences par utilisateur → coût élevé pour 250 devs
- Vendor lock-in (modèle de données propriétaire)
- Dépendance à la roadmap d'un éditeur externe

### Option D — Harness (Visionary)

Plateforme commerciale CI/CD + IDP.

**Avantages** :
- Suite intégrée (CI, CD, IDP, Feature Flags…)
- Support commercial

**Inconvénients** :
- Commercial → coût élevé
- SaaS principal (option self-hosted limitée)
- Vendor lock-in
- Doublon fonctionnel avec GitLab CI déjà en place

### Option E — Microsoft DevBox / AWS Proton (Challengers)

Solutions IDP des hyperscalers.

**Inconvénients rédhibitoires** :
- Liées au cloud provider correspondant (Azure / AWS)
- Pas adaptées à un contexte on-premise
- Vendor lock-in cloud

### Option F — Pulumi (Niche Player)

Plus une solution d'Infrastructure as Code qu'un IDP complet.

**Inconvénients** :
- Périmètre fonctionnel trop limité (pas de portail, pas de catalogue, pas de docs)
- Ne couvre pas les besoins de l'ADR-001

## Décision

Nous retenons **Backstage** comme IDP de la plateforme Insee.

### Justification synthétique

| Critère Insee | Backstage | GitLab | Port | Harness | DevBox/Proton | Pulumi |
|--------------|-----------|--------|------|---------|---------------|--------|
| Open source | ✅ | ⚠️ (Community Ed.) | ❌ | ❌ | ❌ | ⚠️ |
| Self-hosted | ✅ | ✅ | ❌ | ⚠️ | ❌ | ✅ |
| Couverture IDP complète | ✅ | ❌ | ✅ | ✅ | ⚠️ | ❌ |
| Pas de coût de licence | ✅ | ⚠️ | ❌ | ❌ | ❌ | ⚠️ |
| Pas de vendor lock-in | ✅ | ⚠️ | ❌ | ❌ | ❌ | ⚠️ |
| Compatible cloud / on-prem | ✅ | ✅ | ❌ | ⚠️ | ❌ | ✅ |
| Écosystème plugins | ✅ | ❌ | ⚠️ | ⚠️ | ❌ | ❌ |
| Adapté secteur public | ✅ | ✅ | ❌ | ❌ | ❌ | ⚠️ |

Backstage est la seule solution qui coche toutes les cases dans le contexte Insee.

### Ce que Backstage permet de couvrir

- **Software Catalog** → catalogue des services, owners, dépendances (UC16)
- **TechDocs** → documentation centralisée et contextualisée (UC8)
- **Scaffolder** → Golden Paths via templates (UC4, UC5, UC6)
- **Plugins** : ArgoCD (état des déploiements), Grafana (observabilité), GitLab (CI/CD), Kubernetes (état des pods), Vault (secrets) → UC9, UC10, UC12

### Composant custom envisagé

Un type de composant `gitops-repo` sera développé pour représenter les repos apps-of-apps ArgoCD, avec une tab dédiée surfaçant les infos ArgoCD/GitOps et une extraction automatique depuis les `values.yaml`. Cette extension illustre l'intérêt du modèle de plugins Backstage.

## Conséquences

**Positif :**

- Solution open source alignée avec les valeurs et contraintes du secteur public
- Pas de coût de licence, scaling indépendant du nombre d'utilisateurs
- Couverture fonctionnelle complète des UC identifiés
- Écosystème de plugins riche → intégration native avec l'existant Insee (GitLab, ArgoCD, Vault)
- Communauté CNCF active → pérennité et évolutions assurées
- Possibilité de contribuer en retour à la communauté (cf. politique open source de l'État)

**Négatif :**

- Compétences front (React/TypeScript) et back (Node.js) nécessaires dans l'équipe Platform Experience
- Maintenance et évolutions à la charge de l'équipe (vs solution clé en main)
- Configuration initiale plus longue qu'une solution SaaS
- Pas de support commercial direct (mitigation : recours possible à des prestataires comme Roadie ou Spotify Portal en cas de besoin ponctuel)

**Mitigations :**

- Compétences front/back déjà identifiées dans la composition d'équipe (ADR-005 : 2 profils Dev)
- Démarrage avec une installation standard, personnalisation progressive selon les besoins
- Documentation officielle Backstage très fournie + communauté active sur Discord / GitHub

**Lien avec les ADR existantes :**

- Concrétise la brique IDP de l'[ADR-008](./adr-008-format-plateforme.md)
- Permet de matérialiser le périmètre fonctionnel de l'[ADR-001](./adr-001-perimetre-fonctionnel.md)
- Cohérent avec les compétences de l'équipe définies dans l'[ADR-005](./adr-005-organisation-equipe.md)
