# ADR-011 - Approche de mise en œuvre : itérative et phasée

| | |
|---|---|
| **Référence** | ADR-011 |
| **Statut** | Proposé : en cours de validation |
| **Auteurs** | Équipe DevExperience |
| **Public** | Équipe DevExperiencee · décideurs SI |

## Contexte

La mise en place du Platform Engineering à l'Insee nécessite de choisir une stratégie de mise en œuvre. Deux grandes approches s'opposent :

1. **Big Bang** : livrer l'ensemble des fonctionnalités en une seule fois, après une longue phase de construction
2. **Itérative et phasée** : livrer de la valeur progressivement, phase par phase, avec chevauchement

L'équipe Platform Experience sera composée de 6 personnes. Il n'y a pas de contrainte de date imposée. Le risque de perte de soutien managérial ou d'adoption insuffisante est réel si la valeur n'est pas visible rapidement.

## Options envisagées

### Option A — Big Bang

Construire l'ensemble de la plateforme (portail + Golden Path + self-service + observabilité) avant de la livrer.

**Avantages** : livraison cohérente et complète, pas de demi-mesure.

**Inconvénients** : délai avant la première valeur visible (6-12 mois), risque de construire à côté des besoins réels, pas de feedback intermédiaire, risque fort de perte de soutien.

### Option B — Itérative et phasée ✅ (retenue)

Découper la mise en œuvre en phases progressives avec chevauchement, chaque phase livrant un résultat utilisable indépendamment.

**Avantages** : valeur visible rapidement, feedback continu, ajustement possible à chaque phase, crédibilité construite progressivement.

**Inconvénients** : nécessite une priorisation rigoureuse, certaines phases peuvent sembler incomplètes prises isolément.

## Décision

Nous retenons l'**option B — approche itérative et phasée**, structurée en 4 phases progressives avec chevauchement :

- **Phase 0 — Fondations** : organisation, outillage, équipes pilotes
- **Phase 1 — Portail, documentation & découvrabilité** : quick win, touche tous les devs (voir ADR-004)
- **Phase 2 — MVP Golden Path Kube** : premier parcours standardisé de bout en bout
- **Phase 3 — Self-service, observabilité & industrialisation** : extension et généralisation
- **Phase 4 — Maturité & évolution continue** : produit pérenne, métriques DORA, extension VM

Chaque phase produit un livrable utilisable indépendamment et s'appuie sur les fondations de la phase précédente. Le chevauchement entre phases est intentionnel pour maximiser le débit de l'équipe.

Le détail opérationnel (livrables, critères de sortie, planning indicatif) est documenté dans la [Roadmap](./../../roadmap/index.md).

## Conséquences

**Positif :**

- Première valeur visible dès le mois 3-4
- Boucle de feedback continue → le produit est ajusté au fil des phases
- Risque d'adoption réduit : chaque phase prouve la valeur avant la suivante
- Compatible avec la capacité de l'équipe (6 personnes)

**Négatif :**

- Nécessite une priorisation rigoureuse pour éviter la dispersion
- Le chevauchement des phases exige une bonne coordination au sein de l'équipe
- Les durées indicatives dépendent de la constitution complète de l'équipe dès la Phase 0
