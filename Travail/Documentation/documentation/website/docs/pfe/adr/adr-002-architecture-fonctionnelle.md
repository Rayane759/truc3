# ADR-002 - Architecture fonctionnelle DevExperience


| | |
|---|---|
| **Référence** | ADR-002 |
| **Statut** | Proposé : en cours de validation |
| **Auteurs** | Équipe DevExperience |
| **Public** | ÉquipeDevExperiencee · équipes capabilities · architectes du SI · décideurs SI |

## Contexte

Le but de cet ADR est d'identifier le périmètre fonctionnelle de l'équipe DevExperience (PlatformEngineering). 


## Proposition

### Schema
![](./../assets/architecture-fonctionnelle.drawio.png)


### Comment lire le schéma

Le schéma d'architecture fonctionnelle est organisé en **sept grandes briques**, dont la lecture suit une double grille :

- **Le code visuel** distingue ce qui relève du **périmètre fonctionnel de la plateforme** (cases au fond gris uni) de ce qui n'en relève pas (cases au fond blanc, attribuées aux **capability teams** ou aux équipes d'infrastructure).
- **Les flèches étiquetées** (`consomme`, `fournit`, `embarque`, `utilise`, `impose des contraintes`, `s'appuie`) qualifient la nature de chaque relation entre briques, il ne s'agit pas seulement de dépendances techniques, mais de **responsabilités fonctionnelles**.

Ce double codage matérialise le principe central du modèle Team Topologies appliqué à l'Insee : **la plateforme est un canal de distribution, pas un atelier de production universel**. Elle expose, assemble et industrialise des services produits par d'autres, sans s'arroger leur expertise.

### Synthèse du périmètre

| Bloc | Périmètre | Propriétaire |
|---|---|---|
| Plateforme Expérience développeur | ✅ Dans le périmètre plateforme | Équipe Platform Experience |
| Self-Service | ✅ Dans le périmètre plateforme | Équipe Platform Experience |
| Fabrique Logicielle | ✅ Dans le périmètre plateforme | Équipe Platform Experience |
| Orchestration self-service | ✅ Dans le périmètre plateforme | Équipe Platform Experience |
| Briques transverses | ❌ Hors périmètre plateforme | Capability teams (Data, Infra VM, Sécurité…) |
| Capacités transverses | ❌ Hors périmètre plateforme | Capability teams (IAM, Sécurité, Observabilité, FinOps) |
| Substrats d'exécution | ❌ Hors périmètre plateforme | Équipes d'infrastructure (DSI, Réseau, Cloud) |

### Les briques dans le périmètre de la plateforme

#### Plateforme Expérience développeur

C'est **le visage de la plateforme**. Tout ce que le développeur voit, touche, parcourt, il ne devrait jamais avoir à descendre en dessous de cette couche pour faire son travail courant.

##### Sous-cases

- **Portail développeur**, point d'entrée unique combinant trois fonctions : *Découverte* (explorer ce que la plateforme propose), *Scaffolding* (générer un nouveau projet à partir d'un template, avec dépôt Git, pipeline et droits préconfigurés), *Documentation* (TechDocs centralisée et toujours à jour).
- **Catalogue de services**, recensement de tout ce qui existe et qui est consommable : IHM, API, CLI, librairies. C'est l'antidote au "je demande à Anatole" : ce qui n'est pas dans le catalogue n'existe pas.
- **Information concernant les changements**, communication produit sur les évolutions, les dépréciations, les incidents. La plateforme étant un produit utilisé par des centaines de personnes, sa communication doit être traitée comme une fonction à part entière.
- **Annuaire des équipes**, qui possède quoi, qui contacter pour quel service. C'est ce qui rend visible la *propriété* dans un SI où elle est habituellement diluée.
- **Suivi de mes opérations**, restitution des actions en cours et passées du développeur (Claims posées, déploiements, demandes). Sans cette visibilité, le self-service devient une boîte noire.
- **Support unique aux développeurs**, un canal unique de contact, quel que soit le sujet. Charge à la plateforme de router en interne vers la bonne capability team si nécessaire.

##### Pourquoi cette brique est dans le périmètre

Parce qu'elle est **la raison d'être** de la plateforme. L'expérience développeur unifiée est précisément ce qui justifie l'existence d'une équipe Platform Experience : sans elle, il ne reste qu'un assemblage d'outils techniques sans cohérence. Cette brique n'a *pas* d'équivalent ailleurs dans l'organisation, personne d'autre que la Platform Experience n'a la légitimité (ni la mission) de tenir cette promesse de cohérence.

#### Self-Service

Le bloc qui transforme une intention exprimée par le développeur en une **action exécutable et industrialisée**. C'est le cœur technique du contrat plateforme.

##### Sous-cases

- **Briques de construction réutilisables transverses (CI/CD, dépôt applicatif)**, templates de pipelines GitLab CI, structures de dépôts standardisées, snippets réutilisables. Ce sont les *building blocks transverses* (pas spécifiques à un domaine) que la plateforme produit elle-même.
- **Catalogue des outils en self-service**, l'exposition de l'offre : "voici ce que tu peux demander, voici les paramètres, voici ce que ça implique". Sans ce catalogue, le développeur ne peut pas formuler de demande utile.
- **Claim / Contrat d'intention déclaré**, la matérialisation déclarative d'une demande. Le développeur écrit *ce qu'il veut*, jamais *comment le produire*. C'est le contrat-pivot qui découple l'intention de l'implémentation.

##### Pourquoi cette brique est dans le périmètre

Parce que c'est l'**effet de levier** principal de la plateforme. Un template CI bien conçu, consommé par 100 équipes, fait économiser 100 fois le travail d'un seul ingénieur plateforme. Et le contrat Claim, qui rend la cible d'exécution transparente au développeur, est précisément ce qui permet à la plateforme de **faire évoluer le substrat sans casser les applications** (la future bascule cloud devient un changement d'implémentation interne, pas une réécriture côté équipes).

À noter : ce bloc *utilise* les briques produites par les capability teams (Helm, Terraform, Ansible), il ne les *produit pas*. C'est la flèche `embarque / encapsule / utilise` qui matérialise cette relation.

#### Fabrique Logicielle

Le bloc qui **transforme le code en artefact prêt à déployer**, avec les contrôles de qualité et sécurité associés.

##### Sous-cases

- **Construction des artefacts**, orchestration des jobs CI : build, tests, packaging. Mutualise les pipelines pour que chaque équipe n'écrive pas son `.gitlab-ci.yml` à partir de zéro.
- **Qualité, signature et sécurité du code**, analyse statique (SAST), scan des dépendances, scan des images de conteneurs, scan des livrables. Et signature cryptographique (cosign / Sigstore) pour garantir l'intégrité de bout en bout.
- **Stockage des artefacts signés**, registre central des images, paquets, charts. Source unique de vérité de ce qui peut être déployé.

##### Pourquoi cette brique est dans le périmètre

Parce qu'elle porte les **gates qualité et sécurité transverses** que tout artefact doit passer pour atteindre la production, sans dépendre de la rigueur individuelle de chaque équipe. La fabrique est le lieu où s'incarnent les exigences d'intégrité et de conformité de l'entrée en production.

Sa relation `impose des contraintes` avec les Capacités transverses est lisible dans les deux sens : la fabrique applique des règles définies ailleurs (politique sécurité, conformité, IAM), mais elle est *l'outilleur* qui rend ces règles effectivement appliquées sans friction côté développeur. C'est ce qui distingue *avoir une politique sécurité* (n'importe quelle DSMR en a une) de *l'appliquer systématiquement* (ce que seule une fabrique outillée permet à l'échelle de 250 développeurs).

#### Orchestration self-service

Le bloc qui **exécute** une Claim : route la demande vers le bon moteur, provisionne, configure, et accompagne la ressource tout au long de sa vie.

##### Sous-cases

- **Routage selon la cible (Kubernetes, VM, Cloud)**, choix du moteur d'exécution (Crossplane, Terraform/OpenTofu, Ansible) en fonction des paramètres de la Claim. Le développeur ne voit jamais cette bifurcation.
- **Provisionnement des ressources**, création effective de la ressource demandée (cluster, VM, base, bucket…). C'est la mécanique GitOps qui s'enclenche sur la base de la Claim.
- **Configuration Day-2**, configuration immédiate post-provisioning (installation d'agents, application de rôles Ansible, premières conventions de durcissement). Typiquement pour le monde VM.
- **Gestion du cycle de vie**, capacité essentielle souvent omise : mise à jour, redimensionnement, archivage, suppression propre. La vraie valeur du self-service n'est pas seulement de *créer*, c'est aussi de pouvoir *faire évoluer* sans procédure ticket.

##### Pourquoi cette brique est dans le périmètre

Parce que c'est le **moteur** qui rend les Claims effectives. Sans elle, le contrat Self-Service ne serait qu'une déclaration d'intention. La plateforme s'attribue ce rôle parce qu'il est **transverse aux trois mondes** d'exécution (Kubernetes, VM, cloud) et qu'aucune capability team ne couvre ce périmètre transversal : seule une équipe plateforme peut tenir cette cohérence multi-moteurs.

Sa relation `consomme` avec les Substrats d'exécution est explicite : la plateforme *utilise* les substrats fournis par les équipes d'infrastructure, elle ne les *opère* pas.


### Les briques hors du périmètre de la plateforme

C'est la partie du schéma qui formalise un choix d'architecture organisationnelle structurant : **la plateforme ne s'arroge pas l'expertise des autres équipes**. Trois grandes catégories sont explicitement positionnées hors périmètre.

#### Briques transverses (Module Ansible, Module Terraform, Chart Helm)

Ce sont les **composants spécifiques aux domaines techniques** : chart Helm applicatif standard, modules Terraform pour le provisioning d'infrastructure, rôles Ansible pour la configuration des VM.

##### Pourquoi ces briques sont hors périmètre

Parce qu'elles **encodent une expertise de domaine** que l'équipe Platform Experience n'a pas, et qu'elle ne peut pas raisonnablement avoir, sauf à devenir experte dans tous les domaines techniques du SI (Postgres, réseau, OS, sécurité applicative, messagerie…).

Concrètement :

- Le **chart Helm applicatif standard** doit encoder les bonnes pratiques de déploiement Kubernetes, les conventions d'observabilité, les pratiques de sécurité runtime, il est co-produit par les capability teams concernées (Observabilité, Sécurité).
- Les **modules Terraform** pour le provisioning VM ou cloud doivent encoder l'expertise infrastructure (dimensionnement, réseau, durcissement OS), ils sont produits par la capability team Infra.
- Les **rôles Ansible** standards (installation d'agents, durcissement, conformité OS) sont produits par la capability team Infra VM.

La relation `embarque / encapsule / utilise` avec le bloc Self-Service est claire : la plateforme **consomme** ces briques produites ailleurs, les **distribue** via son Self-Service au développeur, et **garantit qu'elles s'intègrent** dans son golden path. Mais elle ne les produit pas.

Cette répartition obéit à un principe simple : **plus une brique encode une expertise de domaine, plus elle appartient à la capability team correspondante**. La plateforme reste propriétaire des seules briques *vraiment transverses* (templates CI/CD, scaffolding), celles qui n'appartiennent à personne d'autre.

#### Capacités transverses (Identité, Secrets, Observabilité, Gouvernance, FinOps)

Ce sont des **fonctions à dimension institutionnelle** qui dépassent le périmètre d'un produit plateforme.

##### Pourquoi ces capacités sont hors périmètre

Pour chacune, la raison est légèrement différente, mais le principe est commun :

- **Identité & accès**, la politique d'identité Insee (SUGOI, fédération, MFA, durée de session) est définie par la fonction Sécurité du SI, pas par la plateforme. La plateforme *consomme* cette politique via Keycloak, elle ne la *décide* pas.
- **Gestion des secrets**, la politique de gestion des secrets (rotation, classification, audit) relève de la fonction Sécurité. La plateforme utilise les outils (Vault + External Secrets Operator) pour rendre la politique applicable, mais n'en est pas l'autorité ni la maintenicienne.
- **Observabilité**, la capability team Observabilité produit et opère la stack (Prometheus, Grafana, Loki, Elastic), définit les conventions de logs et métriques, maintient les bibliothèques d'instrumentation.
- **Gouvernance / conformité**, relève de la DSMR (PES existante) et de la gouvernance SI Insee. La plateforme implémente les politiques (via policy-as-code par exemple) mais ne les arbitre pas.
- **FinOps**, la fonction FinOps (suivi des coûts, allocations, prévisions) est une discipline transversale du SI, pas une fonction de la plateforme. La plateforme expose les données de consommation, le FinOps les exploite..

La relation `impose des contraintes` (vers Fabrique) et `s'appuie` (vers Orchestration) capture cette double dynamique : ces capacités **dictent les règles** que la plateforme doit appliquer, et **fournissent les services** sur lesquels la plateforme repose. La plateforme est leur *intégrateur*, jamais leur *propriétaire*.

Conséquence pratique forte : l'équipe Platform Experience travaille **en partenariat étroit** avec ces capability teams, mais ne se substitue pas à elles. Quand un développeur a une question profonde sur la sécurité applicative, la plateforme l'**oriente** vers la capability team Sécurité ; elle ne tranche pas elle-même.

#### Substrats d'exécution (Monde Kubernetes, Monde VM on-prem, Monde Cloud Souverain)

Ce sont les **environnements physiques et logiques** sur lesquels les workloads s'exécutent.

##### Pourquoi ces substrats sont hors périmètre

Parce qu'ils relèvent des **équipes d'opération avec de l'expertise sur l'infrastructure** : exploitation des clusters Kubernetes (IDDA + KubeSocle + réseau + ....), gestion du parc VM (IDDA + Système + ...), contractualisation et opération du futur cloud souverain (« Les archis », architectes en charge du choix cible).

La plateforme **consomme** ces substrats comme des services : elle déploie ses workloads sur les clusters Kubernetes, demande des VM au parc IDDA, demandera demain des ressources sur le cloud souverain. Mais elle n'a pas vocation à opérer ces substrats, le ferait-elle qu'elle dupliquerait des compétences déjà présentes ailleurs dans l'organisation et brouillerait les responsabilités d'exploitation.

L'intérêt fonctionnel de l'avoir représenté dans le schéma, bien que hors périmètre, est de matérialiser la **cible-agnosticité** du contrat Claim : trois mondes en aval, un seul contrat en amont. C'est cette propriété qui rend la migration cloud future possible sans réécriture applicative.

### Lecture des relations entre blocs

Les flèches du schéma ne sont pas des dépendances techniques mais des **relations de responsabilité** :

| Relation | Sens fonctionnel |
|---|---|
| Développeur **consomme** Plateforme Expérience développeur | Le développeur n'interagit qu'avec cette couche ; tout le reste est servi |
| Plateforme Expérience développeur ← **fournit** ← Self-Service | Le portail expose ce que le Self-Service met à disposition |
| Self-Service **embarque / encapsule / utilise** Briques transverses | La plateforme distribue les briques produites par les capability teams |
| Self-Service **utilise** Fabrique Logicielle et Orchestration | Le Self-Service est le pivot qui mobilise les autres blocs |
| Fabrique Logicielle ← **impose des contraintes** ← Capacités transverses | Les capacités transverses dictent les règles que la fabrique applique |
| Orchestration **s'appuie** sur Capacités transverses | L'orchestration utilise les services fournis par les capability teams |
| Orchestration **consomme** Substrats d'exécution | La plateforme n'opère pas les substrats, elle les utilise |

Cette grille de lecture, plus que la liste des briques, est le **vrai contenu d'architecture** du schéma. Elle dit qui dépend de qui, qui fournit quoi à qui, et, implicitement, où sont les frontières de responsabilité au sein du SI.

### Pourquoi ce découpage importe

Le découpage hachuré / plein n'est pas un détail de présentation. Il porte trois conséquences opérationnelles directes pour la mise en œuvre de la démarche.

**Premièrement**, il **dimensionne correctement l'équipe Platform Experience**. Si l'on avait fait entrer toutes les briques transverses dans son périmètre, l'équipe aurait besoin de spécialistes Postgres, Kafka, réseau, sécurité applicative, FinOps…, c'est-à-dire un effectif intenable. En la cantonnant à son périmètre légitime (l'expérience développeur et la tuyauterie transverse), elle reste à taille humaine.

**Deuxièmement**, il **donne aux capability teams un canal de distribution** plutôt qu'un concurrent. Une capability team voit la plateforme comme la voie par laquelle son expertise atteint les équipes applicatives, ce qui aligne ses intérêts avec ceux de la plateforme, au lieu de créer une dynamique politique adverse.

**Troisièmement**, il **clarifie le contrat aux yeux des équipes applicatives**. Le développeur sait que pour un problème de portail, de pipeline, de Claim, il s'adresse à Platform Experience ; pour un problème métier d'observabilité ou de base de données, à la capability team correspondante. Le support unique (sous-case du Portail) garantit qu'il n'a pas besoin de connaître ce découpage de l'extérieur, mais la plateforme, en interne, sait à qui transférer.

Sans ce découpage, la plateforme devient soit un goulot d'étranglement (tout passe par elle), soit une coquille vide (elle ne fait rien que personne d'autre ne fasse déjà). Le positionnement représenté ici est l'**équilibre fonctionnel** qui rend une plateforme à la fois utile et soutenable dans la durée.