# Synthèse des besoins

Ce document se concentre exclusivement sur les **besoins exprimés (ou implicites)** identifiés à partir des interviews et des focus groupes.

## Besoins fondamentaux

### Point d’entrée unique (Developer Portal)

**Description**: Un portail central permettant d’accéder à l’ensemble des ressources nécessaires au développement et à l’exploitation.

**Attentes clés** :

- Accès unifié à :
  - documentation
  - resources concernant mon appli
  - liens vers l'ensemble des briques qui concerne mon appli (s'inspirer de l'application **TheDoors** à Lille ou de https://diffusion.gitlab-pages.insee.fr/plateforme-de-donnees/plateforme-de-donnees-central/pfd-melodi-favoris/)
  - Etat des pipelines CI/CD
  - Etats des environnements 
  - outils
  - contacts / experts
- Navigation simple et intuitive
- Recherche globale

**Valeur**:

- Réduction de la fragmentation
- Gain de temps
- Meilleure visibilité globale


### Self-service généralisé

**Description**: Permettre aux développeurs d’exécuter eux-mêmes les opérations courantes sans dépendre d’un tiers.

**Attentes clés** : 

- Création / duplication d’environnements
- Déploiement d’applications
- Gestion des secrets et tokens
- Provisionnement de ressources (VM, namespaces, bases)

**Valeur**:

- Autonomie accrue
- Réduction des goulots d’étranglement
- Accélération du delivery
- Réduction de la surcharge de certains profils



## Standardisation des pratiques

**Description**: Définir et imposer des conventions communes pour réduire la variabilité entre équipes.

**Attentes clés**:

- Templates CI/CD prêts à l’emploi
- Conventions de versioning et de déploiement
- Workflows standardisés
- Bonnes pratiques intégrées par défaut

**Valeur**:

- Réduction des erreurs
- Onboarding simplifié
- Cohérence globale

## Observabilité unifiée

**Description**: Fournir une vision centralisée et exploitable de l’état des systèmes.

**Attentes clés**:

- Dashboard unique regroupant :
  - pipelines
  - déploiements
  - logs
  - métriques
  - alertes
- Alertes filtrées et pertinentes
- Accès rapide aux diagnostics

**Valeur**:

- Meilleure réactivité en cas d’incident
- Réduction du bruit
- Gain de temps en investigation

## Centralisation de la connaissance

**Description**: Structurer et rendre accessible toute la connaissance technique.

**Attentes clés**:

- Documentation centralisée
- Guides pas-à-pas (how-to)
- Glossaire des concepts
- Documentation versionnée (docs-as-code)

**Valeur**:

- Réduction de la dépendance aux experts
- Onboarding accéléré
- Meilleure diffusion des connaissances

## Support à l’onboarding et à la montée en compétence

**Description**: Faciliter l’apprentissage et la prise en main de l’écosystème technique.

**Attentes clés**:

- Parcours d’onboarding structurés
- Tutoriels intégrés
- Micro-formations (vidéos, labs)
- Mentorat / accompagnement initial

**Valeur**:

- Montée en compétence plus rapide
- Réduction de la charge sur les seniors

## Visibilité organisationnelle et technique

**Description**: Donner une vision claire des systèmes, des responsabilités et des dépendances.

**Attentes clés**:

- Cartographie des services et environnements
- Annuaire des experts (qui fait quoi)
- Statut des services et incidents

**Valeur**:

- Meilleure collaboration
- Réduction des blocages

## Communication centralisée et structurée

**Description**: Unifier les canaux de communication liés à la plateforme et aux opérations.

**Attentes clés**:

- Canal unique pour :
  - incidents
  - changements
  - annonces
- Notifications ciblées
- Historique consultable

**Valeur**:

- Réduction du bruit
- Meilleure diffusion de l’information

## Automatisation des tâches d’infrastructure

**Description**: Abstraire et automatiser les opérations techniques aujourd’hui manuelles.

**Attentes clés**:

- Automatisation du tagging
- Gestion des configurations (YAML, segmentation)
- Provisionnement automatisé

**Valeur**:

- Réduction de la charge cognitive
- Moins d’erreurs humaines

## Amélioration des performances CI/CD

**Description**: Optimiser les pipelines pour réduire les temps de cycle.

**Attentes clés**:

- Réduction du temps de build et déploiement
- Parallélisation des tâches
- Caching des dépendances
- Feedback rapide en cas d’erreur

**Valeur**:

- Accélération du time-to-market
- Meilleure expérience développeur

---

## Synthèse

Les besoins identifiés convergent vers un objectif commun :

> Construire une plateforme **intégrée, self-service et centrée sur l’expérience développeur**

Axes structurants :

1. Centraliser (outils, connaissance, communication)
2. Simplifier (UX, workflows, accès)
3. Automatiser (infra, CI/CD, opérations)
4. Donner de la visibilité (technique et organisationnelle)

!!!info Remarque sur la notion de "besoins"

    Tous les besoins listés ici sont considérés comme **structurants** pour la plateforme. 

    Cependant, on peut les distinguer implicitement en deux catégories :

    ### Besoins cœur (indispensables)
    - Point d’entrée unique (Developer Portal)
    - Self-service
    - Standardisation
    - Observabilité unifiée

    👉 Sans ces éléments, la plateforme ne remplit pas son rôle principal.

    ### Besoins d’accélération (différenciants)
    - Onboarding et formation
    - Communication centralisée
    - Annuaire / visibilité organisationnelle
    - Automatisation avancée

    👉 Ils améliorent fortement l’expérience, mais peuvent être déployés progressivement. Voir dans la partie roadmap 😊