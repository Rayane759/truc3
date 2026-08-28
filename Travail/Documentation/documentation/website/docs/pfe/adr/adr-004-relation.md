# ADR-004 : Relation équipe DevExpérience vis-à-vis des équipes capabilities

| | |
|---|---|
| **Référence** | ADR-004 |
| **Statut** | Accepté — cohérent avec l'Option C validée par [ADR-003](./adr-003-insertion-equipe.md) (réunion du 03/07/2026) |
| **Auteurs** | Équipe DevExperience |
| **Public** | ÉquipeDevExperiencee · équipes capabilities · architectes du SI · décideurs SI |

## Contexte

[ADR-003](./adr-003-insertion-equipe.md) a positionné la Plateforme Expérience Développeur (PFE) comme **équipe intégratrice (Option C)** : elle ne produit pas elle-même les briques techniques de domaine (charts Helm applicatifs, modules Terraform, rôles Ansible, Compositions Crossplane), mais elle **assemble** ce que produisent les équipes capabilities et le **distribue** aux équipes applicatives via un catalogue unique.

« Intégratrice » ne veut pas dire passive. L'équipe DevExpérience est le **principal client** des capability teams pour ce périmètre, et bénéficie à ce titre d'un **fort sponsoring de la DSI** (cf. ADR-003). Elle peut donc légitimement **échanger avec les capability teams sur leur roadmap** — signaler un besoin non couvert, demander qu'une brique évolue ou soit priorisée — sans pour autant piloter ces roadmaps ni imposer un formalisme lourd de contribution.

## Décision

La relation repose sur trois principes simples :

1. **Les capability teams produisent et restent propriétaires de leurs briques** (charts Helm, modules Terraform, rôles Ansible, Compositions Crossplane…), à leur rythme et selon leurs propres priorités.
2. **L'équipe DevExpérience assemble ces briques et les distribue** aux équipes applicatives via le catalogue (Backstage), avec une exigence minimale de bon sens (documentation, un point de contact identifié) plutôt qu'un référentiel de conformité formalisé.
3. **L'équipe DevExpérience peut faire remonter des besoins et des priorités** aux capability teams — via les instances de pilotage déjà existantes (comités produit, échanges PO à PO) — grâce au sponsoring DSI dont elle dispose, sans détenir de pouvoir de décision sur leur roadmap.

Un point de contact identifié côté DevExpérience et un point de contact identifié côté capability team suffisent à faire fonctionner cette relation ; elle sera outillée plus finement (critères d'admission au catalogue, SLO de support) si le besoin s'en fait sentir dans la durée, plutôt que d'être surconçue dès le départ sur un sujet sensible pour l'organisation.

## Conséquences

**Positif :**

- Relation simple à comprendre et à mettre en place dès le démarrage (septembre 2026, porté par IDDA — voir ADR-003)
- Autonomie des capability teams préservée : elles gardent la maîtrise de leur roadmap
- Le sponsoring DSI donne à l'équipe DevExpérience un vrai levier d'influence sans nécessiter de gouvernance lourde
- Effectif Platform Experience soutenable : pas de dispositif de contrôle qualité à opérer en continu

**Négatif :**

- Cohérence du catalogue moins garantie qu'un dispositif de contrôle qualité formalisé ; à surveiller dans le temps
- Le poids réel de l'influence de l'équipe DevExpérience sur les roadmaps capability dépend du maintien effectif du sponsoring DSI
- Si des problèmes de qualité ou de cohérence apparaissent de façon répétée, un formalisme plus poussé (critères d'admission, engagements de support) devra être introduit — à réévaluer avec l'usage plutôt qu'anticipé aujourd'hui

## Alternatives considérées

**Modèle Coopérateur** : l'équipe DevExpérience jouerait un rôle actif et outillé de prescripteur/orchestrateur (roadmap plateforme co-construite formellement, charte de qualité opposable, comité mensuel dédié). *Non retenu à ce stade* : plus lourd à mettre en place et à faire accepter que ce que permet un lancement dès septembre 2026 porté par IDDA (voir ADR-003) ; sujet sensible pour l'organisation à ne pas surformaliser trop tôt.

**Modèle Consommateur (option B)** : L'équipe DevExpérience n'opère que le portail, les capabilities s'exposent en autonomie totale, sans aucune interaction sur les roadmaps. *Rejeté* (cf. ADR-003) : abandonne la promesse de cohérence d'expérience aux développeurs.

**Modèle Autonome (option A)** : L'équipe DevExpérience internalise la production des briques. *Rejeté* (cf. ADR-003) : effectif intenable, dette d'expertise, concurrence avec les capabilities.

**Lien avec les ADR existantes :**

- **S'appuie sur** [ADR-003 — Modèle d'insertion de la plateforme dans le SI](./adr-003-insertion-equipe.md), qui retient l'Option C et le sponsoring DSI associé.
- **Cohérent avec** [ADR-014 — Répartition de la relation utilisateur entre le PO DevEx et les PO capability](./adr-014-relation-po.md).
