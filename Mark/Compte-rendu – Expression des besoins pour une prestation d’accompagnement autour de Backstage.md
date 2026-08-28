# Compte-rendu – Expression des besoins pour une prestation d’accompagnement autour de Backstage

## Contexte

Dans le cadre de la démarche de **Platform Engineering**, plusieurs irritants ont été identifiés côté développeurs :

- augmentation de la charge cognitive ;
- multiplication et dispersion des outils ;
- difficulté d’accès à la documentation ;
- manque de self-service ;
- faible centralisation des informations techniques et opérationnelles.

L'ensemble des élèments irritants / personnas / cas d'utilisation a déjà été récupéré/aggrégé/concilié dans un documents préalable

L’objectif est de remettre l’**expérience développeur** au centre via une plateforme unifiée permettant (par ordre de priorité décroissante):

- la centralisation de la documentation et des outils;
- la centralisation de la communication descendante équipe prod -> dev  
- la mise à disposition de services self-service.
- l’accès simplifié aux outils;
- la standardisation des pratiques;

Dans ce contexte, la solution **Backstage** a été étudiée et validée comme socle potentiel d’Internal Developer Platform (IDP).


## Solution envisagée : Backstage

### Pourquoi Backstage

Backstage a été identifié comme une solution pertinente car il répond aux principaux besoins exprimés :

- outil open source ;
- fortement utilisé dans l’écosystème Platform Engineering ;
- extensible via plugins ;
- compatible avec une approche self-hosted ;
- intégration native avec GitLab, Kubernetes, documentation technique, APIs, CI/CD ;
- capacité de créer des workflows de génération de templates et de golden paths.

Les alternatives étudiées présentent plusieurs limitations :

| Solution | Limites identifiées |
|---|---|
| Pulumi | Pas de portail/catalogue/documentation complète |
| AWS Proton / Microsoft DevBox | Trop orientés cloud provider |
| Port / Harness | Solutions payantes ou SaaS |
| GitLab seul | Ne couvre pas les besoins de centralisation/documentation/golden paths |

Backstage apparaît aujourd’hui comme la solution la plus alignée avec les besoins identifiés.

## Besoins d’accompagnement identifiés

Deux besoins d’accompagnement ont été identifiés au cours de la discussion :

- un besoin d’accompagnement par un expert Platform Engineering afin de favoriser la montée en compétences de l’équipe et d’accompagner les choix structurants autour de Backstage et des autres briques qui viendront constituer l'offre plateform engineering (crossplane peut être ???);
- un besoin d’accompagnement orienté UX Design / développement frontend afin de rendre l’interface Backstage plus moderne, plus ergonomique et plus attractive pour les utilisateurs.

### Accompagnement expert / montée en compétence

#### Accompagnement architecture et structuration

##### Besoins

- comprendre l’architecture Backstage ;
- définir les bonnes pratiques de développement avec Backstage ;
- installer et configurer des plugins ;
- créer et structurer des plugins ;
- concevoir des golden paths dans les règles de l’art ;
- implémenter une gestion des droits ;
- définir des patterns d’intégration avec les outils existants ;
- structurer la gouvernance de la plateforme.
- Accompagner/Conseiller dans le choix des briques qui pourrait venir s'ajouter à la démarche platform engineering (crossplane / kratix, copier, ...)

Le besoin porte davantage sur :

- l’architecture ;
- l’intégration ;
- la gouvernance ;

que sur de simples formations “clic bouton” centrées sur l’utilisation basique de l’outil.

#### Montée en compétences techniques

##### Sujets ciblés

- fonctionnement interne de Backstage ;
- architecture frontend/backend ;
- système de plugins ;
- développement et extension ;
- intégration GitLab/Kubernetes/OIDC.

##### Compétences ciblées

- React (à confirmer selon les besoins de personnalisation UI) ;
- Node.js ;
- développement de plugins Backstage ;
- gestion des permissions ;
- scaffolder/templates.

#### Accompagnement dans la durée

Le besoin exprimé est un accompagnement :

- progressif ;
- orienté expertise ;
- avec suivi dans le temps ;
- permettant d’éviter les mauvaises orientations techniques ;
- aidant à conserver une vision globale de la plateforme.

L’objectif est d’avoir :

- un expert produit ;
- un accompagnement architecture ;
- un support sur les choix structurants.

### Accompagnement UX Design / Frontend

#### Concevoir une interface moderne

Le besoin exprimé est une prestation permettant de fournir :

- des maquettes d’écrans ;
- une réflexion UX/UI ;
- une organisation plus moderne des informations affichées dans Backstage ;
- une interface plus ergonomique et plus attractive pour les utilisateurs.

L’objectif est de transformer Backstage en une plateforme donnant réellement envie d’être utilisée au quotidien.

#### Implémentation des maquettes d’écran

Le besoin exprimé est de disposer d’un développeur frontend (expert CSS / JavaScript / React) capable :

- d’implémenter les maquettes conçues ;
- de personnaliser l’interface Backstage ;
- d’améliorer l’expérience utilisateur globale ;
- de maintenir une cohérence graphique sur l’ensemble de la plateforme.

## Organisation envisagée

### Temporalité

Consensus exprimé :

- éviter un démarrage immédiat en septembre (donner du temps à la nouvelle équipe de prendre ses marques) => eventuellement juste une présentation du fonctionnement de l'outil en septembre mais pas plus ;
- privilégier un démarrage de prestation vers octobre ;
- laisser le temps à l’équipe de se structurer.

## Modalités souhaitées

Souhait d’avoir :

- implication des futurs mainteneurs (PO IDDA + Future PO IDDA) dès les échanges avec le potentiel prestataire ;
