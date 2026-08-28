# Les clients

## Proto-personnas des client potentiels

Cette typologie illustre une progression des rôles selon leur niveau d’autonomie, leur proximité avec la production et leur responsabilité sur la plateforme.

### Le nouveau développeur

Profil :

- vient d’intégrer l’équipe ou l’entreprise
- ne connaît pas encore :
  - l’environnement technique
  - les pratiques internes
  - les outils et standards
- ne sait pas toujours où trouver l’information

Besoins principaux :

- onboarding rapide
- documentation claire
- environnements prêts à l’emploi
- chemins guidés (“golden paths”)
- liens vers les ressources (dépôts git, observabilité,...)

### Le développeur applicatif (dev full stack)

Profil :

- expert du développement métier
- se concentre principalement sur :
  - le code
  - l’architecture applicative
  - la logique fonctionnelle

Caractéristiques :

- faible appétence pour l’infrastructure
- **ne veut pas entendre parler d'infrastructure**

Besoins principaux:

- 👉 Son objectif : livrer vite sans gérer la complexité infra.
- la qualité/simplicité des outils pour le déploiement
- la simplicité des déploiements
- stabilité des environnements

### Le dev avec profil ci / devops

Profil :

- spécialiste de l’intégration continue
- maîtrise :
  - pipelines CI/CD
  - tests automatisés
  - quality gates
  - stratégies de branches (GitFlow, trunk-based, etc.)
  - déployer sur Kubernetes / VM
  - utiliser les services fournis par l’équipe Ops

Responsabilités :

- transformer le code en artefacts livrables
- fiabiliser la chaîne de build et de test
- Mettre en place la chaine de déploiements
- S'intégrer dans les différents outils

Caractéristiques :

- fort niveau d’autonomie
- utilise les services existants sans forcément maîtriser :
  - les couches basses
  - le réseau
  - la sécurité avancée

⚠️ Ce rôle est souvent appelé “DevOps”, mais en réalité :

- DevOps est une pratique/culture, pas un rôle

### (Le Site Reliability Engineer (SRE))

Profil :

- ingénieur logiciel spécialisé dans la production
- se concentre sur :
  - la fiabilité
  - la disponibilité
  - la performance
  - la gestion des incidents

Responsabilités :

- conception de systèmes hautement disponibles
- définition des SLO / SLA
- automatisation de l’exploitation
- gestion des incidents complexes

👉 C’est l’expert que l’on sollicite pour les systèmes critiques et les problèmes de production majeurs ou quand une application à des besoins particuliers.

**Remarque** : On n'est pas sur d'en avoir à l'Insee, à déterminer à la suite des interviews

### (Le chef de projet)

Profil:

- encadre et suit un projet
- s'engage sur des échéances, pilote les travaux
- Souhaite des metriques aggréger et rapide d'accès

Objectif:

- Avoir des métriques sur le déploiement
- Avancé vite sans revenir dessus

**Remarque** : Non prioritaire à l'heure actuelle


### (Les selfeurs / équipes métier)

Profil:

- Possède les connaissances métiers
- Certains poweruser qui souhaite intervenir dans le développement des briques applicatives et qui sont capable de déployer des briques en autonomie.
- Le successeur du poste peut ne pas savoir faire la même chose que la personne actuellement titulaire du poste (non transmission des compétences)

**Remarque** : Non prioritaire à l'heure actuelle


## Les protospersonnas (acteurs) gravitant autour de la solution

### L’Ops moderne

Profil :

- maîtrise les services d’infrastructure et de production
- conçoit et maintient une **offre de services interne** :
  - clusters
  - CI/CD
  - observabilité
  - sécurité
  - services managés

Responsabilités :

- fournir des outils stable et standardisée
- simplifier l’adoption pour les développeurs
- intégrer sécurité, conformité et gouvernance by design

### L'architecte

Profil :

- maîtrise les offres de services d’infrastructure et de production
- maîtrise les pattern de conception/déploiement applicative/infrastructure

Objectifs :

- accompagner / conseiller les équipes
- assurer une cohérence
- uniformiser les

### La sécurité

Profil :

- maîtrise les offres de services d’infrastructure et de production
- maîtrise les pattern de conception/déploiement applicative/infrastructure

Objectifs :

- identifier les risques
- alerter en cas de failles de sécurité

### L'urbaniste

Profil :

- A une vision organisationnelle du SI