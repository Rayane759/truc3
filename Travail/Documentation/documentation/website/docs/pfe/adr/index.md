# Architecture Decision Records - Equipe DevExperience

Ce sommaire classe les ADR par **ordre de lecture**, du _pourquoi / quoi_ vers le _comment concret_. Les **numéros restent des identifiants immuables** : ils ne reflètent pas l'ordre de lecture et ne sont pas renumérotés lorsqu'un ADR en référence un autre. Un ADR peut donc dépendre d'un numéro plus élevé — c'est normal.

Quatre regroupements structurent la lecture : **fondations → positionnement → solution technique → mise en œuvre**.

## Fondations — le _quoi_

> Ce que la plateforme doit faire et jusqu'où va sa responsabilité, avant toute question d'organisation ou d'outillage. ADR-001 décrit l'offre vue du développeur et s'y réfère ; ADR-002 fait foi sur la frontière IN/OUT.

| #       | Titre                                                                               | Statut  |
| ------- | ----------------------------------------------------------------------------------- | ------- |
| ADR-001 | [Périmètre fonctionnel de l'offre de service](./adr-001-perimetre-fonctionnel.md)   | Proposé |
| ADR-002 | [Architecture fonctionnelle DevExperience](./adr-002-architecture-fonctionnelle.md) | Proposé |

## 2. Positionnement & organisation — le _qui_

> Qui produit l'offre, selon quel mode de collaboration avec les capability teams, et avec quelle équipe. Le modèle d'insertion (ADR-003) détermine le dimensionnement de l'équipe (ADR-002).

| #       | Titre                                                                                     | Statut  |
| ------- | ----------------------------------------------------------------------------------------- | ------- |
| ADR-003 | [Insertion de l'équipe DevExperience dans le SI existant](./adr-003-insertion-equipe.md)  | Accepté |
| ADR-004 | [Relation équipe DevExpérience vis-à-vis des équipes capabilities](./adr-004-relation.md) | Accepté |
| ADR-014 | [Relation PO DevExpérience vis-à-vis des PO capabilities](./adr-014-relation-po.md)       | Accepté |
| ADR-005 | [Composition et organisation de l'équipe plateforme](./adr-005-organisation-equipe.md)    | Proposé |
| ADR-006 | [Modèle de support : self-service et interlocuteur unique](./adr-006-modele-support.md)   | Proposé |

## 3. Solution technique — la forme et les outils

> Sous quelle forme concrète la plateforme est rendue, et avec quelles briques techniques. Le format (ADR-008) cadre l'architecture applicative (ADR-011), qui elle-même motive le choix de l'IDP (ADR-009).

| #       | Titre                                                                                                     | Statut  |
| ------- | --------------------------------------------------------------------------------------------------------- | ------- |
| ADR-007 | [Architecture applicative DevExperience](./adr-007-architecture-applicative.md)                           | Proposé |
| ADR-008 | [Format de la plateforme : combinaison IDP + GitOps + API/CLI + Libraries](./adr-008-format-plateforme.md) | Proposé |
| ADR-009 | [Choix de Backstage comme IDP](./adr-009-choix-idp.md)                                                    | Proposé |

## 4. Mise en œuvre & pilotage — l'exécution

> Dans quel ordre livrer, comment mesurer le succès et maîtriser les risques. Priorisation et phasage doivent s'accorder avec l'Option C validée par ADR-003 et le démarrage porté par IDDA dès septembre 2026.

| #       | Titre                                                                                                | Statut  |
| ------- | ---------------------------------------------------------------------------------------------------- | ------- |
| ADR-010 | [Stratégie de priorisation : documentation et découvrabilité d'abord](./adr-010-priorisation-doc.md) | Proposé |
| ADR-011 | [Feuille de route et phasage](./adr-011-approche-de-mise-en-œuvre.md)                                | Proposé |
| ADR-012 | [Indicateurs de succès et gouvernance produit](./adr-012-indicateurs-gouvernance.md)                 | Proposé |
| ADR-013 | [Gestion des risques](./adr-013-risques.md)                                                          | Proposé |
