# ADR-014 : Répartition de la relation utilisateur entre le PO DevEx et les POs capability


| | |
|---|---|
| **Référence** | ADR-014 |
| **Statut** | Accepté — cohérent avec l'Option C validée par [ADR-003](./adr-003-insertion-equipe.md) (réunion du 03/07/2026) |
| **Auteurs** | Équipe DevExperience |
| **Public** | ÉquipeDevExperiencee · équipes capabilities |

**Objectif** : Clarifier si — et comment — les POs des capability teams conservent la relation utilisateur dans le modèle intégrateur de la plateforme, et statuer sur la répartition des rôles.

## Contexte

Dans l'organisation cible (modèle **intégrateur**, option C — voir [ADR-003](./adr-003-insertion-equipe.md)), l'équipe **Platform Experience** devient le point d'entrée unique des développeurs, portée par un **PO DevEx**. Les **capability teams** (Compute & Runtime, Identity & Security, Data Services, Reliability & Feedback) exposent leurs services via des API ; l'équipe DevExpérience les assemble et les distribue.

Une **objection revient de façon récurrente** :

> *« Si les développeurs ne parlent plus qu'à la DevEx, les POs capability ne perdent-ils pas le contact avec les utilisateurs ? »*

**Le point de départ est un glissement de sens.** L'objection assimile deux choses distinctes :

- la **relation utilisateur** (comprendre les besoins, les usages, les irritants) ;
- le **traitement de demandes** (répondre à des sollicitations unitaires, souvent sous forme de tickets).

**Constat sur la situation actuelle** : quand un PO capability déclare aujourd'hui être « en contact avec les devs », il traite dans les faits surtout des **tickets**. Ce contact est :

- **réactif** : on n'agit qu'une fois le problème remonté ;
- **transactionnel** : demande → réponse, sans vision d'ensemble ;
- **biaisé** : on n'entend que les utilisateurs qui rencontrent un problème, jamais les usages silencieux ni les non-usages.

Ce n'est pas de la connaissance utilisateur : c'est du **support**. Par ailleurs, la case « mesurer l'adoption » — la vraie mesure de la relation à l'usage — n'est aujourd'hui cochée par presque aucune équipe.

**Ce que le modèle intégrateur retire réellement aux POs capability n'est donc pas la relation utilisateur : c'est la file de demandes unitaires et dispersées.**

## Décision

Nous distinguons explicitement deux flux, gérés différemment :

| Flux | Nature | Responsable |
| --- | --- | --- |
| **Demandes unitaires** | Réactif, transactionnel | Centralisé via le **PO DevEx** (évite la sollicitation dispersée) |
| **Connaissance des usages** | Proactif, qualitatif | **Partagé** entre PO DevEx et POs capability |

**Répartition des rôles** :

- **Le PO DevEx** consolide et priorise les besoins **transverses**, porte la **cohérence d'expérience** et la vision globale. Il n'a **pas le monopole** de la relation utilisateur : il est le point d'entrée des demandes, pas un filtre opaque.
- **Le PO capability** garde la **discovery sur son domaine** : il rencontre les développeurs sur ses sujets, **mesure l'adoption** de ses services, et participe aux **phases de conception** et de co-construction des capabilities.

En résumé, pour chaque PO capability :

| Ce qu'on retire | Ce qu'on préserve | Ce qu'on gagne |
| --- | --- | --- |
| La file de tickets unitaires | Le contact terrain sur son domaine | Un contact **ciblé et approfondi** (discovery, co-conception) |
| Le contact subi et dispersé | La participation aux ateliers de conception | La **mesure d'adoption** de ses API, aujourd'hui absente |

!!!info "Pourquoi l'intégration (C) reste compatible avec la discovery capability"
    Le risque théorique du modèle **intégrateur (C)** est que la DevEx se contente d'assembler des spécifications et que les capability teams deviennent une *feature factory* déconnectée de l'usage. Ce risque est mitigé de deux façons : d'une part le sponsoring DSI dont bénéficie l'équipe DevExpérience (cf. [ADR-004](./adr-004-relation.md)) lui permet d'échanger sur les priorités sans en faire un formalisme lourd ; d'autre part, comme détaillé ci-dessous, les POs capability gardent explicitement la **discovery sur leur domaine** — ils ne sont pas cantonnés en bout de chaîne.

## Conséquences

**Positives** :

- Les POs capability passent d'un contact **subi et réactif** à un contact **choisi et proactif**.
- Fin de la sollicitation dispersée : les capability teams ne sont plus interrompues par des demandes unitaires éparpillées.
- La **mesure d'adoption** devient un attendu explicite du rôle de PO capability — comblant une lacune actuelle.
- Le développeur bénéficie d'un **point d'entrée clair** et d'une expérience unifiée, sans perte de connexion terrain côté capability.

**Négatives / risques** :

- Si le PO DevEx devient un **filtre total**, on retombe dans le « téléphone arabe » : les POs capability se coupent des besoins et la discovery se dégrade.
- La frontière entre « demande unitaire » (→ DevEx) et « besoin de fond » (→ discovery partagée) peut être floue et demander de l'arbitrage.
- Le partage de la relation exige une **discipline de communication** entre POs (rituels communs, restitution des remontées).

!!!warning "Point de vigilance"
    Le risque n'est pas que les POs capability perdent la relation utilisateur, mais que le PO DevEx la **capte entièrement**. Le partage des rôles doit être **explicite et outillé** : rituels de discovery partagés, restitution systématique des besoins remontés, et accès des POs capability aux métriques d'adoption de leurs propres services.

## Alternatives considérées

### 1. Relation utilisateur 100 % via le PO DevEx (filtre total)

Toutes les interactions passent exclusivement par la DevEx ; les POs capability ne parlent plus aux développeurs.

- **Avantage** : point de contact unique parfaitement cohérent.
- **Risque** : téléphone arabe, perte de la connaissance métier fine côté capability, capability teams réduites à une *feature factory*.

!!!info "Décision"
    Non retenue : reproduit le risque même que soulève l'objection.

### 2. Chaque PO capability conserve sa relation directe complète (statu quo)

Les développeurs continuent de solliciter directement chaque PO capability, en plus de la DevEx.

- **Avantage** : aucun changement, contact direct maximal.
- **Risque** : sollicitation dispersée, absence de vision transverse, le développeur reste l'orchestrateur — soit le problème que la plateforme cherche à résoudre.

!!!info "Décision"
    Non retenue : contredit l'objectif de point d'entrée unique.

### 3. Partage explicite des rôles (modèle intégrateur) — **retenue**

Demandes unitaires centralisées via la DevEx ; connaissance des usages partagée, avec discovery de domaine et mesure d'adoption maintenues côté capability.

!!!info "Décision"
    Retenue : préserve la relation à l'usage là où elle a de la valeur, tout en supprimant le contact réactif dispersé.

## Bilan

Les POs des capability teams **ne perdent pas la relation utilisateur — ils perdent la file d'attente de tickets**. Ils passent d'un contact subi et dispersé à un contact choisi et approfondi, et gagnent la mesure d'adoption qui leur manque aujourd'hui. La condition de réussite est un **partage explicite et outillé** de la relation entre PO DevEx et POs capability, pour que la DevEx reste un point d'entrée et non un filtre.