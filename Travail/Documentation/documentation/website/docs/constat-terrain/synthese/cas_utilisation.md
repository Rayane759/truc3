# Cas d’utilisation – Platform Engineering

Ce document présente un ensemble de **cas d’utilisation** devant être couvert par la démarche plateform-engineering, construits à partir des irritants et besoins identifiés lors des interviews.
Au sein de chaque partie les UseCases (UC) sont classés du plus prioritaire au moins prioritaire.

Ces cas d’utilisation permettent de structurer une plateforme :

- orientée autonomie
- centrée sur l’expérience développeur 
- réduisant la friction

La plateforme devient ainsi un **produit interne au service des équipes**.

## 🟦 Onboarding & découverte

### UC1 – Accéder à un point d’entrée unique

**Consommateur :** Tous  
**Objectif :** Avoir une vue d'ensemble sur l’écosystème

**Scénario :**

- Accès à un portail unique
- Visualisation des services, outils et docs

**Irritants adressés :**

- Documentation dispersée  
- Multiplicité des outils  

**Valeur :**

- Gain de temps
- Meilleure visibilité

### UC2 – Accéder à un interlocuteur unique

**Consommateur :** Tous  
**Objectif :** Avoir une réponse rapidement peu importe l’écosystème. Avoir une seule communication à suivre.

**Scénario :**

- Je contacte l'équipe pour un Besoin d'un nouveau service qui n'est pas dans le catalogue. Soit l'équipe reprends mon besoin soit elle me redirige vers l'équipe qui gère cette partie.

**Irritants adressés :**

- Multiplicité des canaux
- Non prise en compte des jalons de développement dans les changements demandés par les équipes de la prod

**Valeur :**

- Gain de temps
- Meilleure visibilité

### UC3 – Parcours d’onboarding guidé

**Consommateur :**  Développeur “consommateur de plateforme”  
**Objectif :** Être autonome rapidement

**Scénario :**

- Parcours guidé (setup du poste, création de dépôt avec standard insee, déploiement selon les bonnes pratiques, monitoring)

**Irritants adressés :**

- Dépendance aux seniors  

**Valeur :**

- Réduction du time-to-productivity

## 🟩 Création & standardisation

### UC4 – Créer un nouveau service via template

**Consommateur :** Développeur “consommateur de plateforme” (même si on espère tous)  
**Objectif :** Démarrer rapidement

**Scénario :**

- Création via template
- Génération automatique (repo, CI/CD, config)

**Irritants adressés :**

- Manque de standard  
- Complexité initiale  
- Dépendances aux experts

**Valeur :**

- Démarrage rapide
- Cohérence

### UC5 – Contribuer au catalogue de service

**Consommateur :** Développeur “avancé / contributeur plateforme” ou Lead technique
**Objectif :** S'assurer que les services proposés reste à l'état de l'art et des pratiques actuelles.

**Scénario :**

- Contribution aux templates
- Contribution aux configs de bonnes pratiques

**Irritants adressés :**

- Ne pas savoir si le copié collé qu'on fait introduit de la dette technique

**Valeur :**

- Benefice pour tout ceux qui utilise le UC4

### UC6 – Configurer un service sans erreur

**Consommateur :** Développeur “consommateur de plateforme”  
**Objectif :** Configurer un service sans expertise spécifique

**Scénario :**

- Le dev créé ou modifie un service
- la plateforme:
    
    - pré-remplit les bonnes pratiques de configurations
    - applique les conventions
    - valide avant le déploiement

**Irritants adressés :**

- Perte de temps à débugger des erreurs liés à des fichiers yaml

**Valeur :**

- limites les process manuels
- Eviter d'oublier des choses parce qu'on a "mal lu la doc"


## 🟨 Développement & environnement

### UC7 – Provisionner un environnement à la demande

**Consommateur :** Tous  
**Objectif :** Tester en autonomie dans un environnement proche de l'environnement final.

**Scénario :**

- Création d’environnement via UI

**Irritants adressés :**

- Dépendance aux experts  

**Valeur :**

- Autonomie
- Gain de temps

### UC8 – Accéder à une documentation contextualisée

**Consommateur :** Développeur “consommateur de plateforme”  
**Objectif :** Comprendre rapidement le fonctionnement des ouils sans avoir à chercher la doc.

**Scénario :**

- Accès à la doc depuis le contexte (service, pipeline)

**Valeur :**

- Amélioration de la lecture de la documentation car cette dernière est réellement adaptée et centrée sur ce que j'utilise.


## 🟧 CI/CD & déploiement

### UC9 – Déployer une application simplement

**Consommateur :** Développeur “consommateur de plateforme” (même si on espère tous)   
**Objectif :** Déployer rapidement

**Scénario :**

- Déploiement via UI avec suivi temps réel

**Irritants adressés :**

- Pipelines complexes  

**Valeur :**

- Accélération du delivery

### UC10 – Visualiser un pipeline

**Consommateur :** Développeur “consommateur de plateforme”    
**Objectif :** Comprendre le pipeline

**Scénario :**

- Vue des étapes, durées, erreurs

**Irritants adressés :**

- Manque de temps pour la formation

**Valeur :**

- Debug facilité
- Comprendre ce qui se passe sous le capôt

### UC11 – Recevoir un feedback rapide

**Consommateur :** Tous  
**Objectif :** Corriger au plus tôt

**Scénario :**

- Messages d’erreur clairs

**Irritants adressés :**

- Le scan de cve n'arrive qu'a l'admission en prod. Si il y a cve je dois modifier mon code + rejouer l'entièreté de mon pipeline. C'est long

**Valeur :**

- Gain de temps

## 🟥 Observabilité & monitoring

### UC12 – Visualiser la santé d’un service

**Consommateur :** Tous  
**Objectif :** Suivre la production et l'état de ses services. Être en capacité de voir une panne avant les utilisateurs.

**Scénario :**

- Dashboard unifié (logs, métriques, alertes)
- Visualisation de l'état des services sur lesquels mon appli s'appuie

**Irritants adressés :** 

- Services transverses instables
- Identification des Bugs dans des architectures microservice 


**Valeur :**

- Vision globale de l'état de mon application


### UC13 – Recevoir des alertes pertinentes

**Consommateur :** Tous  
**Objectif :** Réagir efficacement, prise en compte des alertes remontés par les ops trop souvent ignorées.

**Scénario :**

- Consultation des alertes filtrées et ciblées
- Définition des alertes (packages de bases + définition custom)

**Irritants adressés :**

- Trop de bruit généré par des alertes incomprises, ou non adaptées au devs

**Valeur :**

- Réduction du bruit
- Meilleure réactivité

## 🟪 6. Gestion d’incident

### UC14 – Diagnostiquer un incident

**Consommateur :** Tous  
**Objectif :** Comprendre rapidement, faciliter le croisement d'information dans le cadre de résolution de bug

**Scénario :**

- En cas de bug / erreurs sur un service le developpeur utilise cette fonctionnalité pour disposer d'un diagnostic automatisé lui procurant de première piste de recherche

**Irritants adressés :**

- Le croisement de log / metrique / trace est difficile
- Absence d'expertise

**Valeur :**

- Temps moyen de réparation réduit

### UC15 – Identifier le bon contact

**Consommateur :** Développeur “consommateur de plateforme”  
**Objectif :** Escalader quand c'est nécéssaire et non plus automatiquement

**Scénario :**

- en cas d'erreur sur un de mes services la plateforme m'indique directement la responsabilité et le cas échéant l'équipe à contacter

**Irritants adressés :**

- Identification du responsable difficile
- Je ne sais pas où trouver les gens 

**Valeur :**

- Temps moyen de réparation réduit
- Décharge des experts
- Réduction du bruit

### UC16 – Accéder à un runbook

**Consommateur :** Développeur “consommateur de plateforme”  
**Objectif :** Résoudre seul 

**Scénario :**

- Accès à des procédures documentées
- Accès à un bot me guidant dans la résolution de mon bug

**Irritants adressés :**

- Charge des experts sur le MCO / MCS 

**Valeur :**

- Autonomie
- Temps moyen de réparation réduit


## 🟫 7. Gouvernance & communication

### UC17 – Consulter les changements/migrations

**Consommateur :** Tous mais surtout Manager / Lead technique

**Objectif :** Anticiper les changements, s'organiser, prévoir

**Scénario :**

- Feed des changements passé et a venir
- Centralisation des incidents

**Irritants adressés :**

- Changements non anticipés avec impacts sur les roadmaps développeurs


**Valeur :**

- Moins de surprises / meilleur suivi par les devs

### UC18 – Accéder à un catalogue de services

**Consommateur :** Tous mais surtout Manager / Lead technique  
**Objectif :** Comprendre le SI / éviter de réimplémenter des solutions / documentation facile d'accès

**Scénario :**

- Liste des services, owners, dépendances

**Irritants adressés :**

- Duplications d'outil entre unités
- Documentation dispersées
- Coordination compliquée

**Valeur :**

- Vision globale


