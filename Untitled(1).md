## Autres cas d'usage complémentaires

Le cas étudié jusqu'ici se concentrait sur la modification de la configuration d'une application déjà déployée sur Kubernetes. Cette section fait l'analyse de deux autres cas d'usage que la plateforme pourrait couvrir : la modification d'un déploiement Cloud, et la modification d'un déploiement VM.

Pour chaque cas, on suppose que **Backstage et ArgoCD sont déjà présents** dans les 4 solutions. Les étapes communes au cas Kubernetes (clic sur le bouton "Modifier la configuration" dans Backstage, ouverture et review d'une MR, etc.) ne sont pas réexpliquées en détail : seules les différences propres à chaque cas d'usage sont développées.

---

## Cas d'usage : Modification d'un déploiement Cloud

*Un développeur souhaite modifier la configuration d'une ressource Cloud associée à son application (par exemple, augmenter la taille d'une base de données managée, ou ajouter une règle réseau à un VPC existant).*

### Solution 1 : Backstage seul

#### Expérience développeur

Identique au cas Kubernetes : formulaire Backstage, génération de fichiers, ouverture de MR, review, puis pipeline CI/CD. Mais au lieu d'un manifeste Kubernetes, le template Backstage génère un fichier Terraform (ou tout autre outil IaC déjà utilisé en interne) correspondant à la ressource Cloud concernée, ainsi qu'un playbook Ansible en cas de modification sur la configuration applicative ou logicielle.

#### Ce que fait la plateforme

La pipeline CI/CD exécute un `terraform plan` puis un `terraform apply` (ou l'équivalent selon l'outil IaC en place) au lieu d'un `helm upgrade`, suivi d'un `ànsible-playbook` qui cible la ressource modifiée. Comme pour le cas Kubernetes, aucune validation technique n'intervient avant l'exécution : tout repose sur la qualité du template Backstage et sur la review de la MR.

#### Expérience équipe plateforme

L'équipe plateforme doit créer un template Backstage dédié aux ressources Cloud, générant des fichiers Terraform valides ainsi que des playbooks/variables Ansible. Elle doit également adapter la pipeline CI/CD pour exécuter les commandes Terraform appropriées, avec gestion du state Terraform (backend distant, verrouillage, etc.), ce qui est une responsabilité supplémentaire par rapport au cas Kubernetes, où Helm ne nécessite pas de gestion d'état externe (je crois).

---

### Solution 2 : Crossplane

#### Expérience développeur

Identique au cas Kubernetes. La différence se situe dans les champs disponibles : la XR peut exposer des champs propres aux ressources Cloud (taille de base de données, plage CIDR, etc.), validés par le même mécanisme de schéma XRD que pour les ressources Kubernetes.

```yaml
apiVersion: platform.company.io/v1alpha1
kind: MyApp
metadata:
  name: my-service
spec:
  env: production
  replicas: 3
  resources: medium
  expose: public
  database:
    engine: postgres
    size: medium
    multiAZ: true
```

#### Ce que fait la plateforme

C'est ici que Crossplane présente un avantage pour le Cloud : une seule Composition peut combiner plusieurs ressources Cloud interdépendantes (VPC, Subnet, Security Group, instance de base de données managée, ...) en utilisant des références croisées entre ressources (par exemple, l'ID du VPC créé est automatiquement injecté dans le Security Group, qui est lui-même injecté dans l'instance de base de données). Crossplane résout ces dépendances dans l'ordre correct et attend qu'une ressource soit prête avant de provisionner celle qui en dépend.

De plus, Crossplane peut faire appel à `provider-ansible` pour gérer la configuration logicielle des ressources déployées par Crossplane à l'aide des Provider Cloud (`provider-aws`, `provider-gcp`, `provider-azure`, ...).

La réconciliation continue s'applique pleinement à la partie provisionnée par les Providers Cloud natifs (taille de la base de données, règles réseau...). Sur la partie configurée par `provider-ansible`, la même nuance de granularité que pour le monde VM s'applique : Crossplane observe le succès ou l'échec du run, sans visibilité fine sur l'état interne au-delà de ce que le playbook rapporte.

#### Expérience équipe plateforme

En plus des éléments déjà listés pour le cas Kubernetes, l'équipe plateforme doit installer et configurer le Provider Cloud correspondant (`provider-aws`, `provider-gcp`, `provider-azure`, ...) avec les credentials et permissions IAM nécessaires, et concevoir des Compositions capables d'orchestrer plusieurs ressources Cloud interdépendantes, ce qui demande une bonne connaissance du modèle de ressources du fournisseur Cloud concerné. 
Aussi,  l'équipe doit également installer `provider-ansible` et maintenir les playbooks correspondants.

---

### Solution 3 : Kratix

#### Expérience développeur

Identique au cas Kubernetes : Aucune différence visible pour le développeur entre une modification Kubernetes et une modification Cloud, c'est le pipeline derrière la Promise qui gère la différence.

#### Ce que fait la plateforme

Le pipeline de la Promise exécute les mêmes étapes de validation et d'approbation que pour le cas Kubernetes. La différence se situe dans l'étape de génération : au lieu de produire des manifestes Kubernetes, un step du pipeline exécute un `terraform plan` puis un `terraform apply` sur le module correspondant à la ressource Cloud demandée (ou appelle directement l'API du fournisseur Cloud via un SDK). Puis, un autre step exécute le playbook Ansible correspondant pour appliquer la configuration logicielle pour la ressource déployée.

Deux approches sont possibles pour la partie "provisioning" : 

- Exécuter Terraform directement dans le pipeline (plan, validation du plan, apply)
- `Paragraphe ajouté par l'IA` Déléguer la création à un opérateur Terraform tiers (Terraform Cloud Operator de HashiCorp, ou Terraform Controller) piloté par le mécanisme de scheduling GitOps de Kratix, en écrivant la ressource correspondante dans le State Store.

La réconciliation périodique de Kratix (toutes les 10 heures par défaut) s'applique également aux ressources Cloud ainsi créées.

#### Expérience équipe plateforme

En plus des éléments déjà listés pour le cas Kubernetes, l'équipe plateforme doit développer (ou adapter) les conteneurs de pipeline exécutant Terraform et Ansible, gérer le state Terraform, définir les credentials Cloud nécessaires à l'exécution de ces conteneurs et gérer l'inventaie Ansible correspondant aux ressources créées. Si l'approche avec un opérateur tiers est retenue, l'équipe doit également installer et configurer cet opérateur sur le cluster cible.

---

### Solution 4 : Crossplane + Kratix

#### Expérience développeur

Identique à la solution 3.

#### Ce que fait la plateforme

Comme pour le cas Kubernetes, le pipeline Kratix gère la validation et l'approbation, puis génère une XR Crossplane et l'écrit dans le State Store. ArgoCD applique cette XR, et Crossplane prend le relais pour provisionner et réconcilier en continu les ressources Cloud ainsi que pour la configuration logicielle avec `provider-ansible`, en bénéficiant de la gestion native des dépendances entre ressources décrite dans la solution 2.

Cette combinaison permet aussi d'éviter la gestion manuelle du state Terraform évoquée dans les solutions 1 et 3 : Crossplane gère lui-même l'état des ressources Cloud via ses managed resources, sans nécessiter de backend Terraform séparé.

#### Expérience équipe plateforme

Cumul des responsabilités des solutions 2 et 3 : Provider Cloud et Ansible Crossplane à configurer, Compositions à concevoir pour les ressources Cloud, en plus du pipeline Kratix pour la validation et l'approbation. L'équipe plateforme n'a en revanche pas à gérer de state Terraform séparé, ce qui retire l'une des charges identifiées dans les solutions 1 et 3.

---

## Cas d'usage : Modification d'un déploiement VM

*Un développeur souhaite modifier la configuration d'une application déployée sur une VM (par exemple, redimensionner la VM, ou ajuster sa configuration réseau).*

> **Préalable :** ce cas d'usage suppose que l'organisation dispose déjà d'outils de gestion des VMs (scripts, modules Terraform, API interne...). Les 4 solutions s'appuient sur ces outils existants plutôt que de les remplacer.

### Solution 1 : Backstage seul

#### Expérience développeur

Identique au cas Kubernetes et au cas Cloud : formulaire Backstage, MR, review, pipeline CI/CD. Le template Backstage génère cette fois les fichiers attendus par l'outil de gestion VM existant (playbook Ansible, fichier Terraform pour un provider VM, appel à l'API interne...).

#### Ce que fait la plateforme

La pipeline CI/CD invoque d'abord l'outil de gestion VM existant avec les paramètres générés, puis enchaîne avec l'exécution du playbook Ansible (potentiellement via un appel à RunDeck ?). Aucune adaptation profonde n'est nécessaire si l'outil expose déjà une interface en ligne de commande ou une API appelable depuis une pipeline.

#### Expérience équipe plateforme

L'équipe plateforme doit créer un template Backstage capable de générer les fichiers ou appels attendus pour le "provisioning" et pour la configuration d'Ansible, et adapter la pipeline CI/CD pour les enchaîner.

---

### Solution 2 : Crossplane

#### Expérience développeur

Identique au cas Kubernetes mais avec des champs propres à la configuration VM (taille, réseau, etc.), validés par le schéma XRD.

#### Ce que fait la plateforme

Dans notre contexte (Ansible), un Provider Crossplane existe : `provider-ansible`, qui expose une ressource managée `AnsibleRun` permettant d'exécuter un playbook ou un rôle Ansible (récupéré depuis un dépôt Git, ou je sais pas où) directement piloté par une XR. C'est un Provider maintenu par la communauté `crossplane-contrib` (donc pas par la "vraie" équipe de Crossplane).

Si le provisioning de la VM passe également par un Provider Crossplane (par exemple un Provider vSphere), la Composition peut enchaîner provisioning et configuration au sein d'une même XR, sur le modèle déjà décrit pour le Cloud. Si le provisioning VM reste piloté par un outil hors du périmètre Crossplane, seule l'étape de configuration (via `provider-ansible`) est alors couverte nativement par Crossplane.

`Paragraphe ajouté par l'IA`
Une nuance importante distingue toutefois ce Provider des Providers Cloud classiques (AWS, GCP, Azure) : ces derniers connaissent chaque champ de la ressource distante et peuvent détecter une dérive précise sur n'importe quel paramètre (taille de VM, configuration réseau, etc.). `provider-ansible`, lui, exécute le playbook et observe le succès ou l'échec du run, sans avoir de visibilité fine sur l'état interne de la VM au-delà de ce que le playbook lui-même rapporte. La réconciliation continue existe donc bien (Crossplane peut rejouer le playbook si une dérive est détectée), mais sa granularité dépend directement de la qualité et de l'idempotence des playbooks Ansible existants.

#### Expérience équipe plateforme

`Paragraphe étoffé par l'IA`
En plus des éléments du cas Kubernetes, l'équipe plateforme doit installer et configurer `provider-ansible` (c'est le même que pour le cas Cloud, donc en vrai on ne fait cet effort qu'une seule fois), définir les `AnsibleRun` qui référencent les playbooks ou rôles existants (potentiellement stockés et versionnés dans Nexus ou un dépôt Git), et gérer les credentials nécessaires à l'exécution distante. L'effort de migration dépend largement de l'idempotence des playbooks déjà en place : des playbooks bien conçus se prêtent facilement à ce mode de pilotage, tandis que des playbooks impératifs ou avec des effets de bord nécessiteront un travail de mise en conformité avant d'être pilotables depuis une XR.

---

### Solution 3 : Kratix

#### Expérience développeur

Identique aux autres cas : formulaire Backstage, ResourceRequest, approbation, confirmation.

#### Ce que fait la plateforme

Le pipeline de la Promise appelle l'outil de provisioning VM existant (en exécutant un script, un module Terraform, ou un appel API par exemple) exactement comme il appellerait un outil Terraform pour une ressource Cloud. Puis, le pipeline déclenche l'exécution du playbook Ansible (via Rundeck par exemple, encore ?) pour la configuration applicative. Cette approche ne dépend de la maturité d'aucun Provider spécifique : tant que l'outil VM expose une interface programmable, Kratix peut orchestrer ces 2 étapes.

La flexibilité du modèle pipeline de Kratix présente un avantage par rapport à Crossplane pour le monde VM : il n'y a pas de notion de "Provider" à trouver ou à valider, l'équipe plateforme utilise directement les outils déjà en place.

#### Expérience équipe plateforme

En plus des éléments du cas Kubernetes, l'équipe plateforme doit développer le conteneur de pipeline qui invoque l'outil VM existant, avec gestion des credentials nécessaires. La charge de travail est comparable à celle décrite pour le cas Cloud avec Terraform.

---

### Solution 4 : Crossplane + Kratix

#### Expérience développeur

Identique à la solution 3.

#### Ce que fait la plateforme

Deux approches sont possibles selon la maturité du Provider VM disponible : 

- Si un Provider Crossplane suffisamment mature existe pour l'outil de virtualisation, le pipeline Kratix génère une XR Crossplane comme pour les cas Kubernetes et Cloud, et Crossplane prend le relais pour le provisioning, la configuration (avec Ansible du coup) et la réconciliation continue.
- Si aucun Provider adapté n'existe, le pipeline Kratix appelle directement les outils existants (comme en solution 3), sans passer par Crossplane pour cette ressource spécifique. Dans ce cas, le monde VM ne bénéficie pas de la réconciliation continue de Crossplane.

#### Expérience équipe plateforme

Identique à la solution 3 si aucun Provider Crossplane n'est utilisé pour les VMs ; cumul des solutions 2 et 3 si un Provider suffisamment mature est disponible et retenu.

---

## Synthèse rapide

|                           | Backstage seul                             | Crossplane                                                                                | Kratix                                                            | Crossplane + Kratix                                                          |
| ------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Cloud - Provisioning**  | Terraform en pipeline CI/CD, state à gérer | Natif, dépendances entre ressources gérées, réconciliation continue                       | Terraform en pipeline, réconciliation périodique (10h)            | Combine réconciliation continue Crossplane et workflow Kratix                |
| **Cloud - Configuration** | Ansible en pipeline CI/CD après Terraform  | `provider-ansible` (communautaire), réconciliation à granularité dépendante des playbooks | Ansible en pipeline après Terraform                               | `provider-ansible` piloté par la XR, combiné au workflow Kratix              |
| **VM - Provisioning**     | Outil existant invoqué en pipeline CI/CD   | Dépend de la maturité du Provider VM (souvent communautaire/incertain)                    | Outil existant invoqué en pipeline, sans dépendance à un Provider | Selon maturité du Provider : XR Crossplane ou appel direct comme Kratix seul |
| **VM - Configuration**    | Ansible/Rundeck en pipeline CI/CD          | `provider-ansible` (comme pour le Cloud)                                                  | Ansible/Rundeck en pipeline                                       | `provider-ansible` combiné au workflow Kratix                                |


En réalité, Ansible n'est pas un outil propre au monde VM, mais l'outil de configuration retenu, et ce quel que soit le monde concerné. Crossplane y accède via le même Provider (provider-ansible) sur le Cloud comme sur le VM, avec la même réserve de granularité dans les deux cas. Kratix, de son côté, orchestre Terraform et Ansible de façon symétrique sur les deux mondes, sans dépendre de la disponibilité d'un Provider Crossplane pour l'un ou l'autre. L'avantage net de Crossplane reste donc concentré sur le provisioning Cloud (dépendances entre ressources, Providers matures) — pas sur la configuration, où les deux solutions s'appuient en définitive sur le même outil (Ansible) avec une réserve de maturité comparable.

## Décision

### Bilan

Les quatre solutions partagent la même interface développeur (formulaire Backstage) et des performances comparables une fois en place. Ce qui les différencie, c'est le niveau de contrôle et de robustesse offert à l'équipe plateforme, le coût (compétences, temps, complexité), et, point central pour ce qui suit, leur capacité à couvrir nativement les trois mondes que nous opérons : VM, Kubernetes et Cloud.

**Backstage seul** est la solution la plus accessible et la plus rapide à mettre en place. Elle repose sur des outils maîtrisés (Git, CI/CD, et les outils d'exécution déjà en place comme Ansible ou Terraform) et ne demande pas de compétences Kubernetes avancées. Sa faiblesse est l'absence d'enforcement côté serveur : les validations n'existent que dans le formulaire Backstage, contournable par une MR directe ou une exécution manuelle. La scalabilité est également limitée : la charge de l'équipe plateforme augmente avec le nombre d'équipes. C'est une solution viable pour démarrer, mais qui devient de plus en plus difficile à tenir à mesure que la plateforme grandit, et ce quel que soit le monde considéré (VM, Kube, Cloud).

**Crossplane** introduit un niveau de rigueur technique important : le schéma XRD enforce les validations à chaque `kubectl apply`, et la réconciliation continue garantit que l'état du cluster reste conforme à la configuration déclarée. Sur le Cloud, c'est un atout majeur : une seule Composition peut orchestrer plusieurs ressources interdépendantes (VPC, Subnet, base de données managée...) avec résolution automatique des dépendances. Sur le monde VM, Crossplane dispose d'un Provider Ansible (`provider-ansible`, maintenu par la communauté `crossplane-contrib`) permettant de piloter nos playbooks existants depuis une XR, mais la réconciliation qui en résulte n'a pas la même granularité que sur une ressource Cloud : Crossplane observe le succès ou l'échec du run Ansible, sans visibilité fine sur l'état interne de la VM au-delà de ce que le playbook rapporte lui-même. En revanche, la courbe d'apprentissage est élevée (Composition Functions, mode Pipeline, Providers), le débogage peut être complexe, et les règles organisationnelles (quotas, approbation humaine) nécessitent des outils externes (OPA, Kyverno).

**Kratix** adopte une approche différente : plutôt que de gérer l'état en continu, il orchestre des workflows. Son point fort est l'expressivité de ses pipelines : toute règle métier peut y être encodée directement en Python ou Go, et surtout, **un step de pipeline peut appeler n'importe quel outil existant** (Terraform pour le Cloud, Ansible/Rundeck pour les VMs, ...) sans dépendre de la disponibilité d'un Provider dédié à cet outil. Contrairement à Crossplane qui a besoin d'un Provider spécifique pour chaque type de ressource (mature pour le Cloud, communautaire et plus jeune pour Ansible/VM), Kratix se contente d'une API ou d'une CLI à invoquer, ce qui correspond exactement à ce que Rundeck expose déjà. L'approbation humaine, la vérification de quotas, les notifications, se passent dans le pipeline de la Promise, sans outil externe. La réconciliation est assurée par la combinaison de la loop périodique de Kratix et d'ArgoCD.

**Crossplane + Kratix** combine la richesse des workflows Kratix pour la validation et la gouvernance, et la réconciliation continue de Crossplane pour la robustesse (sur les mondes où Crossplane dispose d'un Provider suffisamment mature (Kubernetes, Cloud, et potentiellement VM via `provider-ansible` si nos playbooks s'y prêtent bien)). C'est la solution la plus complète, mais aussi la plus complexe à mettre en place, à maintenir et à déboguer. Elle exige des compétences dans les deux outils simultanément et un travail de cohérence entre les Promises Kratix et les XRDs Crossplane.

---

### Keskonfé

#### Privilégier Backstage seul si :
- L'équipe plateforme est peu disponible pour investir dans de nouveaux outils.
- Il faut livrer un Golden Path fonctionnel rapidement, quitte à l'enrichir plus tard.
- Les équipes de développement sont peu nombreuses et peuvent se reposer sur des conventions et des reviews humaines.
- Il n'existe pas encore de culture Kubernetes avancée dans l'équipe plateforme.

> La dette technique s'accumule vite si le nombre d'équipes ou d'applications augmente. Prévoir l'intégration d'une autre solution dès que possible.

#### Privilégier Crossplane si :
- L'équipe plateforme a (ou peut acquérir) une solide culture Kubernetes et IaC.
- La priorité est la réconciliation continue fine : s'assurer qu'aucune dérive ne peut persister, avec ou sans intervention humaine.
- Les ressources à gérer sont majoritairement des ressources Cloud ou Kubernetes natives, où les Providers Crossplane sont matures.
- Les règles organisationnelles sont relativement simples (la validation de schéma suffit).
- L'équipe est à l'aise avec un modèle purement déclaratif et ne ressent pas le besoin de workflows impératifs.

> Pour le monde VM, la maturité du Provider disponible (`provider-ansible` dans notre cas) doit être évaluée avant de s'appuyer dessus pour des usages critiques. Aussi, ne pas sous-estimer le temps d'apprentissage des Composition Functions.

#### Privilégier Kratix si :
- L'équipe plateforme a une culture développement (Python, Go) plus qu'une culture infrastructure pure.
- Les règles organisationnelles sont complexes ou nombreuses : approbation humaine, vérification de quotas, notifications.
- La plateforme doit unifier des mondes hétérogènes (VM, Kube, Cloud) en s'appuyant sur des outils déjà en place, sans attendre la disponibilité d'un Provider dédié pour chacun.
- On veut garder la main sur la logique métier sans dépendre d'outils externes (OPA/Kyverno).
- Le passage à l'échelle est un enjeu majeur (les Promises s'appliquent à toutes les équipes sans effort supplémentaire).

> Les conteneurs de pipeline doivent être traités comme de vrais projets logiciels (tests, CI/CD pour les images, versioning). Ne pas négliger cet investissement.

#### Privilégier Crossplane + Kratix si :
- La plateforme doit être robuste et évolutive sur le long terme, et l'équipe est prête à assumer la complexité.
- Les deux besoins sont présents simultanément : workflows organisationnels complexes (Kratix) et réconciliation continue stricte (Crossplane, sur les mondes où cette réconciliation fine est disponible et fiable).
- L'équipe plateforme est suffisamment dimensionnée pour maintenir deux outils en conditions opérationnelles.
- La gouvernance est un enjeu fort : double enforcement (pipeline Kratix + schéma XRD Crossplane).

> Vérifier que les besoins justifient la complexité. Définir dès le départ la frontière de responsabilité entre les deux outils, monde par monde (VM / Kube / Cloud), pour éviter les zones grises lors du débogage.

---

### Notre situation

L'équipe plateforme est composée d'environ 6 personnes ayant une bonne culture Kubernetes, de développement (Python notamment) et de CI/CD. ArgoCD est déjà en place. La plateforme a vocation à servir un grand nombre d'équipes de développeurs, gérant à la fois de nouveaux projets et des applications existantes à mettre en conformité avec les bonnes pratiques. Le passage en production implique une validation humaine obligatoire. La création d'environnements de test doit être simple pour les développeurs.

Le point le plus structurant pour la suite : **notre parc est aujourd'hui majoritairement composé de VMs, gérées via Ansible, Nexus (artefacts) et Rundeck (orchestration et exécution des jobs/playbooks)**, mais la trajectoire de l'entreprise va clairement vers davantage de Kubernetes et de Cloud. Le Golden Path doit donc fonctionner dès aujourd'hui avec notre réalité VM dominante, tout en restant capable d'absorber la bascule progressive vers Kube et Cloud sans tout reconstruire.

C'est cette double contrainte (présent majoritairement VM, avenir majoritairement Kube/Cloud) qui oriente la recommandation.

---

### Solution recommandée : Kratix, avec extension de périmètre vers Crossplane

#### Pourquoi Kratix est le bon point de départ pour notre contexte

**Kratix traite VM, Kube et Cloud de manière symétrique**, ce qui est précisément notre besoin actuel. Un step de pipeline Kratix peut appeler l'API REST de Rundeck pour déclencher un job existant (lui-même basé sur un playbook Ansible), exactement comme il appellerait `terraform apply` pour une ressource Cloud, ou générerait un manifeste Kubernetes. Aucun de ces trois chemins ne dépend de la disponibilité ou de la maturité d'un Provider dédié. C'est un argument majeur au vu de notre parc majoritairement VM aujourd'hui.

Les autres atouts de Kratix restent ceux identifiés précédemment dans ce rapport :

- **Validation humaine en production** via le mécanisme de suspension natif (`suspend`), pile ce qu'il faut pour notre exigence de validation humaine en production.
- **Environnements différenciés** : un pipeline léger sans approbation pour le bac à sable de développement, un pipeline complet avec validations pour la production, et cette logique fonctionne identiquement qu'on déploie sur VM, Kube ou Cloud.
- **Scalabilité** : les Promises s'appliquent à toutes les équipes sans effort supplémentaire, ce qui est nécessaire compte tenu du nombre d'équipes à servir.
- **Compétences disponibles** : l'équipe a le profil pour Kratix (Python, Kubernetes, CI/CD), et ArgoCD est déjà en place pour la couche GitOps.
- **Mise en conformité des applications existantes** : le pipeline Kratix peut être déclenché sur des applications déjà déployées (notamment sur VM) via une ResourceRequest, ce qui correspond exactement à notre besoin de mise à niveau du parc existant.

#### Comment Kratix s'articule avec Rundeck, Ansible et Nexus concrètement

Le pipeline d'une Promise "application VM" pourrait : 
- Valider les paramètres soumis par le développeur
- Vérifier les quotas et règles organisationnelles
- Attendre l'approbation humaine si besoin
- Déclencher un job Rundeck existant via son API : `Parenthèse ajoutée par l'IA`(le job exécutant lui-même le playbook Ansible approprié, dont les rôles sont versionnés et récupérés depuis Nexus). 

Rundeck continue donc à jouer son rôle d'aujourd'hui (exécution, RBAC sur les nœuds, audit des runs). Kratix ajoute donc la couche de validation métier et d'approbation en amont, et Backstage unifie l'interface développeur avec les mondes Kube et Cloud.

#### Extension de périmètre : ajouter Crossplane

L'ajout de Crossplane devient pertinent au fur et à mesure de la bascule de notre parc vers Kube et Cloud :

- **Sur le Cloud :** Dès que la gestion de ressources cloud (bases de données managées, réseaux, buckets, ...) prend de l'ampleur et que la réconciliation continue fine devient un besoin opérationnel réel. C'est surtout là que Crossplane apporte le plus de valeur on dirait, avec des Providers matures (AWS, GCP, Azure, ...).
- **Sur Kubernetes :** Au fur et à mesure que les applications migrent de VM vers Kube, en suivant le modèle déjà détaillé dans ce rapport (XRD, Compositions, ...).
- **Sur le monde VM :** C'est plus prudent : `provider-ansible` permet de piloter nos playbooks existants depuis une XR, mais avant de généraliser cette approche, il faudrait évaluer si nos playbooks sont suffisamment idempotents pour en tirer une réconciliation fiable, et si le gain (réconciliation plus fréquente que la loop Kratix) justifie la complexité d'ajout par rapport à la combinaison Kratix + Rundeck déjà fonctionnelle.

En pratique, cela signifie que la part du parc gérée par Crossplane augmente avec la bascule Kube/Cloud déjà engagée, sans qu'il soit nécessaire de migrer le socle VM existant. Rundeck et Ansible peuvent rester la voie de référence pour les VMs aussi longtemps que ce monde reste important dans notre parc.

#### Pourquoi pas Crossplane + Kratix dès maintenant ?

L'équipe ne connaît aujourd'hui ni Crossplane ni Kratix. Démarrer avec les deux simultanément doublerait la courbe d'apprentissage sans bénéfice immédiat, alors que notre parc actuel (majoritairement VM) n'a pas un besoin urgent de la réconciliation continue fine de Crossplane. En effet, Kratix + Rundeck couvre déjà ce besoin de façon suffisament mature. Introduire Crossplane au rythme de la bascule Kube/Cloud, plutôt que dès le départ, permet de concentrer l'effort d'apprentissage là où il rapporte le plus immédiatement.

#### Pourquoi pas Crossplane seul ?

Deux raisons spécifiques à notre contexte. D'abord, Crossplane seul ne gère pas nativement les workflows organisationnels (approbation humaine, différenciation par environnement), qui nécessiteraient un outil externe. Ensuite, et surtout : le monde VM est encore très important chez nous, et la voie Crossplane pour ce monde (`provider-ansible`) est plus jeune et moins éprouvée que nos outils Rundeck/Ansible. Ainsi, démarrer avec Crossplane reviendrait à fragiliser notre socle le plus utilisé aujourd'hui pour gagner en rigueur sur les mondes Kube et Cloud, ce qui est un choix assez fort à prendre.

#### Pourquoi pas Backstage seul ?

Avec un grand nombre d'équipes à servir, l'absence d'enforcement côté serveur rend cette solution inadaptée à terme pour les trois mondes. Elle peut servir de point de départ pour travailler le formulaire et les templates, mais ne doit pas être envisagée comme solution finale.

## Périmètre volontairement restreint à Kube et Cloud

La trajectoire ci-dessus traite le monde VM comme un objectif central de la plateforme. Mais si le choix est fait d'élaborer le Golden Path uniquement autour de Kubernetes et du Cloud (en laissant donc le monde VM hors périmètre), le raisonnement change et la balance penche plus vers Crossplane.

L'argument le plus structurant en faveur de Kratix était sa capacité à orchestrer n'importe quel outil existant pour traiter des mondes hétérogènes sans dépendre de la maturité d'un Provider. Cet avantage perd donc une grande partie de sa pertinence. En effet, cet argument tirait sa force du besoin de piloter notre chaîne Ansible/Rundeck depuis un mécanisme unique. Si le monde VM sort du périmètre, il ne reste plus que Kube et Cloud à couvrir, deux mondes où Crossplane dispose justement de Providers matures et officiellement maintenus (Kubernetes natif, AWS, GCP, ...), sans la réserve qui s'appliquait à `provider-ansible`. La réconciliation continue fine de Crossplane redevient alors un atout disponible nativement sur l'intégralité du périmètre retenu.

Cela ne disqualifie pas Kratix pour autant : son apport sur les workflows organisationnels (approbation humaine en production, différenciation des pipelines par environnement, vérification de quotas) reste entièrement valable et n'est pas remis en cause par ce nouveau périmètre. Crossplane seul ne couvre toujours pas nativement ce besoin.

Avec ce périmètre réduit, deux trajectoires deviennent alors "pertinentes", et le choix entre elles dépend surtout de ce qui est jugé le plus urgent à sécuriser :

- Démarrer par Crossplane si la priorité immédiate est d'obtenir un enforcement et une réconciliation continue solides sur les ressources Kube et Cloud, en acceptant dans un premier temps une gouvernance plus simple (validation de schéma uniquement, approbation humaine gérée hors plateforme ou via un outil externe comme une étape de pipeline CI/CD classique). Kratix viendrait ensuite enrichir la couche de gouvernance une fois ce socle posé.
- Démarrer par Kratix, comme dans la recommandation initiale, si la validation humaine en production et la différenciation des environnements de test sont jugées prioritaires dès le lancement, Crossplane venant ensuite renforcer la réconciliation sur Kube puis sur le Cloud.

Compte tenu de notre contrainte déjà actée (validation humaine obligatoire en production) la seconde option (Kratix d'abord, Crossplane en extension) reste la plus cohérente avec nos besoins exprimés, même en restreignant le périmètre à Kube et Cloud. Le bénéfice principal de ce rétrécissement de périmètre n'est donc pas de changer l'ordre d'adoption, mais d'accélérer et de simplifier l'étape d'extension vers Crossplane : celle-ci peut être engagée plus tôt et avec plus de confiance, puisqu'elle ne repose plus que sur des Providers matures (Kube, Cloud), sans la réserve de prudence qui s'appliquait au monde VM via `provider-ansible`.

## Résumé

- Backstage seul n'est pas suffisant. L'équipe aura de plus en plus de mal à tenir la charge de travail au fur et à mesure que la plateforme grandit et que les développeurs arrivent.
- Si on a envie de continuer à utiliser nos outils internes sur le monde VM, qu'on préfère un outil plus simple à mettre en place et qu'une réconciliation en continu non-instantanée nous suffit, on peut privilégier Kratix.
- Si on veut utiliser d'autres outils que ceux déjà en place pour nos VM, que nous souhaitons de la réconciliation en continu instantanée et qu'une complexité opérationnelle plus élevée ne nous dérange pas pour ce que ça apporte, on peut privilégier Crossplane.