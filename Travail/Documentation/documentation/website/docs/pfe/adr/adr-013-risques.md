# ADR-013 - Gestion des risques

| | |
|---|---|
| **Référence** | ADR-013 |
| **Statut** | Proposé : en cours de validation |
| **Auteurs** | Équipe DevExperience |
| **Public** | Équipe DevExperience · décideurs SI |

## Contexte

La mise en place d'une plateforme interne dans une organisation de la taille de l'Insee (250 développeurs, 4 SNDI, multiples capability teams) comporte des risques organisationnels, techniques et humains qu'il convient d'identifier et de mitiger dès le départ.

Ces risques sont issus de l'analyse du constat terrain, des ADR existantes et des retours d'expérience du Platform Engineering dans d'autres organisations.

## Décision

Nous identifions **7 risques majeurs** avec leurs stratégies de mitigation.

### Risque 1 — Résistance au changement

**Description** : Les développeurs n'adoptent pas la plateforme, par habitude, méfiance ou manque de temps.

**Probabilité** : Moyenne — **Impact** : Fort

**Mitigation** :
- Approche progressive avec équipes pilotes volontaires (pas d'imposition)
- Co-construction avec les développeurs (la plateforme est faite AVEC eux, pas POUR eux)
- Quick win visible dès la Phase 1 (portail + doc) pour démontrer la valeur avant de demander un changement d'habitude
- Communication régulière auprès des SNDI (présentations, retours d'expérience des pilotes)
- La plateforme reste un facilitateur, pas une obligation

### Risque 2 — Surcharge de l'équipe plateforme

**Description** : 6 personnes pour 250 développeurs → l'équipe devient un goulet d'étranglement ou s'épuise.

**Probabilité** : Élevée — **Impact** : Fort

**Mitigation** :
- Self-service comme priorité absolue : chaque interaction humaine évitable doit être automatisée ou documentée
- Contribution communautaire : les profils Contributeur (Persona 2) enrichissent les templates et la doc
- Priorisation stricte du backlog : on ne fait pas tout, on fait ce qui a le plus d'impact
- Règle des 3 occurrences : toute question posée 3 fois devient de la doc ou de l'automatisation
- Pas de support L1 permanent : le canal Tchap n'est pas un help desk 24/7
- En misant sur la standardisation et automatisation on pourrait récupérer des personnes dans d'autres équipes pour faire grossir l'équipe plateforme.

### Risque 3 — Dépendance aux capability teams

**Description** : Une ou plusieurs capability teams ne jouent pas le jeu (pas de doc, pas d'API, pas de contribution), ce qui bloque l'intégration dans la plateforme.

**Probabilité** : Moyenne — **Impact** : Moyen

**Mitigation** :
- Commencer par les teams les plus matures (KubeApp, IDDA) pour construire un modèle de réussite
- Impliquer les capability teams dès la Phase 0 (inventaire doc, conventions de contribution)
- Rendre la contribution la plus simple possible (docs-as-code dans leur propre repo)
- Montrer la valeur pour la capability team elle-même (moins de questions récurrentes, meilleure visibilité de leur offre)

### Risque 4 — Effet "outil de plus"

**Description** : La plateforme est perçue comme un outil supplémentaire qui s'ajoute au paysage existant au lieu de le simplifier.

**Probabilité** : Moyenne — **Impact** : Fort

**Mitigation** :
- Chaque ajout doit retirer de la complexité : si le portail ne remplace pas un workflow existant, il ne sert à rien
- Unifier plutôt qu'empiler : le portail agrège ce qui existe, il ne crée pas une couche de plus
- Mesurer la perception utilisateur (enquête DevExp) et ajuster
- Communication claire sur ce que la plateforme remplace (pas "un outil de plus" mais "un seul outil au lieu de 47")

### Risque 5 — Qualité et maintenance des templates

**Description** : Les Golden Path templates deviennent obsolètes, créant de la dette technique au lieu d'en réduire.

**Probabilité** : Moyenne — **Impact** : Moyen

**Mitigation** :
- Copier comme outil de templating avec mise à jour native des projets existants (`copier update`)
- Ownership clair : chaque template a un mainteneur identifié
- Revue communautaire avant publication
- Tests automatisés sur les templates (le template génère un projet qui build et passe les tests)
- Versionnement et changelog des templates

### Risque 6 — Perte de soutien managérial

**Description** : Le projet perd son sponsor ou sa priorité face à d'autres urgences.

**Probabilité** : Faible — **Impact** : Très fort

**Mitigation** :
- Métriques visibles dès la Phase 1 (adoption, trafic portail, satisfaction)
- Quick wins pour démontrer la valeur concrète rapidement
- Alignement avec la stratégie DSI (cloud-first, DevOps, sécurité)
- Implication des parties prenantes dans la gouvernance produit (revues de fin de phase)

### Risque 7 — Perception "on a juste fait un portail de doc"

**Description** : En commençant par la documentation (Phase 1), la démarche est perçue comme limitée à "un site de doc de plus".

**Probabilité** : Moyenne — **Impact** : Moyen

**Mitigation** :
- Communiquer clairement que le portail est la première brique d'une plateforme plus large (montrer la roadmap complète)
- Inclure dès la Phase 1 des éléments différenciants (catalogue de services avec owners et dépendances, feed des changements, annuaire — pas juste de la doc)
- Prototyper le Golden Path en parallèle (Phase 0) pour montrer la suite
- Présenter les résultats de la Phase 1 avec les métriques d'impact, pas juste les livrables

### Risque 8 — Limiter les fonctionnalités proposées car on veut intégrer le monde VM

**Description** : Le monde VM peut ne pas s'intégrer dans tout les outils qui existe dans le monde du platform engineering. En particulier dans des outils qui pourrait fournir une interface uniforme peut importe le type de déploiement. Ceci pour des contraintes de sécurité imposée par le SIA. Cependant ces outils pourrait être utile pour le monde Kube et le monde Cloud.

**Probabilité** : moyenne — **Impact** : fort


**Mitigation** :
- Définir clairement la cible souhaité pour le platform engineering et s'assurer qu'elle est partagée par tous (hiérarchie, PO, équipe service)
