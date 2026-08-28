# ADR-003 - Modèle d'insertion de la plateforme dans le SI (positionnement vis-à-vis des capability teams)


| | |
|---|---|
| **Référence** | ADR-003 |
| **Statut** | Accepté — Option C validée en réunion de suivi du 03/07/2026 |
| **Auteurs** | Équipe DevExperience |
| **Public** | ÉquipeDevExperiencee · équipes capabilities · architectes du SI · décideurs SI |

> Cet ADR dépend d'[ADR-002 — Architecture fonctionnelle DevExperience](./adr-002-architecture-fonctionnelle.md) (qui fixe la frontière IN/OUT) et complète [ADR-001 — Périmètre fonctionnel de l'offre de service](./adr-001-perimetre-fonctionnel.md) (qui décrit l'offre).

## Statut

Accepté. L'Option C a été validée en réunion de suivi (03/07/2026) ; le démarrage opérationnel, porté par l'équipe IDDA, est acté pour septembre 2026 (voir « Insertion dans l'organisation » ci-dessous).

## Contexte

Le périmètre fonctionnel de la plateforme est établi par ailleurs : ADR-001 et ADR-002 définissent les 7 blocs fonctionnels (4 dans le périmètre — Expérience développeur, Self-Service, Fabrique logicielle, Orchestration self-service ; 3 hors périmètre — briques transverses, capacités transverses, substrats d'exécution) ainsi que la frontière de responsabilité. ADR-001 en décrit l'offre de service côté demande.

Cet ADR répond à une **autre** question, de nature organisationnelle : **comment l'équipe Platform Experience (DevExperience) se positionne-t-elle vis-à-vis des capability teams existantes pour produire cette offre ?** Autrement dit, qui produit quoi, et selon quel mode de collaboration.

Éléments de contexte du SI Insee :

- ~250 développeurs, 12 équipes de service en production
- 2 mondes d'exécution (VM, Kubernetes), bientôt 3 (Cloud souverain)
- 6 ans d'adoption DevOps à homogénéiser sans recentraliser
- Frictions mesurées : de l'ordre de 10 tickets minimum pour obtenir une nouvelle plateforme, ~12 jours en moyenne entre le code et le déploiement d'une nouvelle application
- Irritants : hétérogénéité des connaissances et des pratiques entre individus / équipes / SNDI, complexité des trois mondes portée par chaque équipe, faible découvrabilité et dépendance aux personnes

Les capability teams disposent déjà d'un haut niveau d'expertise sur leur domaine de responsabilité. Le choix de positionnement détermine directement la taille de l'équipe Platform Experience, sa pérennité, et la dynamique politique (partenaire ou concurrent) avec les capability teams. C'est donc une décision structurante, qui relève du modèle Team Topologies.

## Options envisagées

Trois positionnements ont été évalués, du plus autonome au plus intégré.

### Option A — Plateforme indépendante (autonome)

L'équipe DevExperience **produit elle-même** la majorité des briques et réimplémente pour ses utilisateurs. Elle internalise les expertises de domaine.

- **Avantages** : time-to-market initial rapide (et encore, incertain), cohérence forte (un seul propriétaire), décisions techniques rapides, interlocuteur unique.
- **Inconvénients** : risque de « SI dans le SI » (coût et maintenance en hausse), effectif intenable à terme, dette d'expertise inévitable, mise en concurrence avec les capability teams.

### Option B — Plateforme produit + capability teams (consommatrice)

L'équipe DevExperience fournit le portail ; les capability teams **intègrent en autonomie** leur service dans le portail. Modèle de type « marketplace interne » — comparable à un Rundeck DevOps, avec une interface plus soignée.

- **Avantages** : effectif plateforme minimal, autonomie maximale des capability teams, pas de goulot d'étranglement plateforme.
- **Inconvénients** : cohérence d'expérience fragile, industrialisation dispersée, plateforme sans levier sur les standards, maturité élevée requise chez chaque capability team, pas de vision globale.

### Option C — Plateforme produit (intégratrice) + capability teams

L'équipe DevExperience **assemble et distribue** ce que produisent les capability teams. Elle devient leur **principal client** et bénéficie d'un **fort sponsoring** de la DSI.

- **Avantages** : effectif soutenable, expertises des capability teams valorisées, cohérence sans concurrence, évolutivité naturelle, cohérence de l'offre hors plateforme, amélioration de l'offre des capability teams.
- **Inconvénients** : coordination inter-équipes, démarrage plus lent, maturité minimale requise, responsabilité distribuée, les bonnes pratiques poussées par l'équipe DevExperience peuvent ne pas être intégrées dans les équipes capabilities, nécessite un fort sponsoring de la DSI.

### Comparaison synthétique

| Critère | A — Autonome | B — Consommatrice | C — Intégratrice |
|---|---|---|---|
| Effectif plateforme | 🔴 Élevé | 🟢 Faible | 🟡 Modéré |
| Time-to-market initial | 🟢 Rapide | 🟡 Modéré | 🟡 Modéré |
| Pérennité 3-5 ans | 🔴 Faible | 🟢 Élevée | 🟡 Modérée |
| Cohérence d'expérience | 🟢 Forte | 🔴 Variable | 🟢 Forte |
| Valorisation capability teams | 🔴 Faible | 🟢 Élevée | 🟢 Élevée |
| Risque politique | 🔴 Élevé | 🟡 Modéré | 🟡 Modéré |
| Maturité requise du SI | 🟢 Faible | 🔴 Élevée | 🟡 Modérée |
| Cohérence hors plateforme | ⚫ N/A | 🔴 Faible | 🟢 Élevée (si fort sponsoring) |
| Montée en maturité des capability teams | 🔴 Aucune | 🟡 Indirecte | 🟢 Forte (si fort sponsoring) |

### Couverture fonctionnelle par option

| Option | Couverture des blocs fonctionnels | Qualification |
|---|---|---|
| A — Autonome | Tout, mais rien de fiable | 4 domaines réimplémentés, doublons fragiles |
| B — Consommatrice | Ce que les équipes veulent bien exposer | Couverture partielle, conditionnelle à leur maturité |
| C — Intégratrice | Une offre cohérente, assemblée | 4 capacités intégrées, soutenable |

La couverture disqualifie A et B — reste C. Le vrai choix n'est pas technique mais stratégique : **quelle promesse fonctionnelle l'Insee veut tenir vis-à-vis de ses 250 développeurs**, et à quel coût organisationnel soutenable.

### Grille d'arbitrage

Trois questions discriminent les options :

1. **Maturité des capability teams ?** Moyenne/faible → A ou C ; élevée → B.
2. **Effectif plateforme à 2 ans ?** < 5 → B ; 5-10 → C ; > 10 → A envisageable.
3. **Culture de coopération ?** Faible → A ; forte → B ou C.

Les fourchettes d'effectif sont des ordres de grandeur indicatifs, à confirmer selon le périmètre réellement staffé.

## Décision

L'**Option C — Intégratrice** est retenue et **validée** comme positionnement de l'équipe Platform Experience.

Justification :

- **Continuité culturelle** — l'option C prolonge 6 ans de démarche DevOps : industrialiser et rendre cohérent, plutôt que tout recentraliser.
- **Soutenabilité** — effectif à taille humaine et expertises Insee existantes valorisées plutôt que réinternalisées (l'option A conduit à un effectif intenable, l'option B à une cohérence fragile).
- **Modèle éprouvé** — cohérent avec Team Topologies et les références CNCF de Platform Engineering, et avec ce qui se pratique ailleurs.

Le vrai objet du choix n'est pas technique mais stratégique : **quelle promesse fonctionnelle l'Insee veut tenir vis-à-vis de ses 250 développeurs**, et à quel coût organisationnel soutenable.

## Insertion dans l'organisation

### Trois périmètres, trois natures

La confusion la plus fréquente vient d'une comparaison de choses qui ne sont pas de même nature. Trois objets distincts sont en jeu :

| Objet | Nature | Question | En une phrase |
|---|---|---|---|
| **IDDA** | une **équipe** (org) | **QUI ?** | Une équipe existante qui héberge temporairement les ressources DevExpérience — tout en gardant son propre produit (service IDDA) / backlog |
| **Service DevExpérience** | un **produit** (responsabilité) | **QUOI ?** | La couche expérience + intégration : portail, self-service, fabrique, orchestration. Le *canal*. N'inclut **pas** l'expertise de domaine |
| **Plateforme** | une **offre** (vue du dev) | **RÉSULTAT ?** | Tout ce que le développeur consomme : la couche DevExpérience **+** toutes les capabilities distribuées |

IDDA = une **équipe** · DevExpérience = un **produit** · Plateforme = ce que le dev **obtient au bout**.

Deux pièges à éviter :

- **IDDA ≠ DevExpérience** — mêmes personnes en septembre 2026, mais **deux backlogs distincts**. Appartenir à IDDA (l'équipe) ne dit rien du périmètre du produit qu'on porte.
- **DevExpérience ≠ Plateforme** — DevExpérience **assemble et distribue** ; la plateforme est plus large, elle inclut tout ce que les capability teams exposent à travers elle. On **distribue** l'expertise, on ne la **possède** pas (cf. Option C ci-dessus).

### Démarrage : septembre 2026, porté par IDDA

La cible reste un service dédié : **1 nouveau service** avec sa **roadmap** et son **PO** dédiés, et des **ressources** propres pour le réaliser (option A d'insertion dans la roue de la prod). Mais ce modèle est difficile à mettre en place dès septembre 2026 : l'identification du PO, la construction de la roadmap et l'identification des ressources prennent du temps, et en septembre la roadmap **KubeApp** est d'abord ajoutée à la roadmap IDDA.

En septembre 2026, le démarrage est donc pragmatique et porté par IDDA :

- **Création d'un nouveau service** dans la roue de la prod
- **Création d'une roadmap DevExpérience** par le CPO et les deux PO d'IDDA
- **Travail collaboratif des deux PO** pour organiser les priorités de l'équipe IDDA
- **Réalisation des priorités** au sein de l'équipe IDDA

L'organisation des équipes sur le long terme sera instruite dans un second temps, par la hiérarchie, en collaboration avec les agents. Il est demandé à IDDA et aux PO de bien mettre en avant, dans les communications aux utilisateurs, que le périmètre / backlog du produit DevExpérience est **bien distinct** de celui d'IDDA.

## Conséquences

**Positif :**

- Équipe Platform Experience dimensionnée à taille humaine et pérenne sur 3-5 ans, sans avoir à recruter des experts dans tous les domaines techniques
- Les capability teams disposent d'un **canal de distribution** de leur expertise plutôt que d'une concurrente, ce qui aligne les intérêts et réduit le risque politique
- Cohérence de l'expérience développeur préservée (contrairement à l'option B seule)
- Démarrage rapide dès septembre 2026 en s'appuyant sur une équipe existante (IDDA) pendant que l'organisation cible se construit

**Négatif :**

- Coût de coordination inter-équipes récurrent
- Démarrage plus lent que les options autonomes
- Nécessite une maturité minimale des capability teams et un fort sponsoring de la DSI pour tenir la cohérence hors plateforme
- Responsabilité distribuée : la frontière de responsabilité (définie par ADR-002) doit rester claire et communiquée
- Risque de confusion entre le périmètre IDDA (équipe) et le périmètre DevExpérience (produit) pendant la phase de démarrage — à traiter explicitement dans la communication (voir « Trois périmètres, trois natures »)

**Points de vigilance / décisions liées :**

- **Composition de l'équipe** — voir [ADR-005](./adr-005-organisation-equipe.md) (environ 6 personnes : 2 profils Dev, 2 profils Ops, 2 profils DevOps).
- **Organisation cible au-delà de septembre 2026** — à instruire par la hiérarchie, en collaboration avec les agents.

**Lien avec les ADR existantes :**

- **Dépend d'**[ADR-002 — Architecture fonctionnelle DevExperience](./adr-002-architecture-fonctionnelle.md) : la frontière IN/OUT qu'il définit est la condition de sens des options (une plateforme « canal de distribution » suppose que les briques transverses restent chez les capability teams).
- **Complète** [ADR-001 — Périmètre fonctionnel de l'offre de service](./adr-001-perimetre-fonctionnel.md) : ADR-001 dit *quoi*, cet ADR dit *avec qui et comment* l'offre est produite.
- **Cadre** [ADR-004 — Relation équipe DevExpérience vis-à-vis des équipes capabilities](./adr-004-relation.md) et [ADR-014 — Répartition de la relation utilisateur entre le PO DevEx et les PO capability](./adr-014-relation-po.md), qui détaillent la mécanique du modèle Intégrateur retenu ici.
