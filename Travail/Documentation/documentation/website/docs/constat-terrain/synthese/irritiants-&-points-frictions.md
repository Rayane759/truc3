# Synthèses des irritants & points de frictions 

L'analyse des interviews et des focus groupes met en évidence plusieurs points de frictions/irritans structurant impactant l'expérience du développeur. Les points suivants les résument par ordre de priorité

## Ressources difficile d'accès

La visibilité et la découvrabilité des ressources mise à disposition/partagées par les équipes est jugées difficile. Les ressources sont souvent:

- dispersées
- non référencées
- non maintenue

Cela se traduit par:

- Une non lecture de certaines documentations
- Une difficulté pour coordonner certaines opérations entre équipes de développements

## Des outils non adaptés a l'utilisateurs

Les outils mise à disposition par les équipes de productions sont souvent:

- jugés trop lent
- non pensés avec une bonne UX experience (documentation inadapté)
- outils trop complexe
- souvent encore trop proche de l'Ops

Cela se traduit par:

- Une non utilisation de certains outils
- Une dépendances au profil de sachant pour la réalisation de tâches complexe
- Un vocabulaire non maitrisé

**Illustrations issues des ateliers :**

> "snapshot, chart, label, CVE c'est du « chinois »"

## Complexité des opérations de production et besoin de montée en compétence

Les opérations liées à la production nécessitent une compréhension approfondie des outils et des processus (CI/CD, déploiement, infrastructure). Ces connaissances comme présentées dans le point précédent ne sont détenus que par une faible partie des agents.

Les développeurs expriment un besoin important de pouvoir réaliser ces opérations sans formation. Actuellement les outils proposés sont trop proche de l'Ops et nécéssitent trop de connaissances dans leur utilisation/ordonnancement. Ils souhaitent quand même avoir le temps à un moment de se former dessus.

Cela traduit :

- une complexité élevée des outils et des workflows
- un manque de lisibilité des processus
- une difficulté à monter en compétence de manière autonome

Ce fonctionnement entraîne :

- une dépendance aux profils expérimentés
- un ralentissement des opérations
- une hétérogénéité des pratiques

**Illustrations issues des ateliers :**

> “Je fais du copié collé"

## Dépendance à des experts pour les opérations de production

Les opérations liées à la production (déploiement, configuration, exploitation, mise en place de l'automatisation) reposent fortement sur un nombre limité de profils expérimentés que ce soit cotés devs ou coté exploitant.

Les développeurs moins expérimentés ne disposent pas :

- d’une compréhension claire des outils, processus, ni même de la frontière de la production
- d’une autonomie suffisante pour réaliser certaines opérations
- de supports leur permettant de monter en compétence rapidement

Même des développeurs expérimentés reconnaissent s'appuyer sur des personnes pour certaines tâches d'exploitation complexe (comme la création de Base de données)

Cela se traduit par :

- des sollicitations fréquentes des experts (personne faisant office de référent local ou directement coté Ops)
- des ralentissements dans les cycles de delivery
- une concentration du savoir critique

**Illustrations issues des ateliers :**

> “Je demande à un sachant”  
> “Je demande à Anatole”

## Manque de coordination et de prise en charge des évolutions transverses

Les équipes de développement rencontrent des difficultés à suivre et intégrer les évolutions portées par les équipes transverses (infrastructure, production, sécurité).

Ces changements sont :
- introduits sans vision consolidée
- communiqués via de multiples canaux
- peu intégrés dans les cycles de développement

Les développeurs ne disposent pas d’une visibilité claire sur :
- les évolutions à venir
- leur périmètre d’impact
- leur niveau de priorité

Cela se traduit par :

- une accumulation de migrations à réaliser
- des sollicitations multiples et peu synchronisées
- une difficulté à intégrer ces travaux dans les backlogs
- des ajustements de dernière minute
- une désynchronisation entre roadmap produit et contraintes techniques

Les équipes expriment également une perte de lisibilité et un désengagement vis-à-vis de certains canaux jugés peu exploitables.

**Illustrations issues des ateliers**

> “Les incidents ça arrive, mais communiquez.”

## Répartition des responsabilités inadaptée

Les évolutions transverses sont portées par les équipes de production, mais leur mise en œuvre repose majoritairement sur les équipes produit.

Ces changements :

- sont imposés de manière globale
- nécessitent des adaptations locales
- ne sont pas accompagnés de mécanismes facilitant leur adoption
- ne sont pas compris par les développeurs

Cela entraîne :

- une charge supplémentaire non planifiée
- des reworks
- une adoption hétérogène

**Illustrations issues des ateliers**

> “On veut bien participer aux tâches, mais prenez en compte nos backlogs.”

## Manque de fiabilité des services transverses

Les services mutualisés (CI/CD, infrastructure, sécurité, observabilité, service transverses (SPOC / MajSQL) etc.) sont perçus comme instables ou peu fiables.

Cela entraîne :

- des interruptions ou ralentissements dans les pipelines
- une perte de confiance dans les outils communs
- une surcharge ou une mauvaise utilisation de certains outils
- des contournements ou solutions locales (tests global sur le poste plutot sur les plateformes de recettes)

Ce manque de fiabilité augmente la complexité globale du système.

**Illustrations issues des ateliers :**

> "les runners sont lents, j'ai pas envie de les utiliser"
> "si un service de prod tombe, après j'implémente ma solution je vous fais plus confiance"

## Complexité et manque de lisibilité des pipelines de déploiement

Les pipelines de build et de déploiement sont perçus comme longs et complexes.

Le processus actuel (construction d’image, livraison, promotion entre environnements) est jugé :

- plus lent que les pratiques précédentes
- difficile à comprendre pour les équipes
- peu transparent dans son fonctionnement

Les développeurs expriment notamment :

- un manque de visibilité sur les étapes exécutées
- une difficulté à diagnostiquer les problèmes
- une perception d’opacité lors des déploiements en production

Cela se traduit par :

- une frustration vis-à-vis des outils de delivery
- une perte de confiance dans les pipelines
- une comparaison défavorable avec des pratiques plus simples mais moins robustes (ex : déploiement manuel)

**Illustrations issues des ateliers :**

> "pourquoi c'est lent ? pourquoi ca plante ? Ok c'est cassé mais dit le moi !"

## Intégration de la sécurité génératrice de frictions dans le cycle de delivery

Les mécanismes de sécurité intégrés dans les pipelines (scans, contrôles, validations) sont perçus comme ralentissant significativement les cycles de développement.

Ces contrôles :

- interviennent parfois tardivement dans le pipeline
- génèrent des blocages difficiles à comprendre ou à corriger
- allongent les temps de déploiements

Cela se traduit par :

- une dégradation de l’expérience développeur
- des cycles de delivery plus longs
- une perception de la sécurité comme contrainte plutôt que comme facilitateur

**Illustrations issues des ateliers :**

> "Avant c'était plus rapide"







