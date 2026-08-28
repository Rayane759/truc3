# ADR-010 - Stratégie de priorisation : documentation et découvrabilité d'abord

| | |
|---|---|
| **Référence** | ADR-010 |
| **Statut** | Proposé : en cours de validation |
| **Auteurs** | Équipe DevExperience |
| **Public** | Équipe DevExperiencee · équipes capabilities · utilisateurs · décideurs SI |

## Contexte

Le constat terrain identifie 9 irritants majeurs. L'irritant n°1 — "ressources difficiles d'accès" — est transverse à tous les profils, tous les SNDI et tous les mondes techniques (Kube et VM).

Verbatims terrain :
- *"La doc ? J'en ai pas trouvé"*
- *"Y a un wiki mais je sais pas où"*
- Documentation dispersée entre wikis, PDF, GitLab Pages, messages Tchap, notes personnelles
- Documentation non maintenue, non référencée, non trouvable

Parallèlement, la démarche Platform Engineering a un enjeu de crédibilité : il faut démontrer rapidement de la valeur pour embarquer les développeurs et les parties prenantes.

**Deux stratégies de priorisation sont possibles :**

1. **Golden Path d'abord** : commencer par l'automatisation de la création de projets Kube (impact fort mais périmètre restreint aux devs Kube, délai de livraison plus long)
2. **Documentation et découvrabilité d'abord** : commencer par le portail, la centralisation de la doc et le catalogue de services (impact large, quick win visible, touche tous les devs)

## Décision

**Nous priorisons la centralisation de la documentation et la découvrabilité (option 2) comme Phase 1 de la feuille de route.**

Le Golden Path Kube devient la Phase 2, en chevauchement avec la fin de la Phase 1.

### Justification

| Critère | Doc & découvrabilité d'abord | Golden Path d'abord |
|---------|------------------------------|---------------------|
| **Population touchée** | Tous les devs (Kube + VM) | Devs Kube uniquement |
| **Irritant adressé** | N°1 — le plus exprimé | N°3 à N°5 |
| **Changement requis côté dev** | Aucun — on rend accessible ce qui existe | Adoption d'un nouvel outil (CLI) |
| **Délai de première valeur** | Court (2-3 mois) | Moyen (4-5 mois) |
| **Effet de crédibilité** | Fort — visible par tous | Modéré — visible par les early adopters |
| **Personas bénéficiaires** | Les 3 personas | Surtout Persona 1 (Consommateur) |
| **Complexité technique** | Moyenne (Backstage + TechDocs) | Élevée (CLI + templates + CI/CD + GitOps) |

### Ce que la Phase 1 "Documentation & Découvrabilité" inclut

- Software Catalog Backstage (composants, owners, dépendances)
- Documentation centralisée via TechDocs (migration des docs de toutes les capability teams)
- Annuaire des équipes et interlocuteurs
- Feed des changements et incidents centralisé
- Parcours d'onboarding documenté pour les nouveaux arrivants
- Moteur de recherche intégré au portail

### Ce que ça ne retarde pas

Le Golden Path Kube démarre en Phase 2 (mois 4) avec un chevauchement sur la fin de la Phase 1. Le travail de fond sur les templates et la CLI peut commencer en parallèle dès la Phase 0. La Phase 1 pose d'ailleurs les fondations nécessaires au Golden Path (Backstage installé, catalogue alimenté, TechDocs en place).

## Conséquences

**Positif :**

- Quick win visible qui touche l'ensemble des 250 développeurs
- Crédibilise la démarche Platform Engineering avant de pousser des outils plus structurants
- Adresse l'irritant le plus fortement exprimé lors du constat terrain
- Pose les fondations techniques (Backstage, TechDocs) nécessaires aux phases suivantes
- Ne nécessite pas de changement d'outillage côté développeur — adoption naturelle

**Négatif :**

- Retarde de ~2 mois la livraison du Golden Path Kube
- La centralisation de la doc nécessite la coopération des capability teams (risque de lenteur)
- Risque de perception "on a juste fait un portail de doc" si la communication n'est pas bien gérée

**Mitigation :**

- Commencer le prototypage du Golden Path dès la Phase 0 pour réduire le décalage
- Impliquer les capability teams dès la Phase 0 dans l'inventaire et la migration de leur documentation
- Communiquer clairement que le portail est la première brique d'une plateforme plus large
