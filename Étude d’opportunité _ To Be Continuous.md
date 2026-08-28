# Étude d’opportunité : To Be Continuous

## État des lieux

Nous essayons de plus en plus de créer des **components CI** en interne.
Aujourd'hui, nous avons une bonne dizaine de components CI existants et fonctionnels, et nous comptons en ajouter à court et moyen terme.

Cependant, du fait de la disponibilité des équipes, ces components sont souvent assez "légers" (peu de fonctionnalités supplémentaires par rapport à tout ce qu'il est possible de faire) et difficilement mis à jour.

## To Be Continuous (TBC)

**To Be Continuous** est un projet communautaire mettant en place des components CI. Ces components sont très nombreux (voir la liste dans la partie `Components TBC`, il y en a beaucoup), très complets et régulièrement entretenus par la communauté.

Ainsi, on peut se demander s'il serait pertinent d'intégrer les components CI de To Be Continuous à notre environnement.

---

## Avantages

- **Richesse fonctionnelle :** Les components sont très complets (beaucoup de jobs, beaucoup d'options, ...) et sont déjà bien documentés.
- **Maintenance :** La communauté met régulièrement à jour les components, ce qui nous permet de ne pas avoir à gérer la maintenance des components (en grande partie)
- **Bonnes pratiques :** Chaque component intègre, en plus de sa fonctionnalité principale, les bonnes pratiques DevSecOps (Compilation, Livraison logicielle, Déploiement, Sécurité (SAST, Dependency Check, ...), Tests, ...)
- **Cohérence :** (Dans notre cas, je sais pas si c'est vraiment un avantage propre à TBC) Les components ont la même architecture : Mêmes stages, mêmes types d'environnements, etc.. Ainsi, il suffit de comprendre l'architecture d'un component pour comprendre celle des autres.
- **Collaboration (?) :** Les components marchent très bien ensemble (Exemple : Kubernetes déploie l'image construite par Docker, qui lui-même récupère les artefacts produits par Maven. SonarQube récupère les rapports de couverture de Maven, ...) `Exemple fourni par l'IA`
- **Accessibilité :** Les components peuvent être inclus avec `project:` et `component:`. `Phrase ajoutée par l'IA :` De plus, les components sont accessibles via le CI/CD Catalog.

## Inconvénients

- **Projet externe :** To Be Continuous est externe à l'INSEE. On dépend donc des choix organisationnels (rythme de mise à jour, évolutions, ...) et techniques (conventions, choix d'architecture, ...) du projet.
- **Hétérogénéité :** Certaines components sont très matures (Python, Helm, ...) tandis que d'autres le sont moins (Rust, ...). Il faut faire attention à la maturité des components que l'on choisit.
- **Sur-engineering :** Les components sont plus complets, mais les jobs sont donc plus complexes et plus nombreux. C'est plus dur d'entrer dedans, de maintenir / améliorer les components, etc. Il faut se poser la question de si c'est utile ou pas.
- **Migration :** Intégrer ces nouveaux components implique de remplacer certaines variables TBC par nos variables internes (ou inversement), de modifier nos CI déjà existantes, d'informer (et former) les équipes sur les nouvelles conventions (stages, ...), etc.
- **Sécurité :** Il faut bien faire attention à n'utiliser que des components vérifiés en interne (notamment, à utiliser une version vérifiée), à utiliser des images Docker internes et pas des images/liens externes (même si, pour ça, notre GitLab a l'air de nous empêcher de le faire), etc.
- `Paragraphe ajouté par l'IA :` **Hypothèses fortes sur le branching/workflow :** TBC impose des conventions assez marquées : la branche main (ou master) est production, la branche develop est intégration, toute autre branche est développement, et le projet recommande explicitement d'éviter Gitflow par défaut. L'adoption peut demander un alignement préalable. 

---

## Components TBC

### Build / Test

| Component      | Usage                                                     |
| -------------- | --------------------------------------------------------- |
| .NET           | Build/test/analyse projets .NET                           |
| Angular        | Build/test/analyse projets Angular                        |
| Bash           | Test et analyse de scripts shell                          |
| dbt            | Intégration/déploiement de pipelines de données dbt       |
| GitLab Package | Publication d'artefacts génériques sur le registre GitLab |
| GNU Make       | Pipelines basés sur Makefile                              |
| Go             | Build/test/analyse projets Go                             |
| Gradle         | Build/test/analyse projets Gradle                         |
| Maven          | Build/test/analyse projets Maven                          |
| MkDocs         | Build de sites de documentation statiques                 |
| Node.js        | Build/test/analyse projets JS/TypeScript/Node             |
| PHP            | Build/test/analyse projets PHP                            |
| pre-commit     | Exécution des hooks pre-commit en CI                      |
| Python         | Build/test/analyse projets Python                         |
| Rust           | Build/test/vérification projets Rust                      |
| Scala/SBT      | Build/test/analyse projets sbt                            |
| Sphinx         | Build de documentation Sphinx                             |
| Zola           | Build/test/vérification de sites Zola                     |

Pour nous : Python, Maven et Java

### Analyse de code

| Component                | Usage                                                                |
| ------------------------ | -------------------------------------------------------------------- |
| DefectDojo               | Import de rapports de sécurité dans DefectDojo                       |
| Dependancy Track         | Gestion du risque de la chaîne d'approvisionnement logicielle (SBOM) |
| GitLeaks                 | Détection de secrets codés en dur dans le repo Git                   |
| MobSF                    | Pentest/analyse de sécurité d'applications mobiles                   |
| OSS Review Toolkit (ORT) | Conformité des dépendances open source (licences)                    |
| SonarQube                | Inspection continue de la qualité du code                            |
| Spectral                 | Lint de documents JSON/YAML (OpenAPI, AsyncAPI)                      |
| SQLFluff Lint            | Lint de fichiers SQL                                                 |

Pour nous : GitLeaks, SonarQube et Dependancy Track (?)

### Packaging

| Component               | Usage                                                            |
| ----------------------- | ---------------------------------------------------------------- |
| Cloud Native Buildpacks | Transformation du code source en images sans Dockerfile          |
| Debian                  | Build de paquets Debian (.deb)                                   |
| Docker                  | Build/test/sécurisation d'images Docker à partir d'un Dockerfile |
| RPM                     | Build de paquets RPM                                             |
| Source-to-Image         | Build d'images container reproductibles depuis le code source    |

Pour nous : Docker

### Packaging

| Component | Usage                                   |
| --------- | --------------------------------------- |
| Terraform | Gestion d'infrastructure avec Terraform |

Pour nous : Terraform

### Déploiement / Run

| Component           | Usage                                                      |
| ------------------- | ---------------------------------------------------------- |
| Amazon Web Services | Déploiement vers AWS                                       |
| Ansible             | Provisioning/déploiement avec Ansible                      |
| Azure               | Déploiement vers Azure                                     |
| Cloud Foundry       | Déploiement vers une plateforme Cloud Foundry              |
| Docker Compose      | Déploiement via Docker Compose                             |
| GitOps              | Déclenchement de déploiement GitOps depuis la pipeline     |
| Google Cloud        | Déploiement vers GCP                                       |
| Helm                | Build de charts Helm et/ou déploiement Kubernetes via Helm |
| Helmfile            | Déploiement Kubernetes via Helmfile                        |
| Kubernetes          | Déploiement via configuration déclarative ou Kustomize     |
| Openshift           | Déploiement vers une plateforme OpenShift                  |
| S3                  | Déploiement d'objets vers un stockage compatible S3        |

Pour nous : Helm et Kubernetes. Probablement S3 et GitOps. Peut-être AWS, Azure et GCP ?

### Tests post-déploiement

| Component       | Usage                                      |
| --------------- | ------------------------------------------ |
| Bruno           | Tests API automatisés avec Bruno           |
| Cypress         | Tests web automatisés                      |
| Hurl            | Tests HTTP automatisés                     |
| k6              | Tests de charge automatisés                |
| Lighthouse      | Analyse de performance web (Lighthouse CI) |
| Playwright      | Tests web automatisés                      |
| Postman         | Tests API automatisés                      |
| Puppeteer       | Tests web automatisés                      |
| Robot Framework | Tests automatisés génériques               |
| Test SSL        | Vérification de la conformité TLS/SSL      |

### Autres

| Component        | Usage                                          |
| ---------------- | ---------------------------------------------- |
| GitLab Butler    | Nettoyage automatisé des projets GitLab        |
| Renovate         | Automatisation des mises à jour de dépendances |
| semantic-release | Versioning et gestion de release automatisée   |

---

## Comment intégrer un component en interne ?

Les modifications détaillées ici se basent sur l'expérience que j'ai eu en intégrant le component TBC **Maven**.
Pour d'autres components qui seraient moins matures / documentés, plus complexes ou utilisant plus de références extérieures, la difficulté d'intégration peut significativement changer.

### Adapter le nom des stages

Dans un premier temps, il faut penser à adapter le nom des stages. En particulier, il faut harmoniser les stages entre : 

- Le component en lui-même
- La CI qui utilise le component
- Les éventuels components utilisés au sein du component

Cette étape est très rapide en pratique, et les messages d'erreur en cas de mauvais nom de stage sont explicites dans le pire des cas.

### Remplacer les images/liens externes

Les components utilisent des images et des liens publics. Or, nos components seront stockés sur notre GitLab interne et n'auront pas accès à ces contenus.

Il faut alors : 

- Retrouver les mentions de ces contenus externes dans le projet du component
- Trouver les alternatives à ces contenus externes
- Remplacer les contenus externes par les alternatives

La première partie (Retrouver les contenus externes) peut être assez pénible en fonction des cas.
Typiquement, dans le cas du component Maven, j'ai mis du temps à comprendre comment empêcher la pipeline d'aller chercher les vulnérabilités sur un lien externe (finalement, l'ajout du paramètre `-DknownExploitedEnabled=false` dans `features.dependency-check.MAVEN_DEPENDENCY_CHECK_ARGS` dans le fichier `kicker.json` a résolu ce problème ... C'était long)

La suite est assez rapide dès qu'on sait quoi utiliser pour remplacer.

Cette étape est, pour moi, la plus compliqué et chronophage car chaque component est différent et nécessite donc un nouveau travail de recherche.

En revanche, une fois que l'on sait comment résoudre ces problèmes dans un component, la résolution pour les autres components est bien plus rapide (typiquement, mon incompréhension du rôle du fichier `kicker.json` est probablement ce qui m'a fait perdre le plus de temps).

### Autres problèmes mineurs

Je liste ici les quelques problèmes que j'ai rencontré. Ceux-ci ne sont pas forcément des éléments propres à To Be Continuous, mais ce sont aussi des erreurs que j'ai rencontré : 

- Créer un fichier `templates/gitlab-ci-maven/template` en plus du fichier `templates/gitlab-ci-maven.yml` de base. Et répercuter les changements d'un fichier dans l'autre.
- Penser à publier et créer un nouveau tag pour notre component quand on change quelque chose ...
- Penser à utiliser le nouveau tag dans la pipeline CI de test ...

### Temps estimé

J'ai personnellement mis 2 jours de travail pour faire en sorte que le component soit complètement fonctionnel.
Cette durée inclut le temps mis à découvrir le code du component, à l'inclure dans ma pipeline Ci de test et à régler tous les problèmes évoqués ci-dessus (y compris ceux liés au fait que je ne suis pas familier avec les CI).

Ainsi, pour un agent connaissant bien les CI de manière générale et ayant connaissance des problèmes classiques rencontrés, **j'estimerais la durée nécessaire pour rendre un component To Be Continuous fonctionnel en interne à 1 jour de travail**. (Cette durée est, à mon avis, surestimée, mais je préfère prendre large)

## Avis général

Au vu des avantages et inconvénients présentés ci-dessus ainsi que de la démarche d'intégration d'un component TBC en interne, je pense qu'il serait très intéressant d'envisager une intégration des components TBC en interne.

En effet, les efforts nécéssaires à l'intégration de ces components sont largement compensés par la richesse qu'ils apportent et par le fait qu'ils sont mis à jour très régulièrement.

Dans notre cas (et de ce que je sais), environ une dizaine de components nous intéresse réellement et ceux-ci sont parmi les plus importants de TBC (important dans le sens où ils sont très utilisés, et par conséquent très documentés et régulièrement mis à jour).