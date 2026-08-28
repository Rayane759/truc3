# Etude d'opportunité : Crossplane VS Kratix

## Utilisation de l'IA

Pour cette étude, j'ai utilisé l'IA pour relire le document ci-dessous. Si des phrases ou paragraphes ont été modifiés/corrigés par l'IA, les blocs de texte concernés seront notifiés de la manière suivante : `Paragraphe étoffé par l'IA`

Dans certains cas, des paragraphes entiers ont été rédigés par l'IA (c'est notamment le cas dans la section "Questions"). Ceux-ci seront alors notifiés de la manière suivante : `Paragraphe ajouté par l'IA`

## Objectif

Dans ce document, nous allons essayer de déterminer la meilleure solution à adopter pour notre Golden Path de configuration d'application.

Ce Golden Path doit permettre aux développeurs de facilement déployer leur application, de modifier la configuration de leur application, etc.

## Critères

Le choix final pourra se baser sur plusieurs critères tels que : 

- **Facilité de mise en place :**  La facilité avec laquelle l'équipe plateforme peut mettre en place cette solution (coût d'entrée technique, coordination de la solution avec d'autres outils internes, création des ressources en cas de besoin, ...)
- **Expérience utilisateur :** La facilité avec laquelle un développeur peut déployer ou modifier la configuration de son application avec cette solution (abstraction technique, gardes-fou, interface, ...)
- **Performance :** Capacité de la solution à déployer une application / modifier la configuration d'une application (temps nécessaire à un développeur pour réaliser une action, ...)
- **Maintenance & Mise à jour :** La facilité avec laquelle l'équipe plateforme peut maintenir cette solution en conditions opérationnelles et de sécurité, ou faire évoluer la solution
- **Support :** Capacité de l'équipe plateforme à répondre aux besoins/demandes des développeurs en adoptant cette solution
- **Accessibilité :** Niveau technique requis dans l'équipe plateforme en adoptant cette solution

## Cas étudié

Dans ce document, nous allons étudier le cas suivant : 

*Un développeur peu familier avec Kubernetes a déployé son application, à l'aide du Golden Path, dans un environnement de Développement sur Kubernetes. Quelques mois plus tard, il souhaite modifier la configuration de son application afin de la passer dans un environnement de Production (toujours sur Kubernetes).*
*Ces modifications suggèrent alors plusieurs modifications : Ressources allouées, Nombre de replicas, Exposition réseau, Sécurité, ..., ainsi qu'un changement d'environnement (Développement -> Production) qui implique donc des exigences / vérifications supplémentaires.*

Pour répondre à ce cas d'usage, nous avons envisagé 4 solutions : 

- **Solution 1 :** Backstage seul
- **Solution 2 :** Crossplane
- **Solution 3 :** Kratix
- **Solution 4 :** Crossplane + Kratix

## Vocabulaire

Dans cette section, nous allons définir certains termes utilisés dans la suite de ce document pour mieux comprendre le fonctionnement des différentes solutions.

### Crossplane

Crossplane est un framework qui transforme un cluster Kubernetes en un control plane d'infrastructure. Il permet de définir et de gérer des ressources cloud (bases de données, buckets, réseaux...) et Kubernetes via des objets Kubernetes déclaratifs, en maintenant en permanence l'état réel conforme à l'état déclaré.

Crossplane repose sur trois concepts fondamentaux : les XRDs, les Compositions, et les XRs.

#### XRD : Composite Resource Definition

Une XRD est la définition du schéma de l'API exposée aux développeurs. Elle décrit quels champs existent, quels types ils acceptent, et quelles valeurs sont autorisées. Elle est écrite une fois par l'équipe plateforme et n'évolue pas souvent.

En pratique, une XRD crée un nouveau type d'objet Kubernetes (une Custom Resource) que les développeurs peuvent ensuite instancier.

```yaml
# Squelette d'une XRD Crossplane
apiVersion: apiextensions.crossplane.io/v1
kind: CompositeResourceDefinition
metadata:
  name: myapps.platform.company.io
spec:
  group: platform.company.io
  names:
    kind: MyApp          # nom du type d'objet créé
    plural: myapps
  versions:
    - name: v1alpha1
      served: true
      referenceable: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                env:
                  type: string
                  enum: [dev, staging, production]   # seules ces valeurs sont acceptées
                replicas:
                  type: integer
                  minimum: 1
                  maximum: 10
                resources:
                  type: string
                  enum: [small, medium, large]
                expose:
                  type: string
                  enum: [internal, public]
              required: [env, replicas, resources]   # champs obligatoires
```

Tout objet `MyApp` ne respectant pas ce schéma sera rejeté immédiatement par Kubernetes au moment de l'`apply`, avant même que Crossplane ne le traite.

#### Composition

La Composition décrit comment Crossplane doit traduire une XR (instance de MyApp) en ressources réelles. C'est ici qu'il y a toute la logique technique : mapping des valeurs, création des ressources Kubernetes ou cloud, application des politiques de production, etc.

Une Composition peut créer autant de ressources que nécessaire à partir d'une seule XR : Deployment, Network Policy, Ingress, bucket S3, etc.

`Paragraphe ajouté par l'IA`
Depuis Crossplane v1.17, les Compositions utilisent le mode Pipeline comme standard. La logique de composition est exprimée via des Composition Functions : des plugins (officiels ou custom) appelés en séquence, chacun recevant et enrichissant l'état désiré avant de le passer au suivant.

```yaml
# Squelette d'une Composition Crossplane
apiVersion: apiextensions.crossplane.io/v1
kind: Composition
metadata:
  name: myapp-production
spec:
  compositeTypeRef:
    apiVersion: platform.company.io/v1alpha1
    kind: MyApp # Cette Composition s'applique aux objets MyApp
  mode: Pipeline
  pipeline:

    # Étape 1 : patch-and-transform (Function officielle Crossplane)
    # Gère le mapping des valeurs XR → ressources composées
    - step: patch-and-transform
      functionRef:
        name: function-patch-and-transform
      input:
        apiVersion: pt.fn.crossplane.io/v1beta1
        kind: Resources
        resources:

          # Ressource 1 : le Deployment Kubernetes
          - name: deployment
            base:
              apiVersion: apps/v1
              kind: Deployment
              spec:
                template:
                  spec:
                    containers:
                      - name: app
                        resources:
                          requests:
                            cpu: "500m"
                            memory: "512Mi"
            patches:
              # Injecter le nombre de réplicas depuis la XR
              - type: FromCompositeFieldPath
                fromFieldPath: spec.replicas
                toFieldPath: spec.replicas

          # Ressource 2 : le PodDisruptionBudget
          - name: pdb
            base:
              apiVersion: policy/v1
              kind: PodDisruptionBudget
              spec:
                minAvailable: 2

          # Ressource 3 : la Network Policy
          - name: network-policy
            base:
              apiVersion: networking.k8s.io/v1
              kind: NetworkPolicy
              spec:
                podSelector: {}
                policyTypes: [Ingress, Egress]
                # règles restrictives de production...

    # Étape 2 (optionnel) : Function custom pour la logique complexe
    # ex. calcul conditionnel des resource limits selon spec.resources
    - step: compute-resource-limits
      functionRef:
        name: function-company-resource-limits
```

#### XR : Composite Resource

La XR est l'instance créée par le développeur (ou par le pipeline Kratix dans la solution 4). C'est l'objet concret qui exprime la configuration souhaitée. Crossplane détecte sa création ou sa modification et déclenche la réconciliation vers les ressources définies dans la Composition.

```yaml
# Exemple de XR (objet app.yaml dans le repo du développeur)
apiVersion: platform.company.io/v1alpha1
kind: MyApp
metadata:
  name: my-service
spec:
  env: production
  replicas: 3
  resources: medium
  expose: public
```

#### Provider

Un Provider est un plugin Crossplane qui lui permet de gérer des ressources sur une plateforme spécifique (AWS, GCP, ...).

```yaml
# Installation d'un Provider (exemple : provider-aws)
apiVersion: pkg.crossplane.io/v1
kind: Provider
metadata:
  name: provider-aws
spec:
  package: xpkg.upbound.io/upbound/provider-aws:v1.0.0
```

#### Réconciliation continue

La réconciliation continue est le processus par lequel Crossplane surveille en permanence l'état réel des ressources qu'il gère et le compare à la XR (état désiré). Toute divergence (modification manuelle sur le cluster, suppression accidentelle d'une ressource, dérive de configuration) est détectée et corrigée automatiquement par Crossplane.

### Kratix

Kratix est un orchestrateur de plateforme qui se concentre sur la définition et l'exécution de workflows : des étapes qui peuvent inclure des validations techniques ou humaines, des appels à des APIs externes,la génération de manifeste, etc.

Kratix se repose sur deux concepts fondamentaux : les Promises et le State Store.

#### Promise

Les Promises sont au centre de Kratix. Elles définissent :

- Le schéma de l'API exposée aux développeurs (ce qu'ils peuvent demander), sous la forme d'un CustomResourceDefinition Kubernetes embarqué
- Le pipeline de workflow exécuté à chaque demande (ce qu'il se passe après la demande)

Une Promise est composée de trois parties : la définition de l'API (`spec.api`), les règles de scheduling (`spec.destinations`, sur quel cluster déployer) et les workflows (`spec.workflows`).

Kratix dispose de deux types de workflows :

- `workflows.promise` : exécuté lors du cycle de vie de la Promise elle-même (installation, mise à jour, suppression sur le cluster plateforme). Permet par exemple d'installer des dépendances ou d'enregistrer la Promise dans un catalogue.
- `workflows.resource` : exécuté à chaque ResourceRequest soumise par un développeur. C'est ici que réside la logique métier : validation, génération de manifestes, notifications, etc.

```yaml
# Squelette d'une Promise Kratix
apiVersion: platform.kratix.io/v1alpha1
kind: Promise
metadata:
  name: myapp
  labels:
    kratix.io/promise-version: v0.1.0

spec:

  # Partie 1 : API exposée aux développeurs
  # spec.api contient un CustomResourceDefinition Kubernetes standard embarqué
  api:
    apiVersion: apiextensions.k8s.io/v1
    kind: CustomResourceDefinition
    metadata:
      name: myapps.platform.company.io
    spec:
      group: platform.company.io
      names:
        kind: MyApp
        plural: myapps
        singular: myapp
      scope: Namespaced
      versions:
        - name: v1alpha1
          served: true
          storage: true
          schema:
            openAPIV3Schema:
              type: object
              properties:
                spec:
                  type: object
                  properties:
                    env:
                      type: string
                      enum: [dev, staging, production]
                    replicas:
                      type: integer
                    resources:
                      type: string
                      enum: [small, medium, large]

  # Partie 2 : workflows
  workflows:

    # Cycle de vie de la Promise (installation, mise à jour de la Promise elle-même)
    promise:
      configure:
        - apiVersion: platform.kratix.io/v1alpha1
          kind: Pipeline
          metadata:
            name: install-dependencies
          spec:
            containers:
              - name: setup
                image: company-registry/promise-setup:v1.0.0

    # Cycle de vie de chaque ResourceRequest soumise par un développeur
    resource:
      configure:
        - apiVersion: platform.kratix.io/v1alpha1
          kind: Pipeline
          metadata:
            name: myapp-pipeline
          spec:
            containers:
              # Étape 1 : validation des inputs métier
              - name: validate
                image: company-registry/validate-app:v1.2.0

              # Étape 2 : vérification des quotas et politiques
              - name: check-policies
                image: company-registry/check-policies:v1.0.0

              # Étape 3 : demande d'approbation humaine (voir note ci-dessous)
              - name: request-approval
                image: company-registry/request-approval:v1.0.0

              # Étape 4 : génération des manifestes finaux
              - name: generate-manifests
                image: company-registry/generate-manifests:v1.1.0
```

Chaque étape est un conteneur Docker développé par l'équipe plateforme. Il reçoit en entrée la ResourceRequest soumise par le développeur et peut lire/modifier un dossier de sortie qui sera écrit dans le State Store.

`Paragraphe ajouté par l'IA`
Note sur l'approbation humaine : 
Kratix ne propose pas de mécanisme d'approbation "out of the box". Le pattern consiste à écrire un fichier `/kratix/metadata/workflow-control.yaml` depuis un conteneur du pipeline, avec `suspend: true` (et un message optionnel), ce qui met le workflow en pause jusqu'à ce qu'une action externe (suppression du label `kratix.io/workflow-suspended`, ou réconciliation manuelle) le relance. L'implémentation de la notification (email, Tchap, ticket...) et de l'interface de validation reste à la charge de l'équipe plateforme.

```yaml
> # Exemple de fichier écrit par le conteneur "request-approval"
# pour mettre le pipeline en pause
# /kratix/metadata/workflow-control.yaml
suspend: true
message: "Approbation requise par le tech lead avant passage en production"
```

#### Conteneur de pipeline

Chaque step d'une Promise est un conteneur autonome. Le SDK Python de Kratix (disponible depuis août 2025, actuellement en version 0.4.x, il faut regarder si c'est assez mature pour nous) permet d'écrire ces steps sans manipuler directement les fichiers de système de Kratix.

Le SDK repose sur un modèle simple : Kratix monte la ResourceRequest dans `/kratix/input/object.yaml`, et le conteneur écrit ses sorties (manifestes générés, sélecteurs de destination, statut) dans des répertoires montés en sortie. Le SDK abstrait ces lectures/écritures de fichiers.

```python
# Exemple de step de validation (SDK Python Kratix v0.4.x)
import sys
import kratix_sdk as ks

def main():
    sdk = ks.KratixSDK()
    resource = sdk.read_resource_input()  # lit /kratix/input/object.yaml

    env = resource.get_value("spec.env")
    replicas = resource.get_value("spec.replicas")
    resources_size = resource.get_value("spec.resources")

    errors = []

    # Règle 1 : minimum 2 réplicas en production
    if env == "production" and replicas < 2:
        errors.append("Au moins 2 réplicas sont requis en production.")

    # Règle 2 : profil 'small' interdit en production
    if env == "production" and resources_size == "small":
        errors.append("Le profil 'small' n'est pas autorisé en production.")

    if errors:
        # Écriture du statut d'erreur lisible par le développeur
        status = ks.Status({"message": " | ".join(errors), "state": "ValidationFailed"})
        sdk.write_status(status)
        sys.exit(1)  # exit code non-zéro = pipeline en échec

    # Validation réussie : exit code 0 implicite

if __name__ == "__main__":
    main()
```

#### ResourceRequest

La ResourceRequest est l'objet soumis par le développeur (ou par Backstage) pour déclencher le pipeline d'une Promise.

C'est un peu comme la XR Crossplane d'un point de vue pratique, mais le mécanisme de réconciliation est différent. Alors que Crossplane surveille en continu l'état réel des ressources et corrige toute dérive immédiatement, Kratix rejoue son pipeline à intervalle régulier (toutes les 10 heures par défaut, modifiable). Cette réconciliation Kratix regénère les manifestes dans le State Store si nécessaire. Ensuite, c'est ArgoCD qui synchronise le cluster. La source de vérité est donc le repo Git (State Store), et non la ResourceRequest elle-même.`

```yaml
# Exemple de ResourceRequest générée par Backstage
apiVersion: platform.company.io/v1
kind: MyApp
metadata:
  name: my-service
  namespace: my-team
spec:
  env: production
  replicas: 3
  resources: medium
  expose: public
```

#### State Store

Le State Store est l'espace de stockage où Kratix écrit les manifestes générés par ses pipelines. Il peut s'agir d'un repo Git dans notre cas, mais ça peut être un bucket S3 aussi. C'est la source de vérité de Kratix : tout ce qui est écrit dans le State Store sera ensuite appliqué sur les clusters cibles par ArgoCD.

#### GitOps + ArgoCD

Le modèle GitOps repose sur le principe que le repo Git est la source de vérité de l'infrastructure : tout changement sur un cluster passe par un commit dans Git, et un agent surveille ce repo en permanence pour maintenir le cluster conforme à son contenu.

Pour nous, c'est ArgoCD. Il surveille un repo Git et applique automatiquement tout changement détecté. Il assure également la réconciliation continue entre le cluster et le contenu du repo.


## Solution 1 : Backstage seul

### Expérience développeur

Le développeur va sur Backstage, sur son application, et clique sur le bouton "Modifier la configuration".

Un formulaire s'ouvre, similaire à celui du Golden Path, lui proposant donc les mêmes champs : 

- Environnement : dev (Il sélectionne production)
- ...

Il valide les champs du formulaire, et Backstage génère les fichiers modifiés et ouvre une MR sur le repo.

La MR est relue et validée par un pair ou un tech lead. C'est l'unique vérification humaine de cette solution. De plus, il n'existe aucun enforcement technique côté serveur. La pipeline CI/CD se déclenche ensuite au merge et la nouvelle configuration est appliquée.

### Expérience équipe plateforme (Ce qu'elle fait, ce qu'elle met en place, ...)

L'équipe plateforme doit créer les templates Backstage pour chaque type d'application. Ces templates indiquent les champs à remplir, les valeurs acceptables, etc. pour générer les fichiers de configuration.

Par ailleurs, l'équipe plateforme doit également maintenir et mettre à jour ces templates ainsi que la pipeline CI/CD qui déclenche le `helm upgrade` après chaque MR validée.

Enfin (même si c'est le cas pour toutes les solutions), il faut maintenir et mettre à jour Backstage en lui-même.


## Solution 2 : Crossplane

### Expérience Développeur

Le développeur va sur Backstage, sur son application, et clique sur le bouton "Modifier la configuration". Un formulaire s'ouvre, similaire à celui du Golden Path, lui proposant les mêmes champs. Backstage génère alors le fichier app.yaml mis à jour dans son repo Git.

Ce fichier app.yaml est une XR Crossplane simplifiée, qui ressemble à ça :

```yaml
# Fichier app.yaml — XR Crossplane (généré par Backstage)
apiVersion: platform.company.io/v1alpha1 # Groupe défini dans la XRD
kind: MyApp # Type défini dans la XRD
metadata:
  name: my-service
spec:
  env: production
  replicas: 3
  resources: medium
  expose: public
```

Les champs sont assez explicites, le développeur peut les lire et les vérifier facilement avant de soumettre.
De plus, en cas d'erreur de schéma (mauvais type, valeur non prévue, champ obligatoire manquant), Crossplane rejette la modification et en informe le développeur.

Le développeur valide ses changements, Backstage ouvre une MR. Celle-ci est relue rapidement car les champs sont simples et lisibles. Une fois mergée, la pipeline CI/CD applique le fichier via `kubectl apply`. C'est à ce moment là que Kubernetes valide le fichier par rapport au schéma de la **XRD** et rejette immédiatement toute valeur invalide (mauvais type, valeur non autorisée, champ obligatoire manquant), avant même que Crossplane ne traite la demande.

### Ce que fait la plateforme

Une fois le `app.yaml` appliqué sur le cluster, Kubernetes enregistre la **XR**.
Crossplane détecte la nouvelle **XR** et consulte la **Composition** associée au type `MyApp` (définie par l'équipe plateforme). C'est à l'intérieur de cette Composition que les règles propres à chaque environnement sont appliquées.
Par exemple, pour `env: production` :

- resources: medium → traduit en 
    - requests: {cpu: 500m, memory: 512Mi},
    - limits: {cpu: 1, memory: 1Gi}
- replicas: 3 → 
    - Deployment à 3 réplicas
    - Création d'un PodDisruptionBudget (min 2 disponibles)
- env: production → 
    - Network Policy plus restrictive
    - Monitoring
    - ...
- expose: public → 
    - Ingress
    - Certificat

Enfin, Crossplane fait de la **Réconciliation continue** : Elle compare en permanence la configuration réelle à la **XR**. Ainsi, si la configuration est modifiée manuellement par un développeur, Crossplane le remettra à l'état attendu automatiquement.

### Expérience équipe plateforme (Ce qu'elle met en place, ...)

L'équipe plateforme doit : 

- Créer et maintenir les templates Backstage (formulaire de modification, action qui génère le fichier app.yaml et ouvre la MR)
- Rédiger les XRD et les Compositions pour chaque type d'application
- Configurer les Providers (Kubernetes, AWS, ...)
- Mettre en place et maintenir la pipeline CI/CD qui applique le fichier app.yaml sur le cluster
- Gérer les maintenances + mises à jour de Crossplane, des XRD et des Compositions

## Solution 3 : Kratix

### Expérience Développeur

Le développeur va sur Backstage, sur son application, et clique sur le bouton "Modifier la configuration".
Un formulaire s'ouvre, similaire à celui du Golden Path, lui proposant les mêmes champs :

- Environnement : dev (Il sélectionne production)
- ...

Il valide les champs du formulaire. Backstage soumet la demande au cluster plateforme sous la forme d'une **ResourceRequest** Kratix.

Le pipeline se met alors en pause en attente d'approbation. Le leader technique reçoit une notification (par Tchap, email, voire Backstage !) et valide la demande via l'interface prévue à cet effet. Une fois approuvée, la nouvelle configuration est automatiquement appliquée sur le cluster cible. Le développeur reçoit une confirmation.

### Ce que fait la plateforme

Kratix reçoit la ResourceRequest et déclenche le pipeline de la Promise associée au type d'application. Ce pipeline s'exécute en plusieurs étapes :

- Validation des inputs : Vérification que les valeurs soumises respectent les règles définies (ex : `replicas >= 2` en production, `resources: small` interdit en production, ...). En cas d'échec, le pipeline s'arrête et le développeur est notifié avec un message explicite.
- Vérification organisationnelle : Vérification des quotas de l'équipe, des règles de sécurité, etc.
- Approbation humaine : La pipeline se met en pause et notifie le leader technique. Le déploiement ne reprend qu'après validation.
- Génération des charts : La pipeline génère les charts finaux (charts Helm, Network Policy, PodDisruptionBudget, Monitoring, ...) en appliquant les exigences de production.
- Écriture dans le **State Store** : Les charts générés sont poussés dans le repo Git dédié au cluster cible.

ArgoCD détecte les nouveaux fichiers dans le repo et les applique sur le cluster. 
Par ailleurs, Kratix rejoue lui-même les pipelines de chaque ResourceRequest à intervalle régulier (toutes les 10 heures par défaut) : si une dérive a eu lieu dans le State Store, les manifestes sont régénérés et ArgoCD re-synchronise le cluster en conséquence.

### Expérience équipe plateforme (Ce qu'elle met en place, ...)

L'équipe plateforme doit :

- Créer et maintenir les templates Backstage (formulaire de soumission, action Scaffolder qui soumet la ResourceRequest au cluster plateforme)
- Rédiger les **Promises** pour chaque type d'application (schéma de la ResourceRequest + pipeline de workflow)
- Développer les conteneurs de pipeline implémentant les étapes de validation, de vérification des politiques, d'approbation et de génération de manifestes
- Implémenter le mécanisme d'approbation : notification du responsable et interface de validation (webhook, action Backstage, etc.)
- Configurer le **State Store** et les **Destinations** (clusters cibles)
- Configurer ArgoCD sur chaque cluster cible
- Gérer les maintenances + mises à jour de Kratix, des **Promises** et des conteneurs de pipeline

## Solution 4 : Crossplane + Kratix

### Expérience Développeur

L'expérience développeur est identique à celle de la solution 3 : le développeur remplit le formulaire Backstage, soumet sa demande, attend l'approbation, puis reçoit une confirmation une fois la configuration appliquée.

### Ce que fait la plateforme

Le pipeline Kratix s'exécute de la même manière que dans la solution 3 : validation des inputs, vérification des politiques, approbation humaine. La différence réside dans l'étape de génération.

Au lieu de générer des manifestes Kubernetes bruts, le pipeline Kratix génère une **XR** Crossplane et l'écrit dans le **State Store** : 

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
```

ArgoCD applique cette **XR** sur le cluster plateforme. Crossplane consulte alors la **Composition** associée au type `MyApp` et provisionne l'ensemble des ressources (Deployment, Network Policy, Ingress, ...).

Crossplane assure ensuite la **réconciliation continue** sur ces ressources : une fois la **XR** appliquée sur le cluster, elle devient la source de vérité pour Crossplane. Toute modification manuelle d'une ressource (Deployment, NetworkPolicy, etc.) est automatiquement corrigée par Crossplane sans nécessiter de nouveau commit Git. Le repo Git reste néanmoins la source de vérité de la XR elle-même : c'est ArgoCD qui la maintient sur le cluster, et toute modification de la XR passe par un commit.

Chaque outil joue alors son propre rôle :

- Kratix gère les workflows, les validations métier et l'approbation humaine
- Crossplane gère la réconciliation continue et le provisioning des ressources infrastructure

### Expérience équipe plateforme (Ce qu'elle met en place, ...)

L'équipe plateforme doit assumer la charge des deux solutions précédentes :

- Créer et maintenir les templates Backstage (formulaire de soumission, action Scaffolder)
- Rédiger les **Promises** Kratix (schéma + pipeline) pour chaque type d'application
- Développer les conteneurs de pipeline Kratix
- Implémenter le mécanisme d'approbation (notification + interface de validation)
- Rédiger les **XRD** et **Compositions** Crossplane correspondantes
- Configurer les Providers Crossplane (Kubernetes, AWS, ...)
- Configurer le **State Store** et les Destinations Kratix
- Configurer ArgoCD sur chaque cluster cible
- S'assurer de la cohérence entre les **Promises** Kratix et les **XRD** Crossplane
- Gérer les maintenances + mises à jour de Kratix, Crossplane, des **Promises**, des **XRD** et des **Compositions**

## Détails

### Mise en place 

#### Backstage seul

L'effort se concentre sur la création des Software Templates Backstage : définir les champs du formulaire, les valeurs acceptables, et la logique de génération des fichiers de configuration via des templates. Il faut également configurer les actions du Scaffolder (connexion au repo Git, ouverture de MRs) et mettre en place la pipeline CI/CD qui déclenche `helm upgrade` après le merge.

Tout cela repose sur des outils classiques (Git, Helm, CI/CD) et ne requiert pas de compétences Kubernetes avancées.

#### Crossplane

En plus des Software Templates Backstage, l'équipe doit installer Crossplane via Helm chart dans un namespace dédié, installer et configurer les Providers nécessaires (provider-kubernetes, provider-aws, provider-gcp...) avec leurs credentials et permissions IAM associés, écrire les XRDs (schéma de l'API développeur) et les Compositions (mapping vers les ressources réelles) pour chaque type d'application, et mettre en place le RBAC pour interdire les modifications directes des XRs sur le cluster.

`Paragraphe corrigé et étoffé par l'IA`
La partie la plus exigeante est la conception des Compositions. Depuis Crossplane v1.17, le standard est le mode Pipeline avec des Composition Functions : la logique de mapping est exprimée via des functions (officielles comme `function-patch-and-transform`, ou custom). Ce standard est plus puissant que l'ancien mode `Resources` (déprécié), mais nécessite un apprentissage supplémentaire par rapport à celui-ci. Il faudra attendre plusieurs semaines avant d'avoir une première Composition fonctionnelle en production.

#### Kratix

En plus des Software Templates Backstage, l'équipe doit installer cert-manager (prérequis de Kratix pour ses webhooks internes), installer Kratix sur le cluster plateforme, configurer le State Store (repo Git ou bucket S3 où Kratix écrit les manifestes générés), enregistrer les clusters cibles comme Destinations, et installer ArgoCD ou Flux sur chaque cluster cible pour assurer la synchronisation.

`(Paragraphe corrigé et étoffé par l'IA)`
L'écriture des Promises constitue le cœur du travail : définir le schéma de la ResourceRequest (sous forme de CRD embarqué) et développer les conteneurs de pipeline (validation, vérification des politiques, approbation humaine via le mécanisme suspend, génération des manifestes). La CLI Kratix aide pour les cas simples (wrapper un Helm chart existant), mais les pipelines complexes demandent un vrai effort de développement logiciel. Le SDK Python de Kratix (lancé en août 2025, v0.4.x) réduit la barrière d'entrée pour les équipes déjà familières avec Python, mais reste récent. Les équipes exigeant une maturité maximale en production préféreront le SDK Go. Dans tous les cas, les conteneurs de pipeline doivent être traités comme de vrais projets logiciels : tests, CI/CD pour les images, versioning.

#### Crossplane + Kratix

C'est la somme des deux mises en place précédentes, avec en plus la nécessité de faire fonctionner les deux outils ensemble : les pipelines Kratix doivent générer des XRs Crossplane valides, le RBAC doit être pensé pour les deux couches, et l'équipe doit avoir une vision claire de la responsabilité de chaque outil dès le départ. Le risque principal est de mal délimiter ces responsabilités, ce qui complique ensuite le débogage et la maintenance.

### Expérience utilisateur

#### Backstage seul

Le développeur remplit un formulaire dans Backstage et n'interagit jamais avec des fichiers techniques. Les validations côté formulaire (types, valeurs autorisées, champs obligatoires) évitent les erreurs de saisie. L'expérience est fluide pour les cas couverts par les templates existants.

#### Crossplane

Avec Backstage par-dessus, l'expérience est identique à la solution Backstage seul.

#### Kratix

Formulaire Backstage. Mais la différence visible pour le développeur est l'étape d'approbation humaine : il soumet sa demande et attend la validation avant que la configuration ne soit appliquée.

#### Crossplane + Kratix

Identique à Kratix du point de vue du développeur.

### Performance

#### Backstage seul

Le délai entre la soumission du formulaire et l'application de la configuration dépend principalement du temps de review et de merge de la MR, puis de l'exécution du pipeline CI/CD.

#### Crossplane

`Paragraphe étoffé avec l'IA`
Même délai pour la MR. Une fois la XR appliquée, Crossplane démarre la réconciliation immédiatement. Le provisioning des ressources prend quelques secondes à quelques minutes selon leur nature (ressources Kubernetes locales plus rapides que ressources cloud).

#### Kratix

Le délai dépend du nombre de steps et de la présence d'une étape d'approbation humaine. Hors approbation, un pipeline typique s'exécute en quelques minutes.

#### Crossplane + Kratix

Légèrement plus long que Kratix ou Crossplane seul en théorie, mais la différence est négligeable en pratique.

### Maintenance & Mise à jour

#### Backstage seul

Faire évoluer un Software Template est accessible : modifier un champ, ajouter une valeur à un enum, ajuster un template de fichier. La difficulté principale est la coordination avec les charts Helm templates : toute évolution d'un chart doit être répercutée manuellement dans le template Backstage correspondant. La charge de maintenance augmente avec le nombre de types d'applications.

#### Crossplane

Faire évoluer une XRD sans casser les XRs existantes demande une gestion rigoureuse des versions d'API (`v1`, ...). Crossplane supporte plusieurs versions simultanément, mais cela complexifie les Compositions. 

Les Compositions elles-mêmes peuvent devenir longues et complexes, difficiles à refactoriser sans risque de régression

D'un point de vue Cloud : La mise à jour des Providers cloud peut introduire des changements de comportement sur les ressources existantes et doit être testée avant la production.

#### Kratix

Faire évoluer une Promise est relativement souple, car modifier un step de pipeline n'affecte que les nouvelles demandes. En revanche, modifier le schéma de la ResourceRequest soulève les mêmes problèmes de versioning d'API que Crossplane. La maintenance des conteneurs de pipeline implique de gérer des images Docker, des registres, et des pipelines de build pour ces images. C'est une infrastructure supplémentaire à gérer.

#### Crossplane + Kratix

Toute évolution doit être coordonnée entre les deux outils. Modifier le schéma d'une XRD peut impacter les Promises qui génèrent des XRs conformes à ce schéma. Ainsi, chaque mise à jour nécessite une validation croisée entre les deux outils.

### Support

#### Backstage seul

Les questions portent principalement sur les cas non couverts par les templates existants et sur les échecs de pipeline CI/CD. Quand un déploiement échoue, le message d'erreur remonte directement depuis `helm upgrade` et est souvent peu lisible pour un développeur non-Kubernetes. L'équipe plateforme doit intervenir.

#### Crossplane

`Paragraphe étoffé par l'IA`
Les abstractions XRD réduisent les questions sur les usages classiques. En revanche, quand une XR ne se réconcilie pas, le message d'erreur peut être très difficile à comprendre : il traverse plusieurs couches (controller Crossplane, Provider, API cloud) avant de remonter. L'équipe plateforme doit souvent étudier l'erreur en profondeur pour avoir une explication compréhensible pour le développeur.

#### Kratix

Le formulaire Backstage et les validations dans le pipeline réduisent au minimum les erreurs d'usage. Les messages d'erreur du pipeline sont configurables par l'équipe plateforme : ils peuvent être rendus explicites et compréhensibles. Les questions se concentrent alors sur les cas non couverts par les Promises existantes et sur les demandes bloquées (pipeline en échec, ...).

#### Crossplane + Kratix

Même profil que Kratix du point de vue développeur. En revanche, quand un problème survient, l'équipe plateforme doit investiguer dans deux outils pour identifier la couche en cause, ce qui allonge les délais de résolution.

### Accessibilité 

#### Backstage seul

Backstage (Software Templates, Scaffolder), Helm, Kubernetes basique, CI/CD. Accessible assez rapidement.

#### Crossplane

`Paragraphe étoffé par l'IA`
Kubernetes avancé, modèle mental Crossplane (XRD, Composition, Providers, managed resources, réconciliation), APIs cloud (AWS/GCP/Azure), gestion du RBAC et des credentials. Profil Platform Engineer ou SRE senior avec spécialisation Crossplane — moins courant sur le marché, nécessite généralement une formation dédiée ou une période d'apprentissage significative.

#### Kratix

`Paragraphe étoffé par l'IA`
Kubernetes intermédiaire, développement de conteneurs (Python, Go ou shell), modèle GitOps (ArgoCD ou Flux), Kratix. Profil orienté développement avec une culture infrastructure. Le SDK Python de Kratix réduit la barrière d'entrée pour les équipes déjà familières avec Python. Plus accessible que Crossplane, mais requiert quand même une discipline de développement logiciel (tests, CI pour les images, versioning).

#### Crossplane + Kratix

Besoin des compétences des solutions 2 et 3. Nécessite soit des profils très polyvalents, soit plusieurs personnes aux spécialisations complémentaires au sein de l'équipe plateforme.

### Conception des abstractions

#### Backstage seul

La conception se limite aux Software Templates : quels champs exposer, quelles valeurs autoriser, comment générer les fichiers correspondants. C'est de la modélisation de formulaire, c'est assez accessible. La limite est que ces abstractions n'ont aucun équivalent côté serveur, elles n'existent que dans l'interface.

#### Crossplane

Concevoir une XRD, c'est comme concevoir une API. L'équipe doit décider quels champs exposer, quelles contraintes appliquer, et comment gérer l'évolution du schéma sans casser les applications existantes. La Composition associée doit ensuite mapper chaque combinaison de paramètres vers les ressources réelles, y compris les transitions d'état (que se passe-t-il quand `env` passe de `dev` à `production` sur une ressource existante ?). Ces transitions ne sont pas toujours faciles à modéliser et peuvent nécessiter des Composition Functions pour les cas complexes.

#### Kratix

`Paragraphe étoffé par l'IA`
Concevoir une Promise, c'est concevoir à la fois une API (le schéma) et un workflow (le pipeline). La flexibilité est plus grande qu'avec Crossplane, mais elle impose une discipline : sans bonne conception, les pipelines deviennent des scripts monolithiques difficiles à tester et à maintenir. L'équipe doit structurer ses pipelines de manière modulaire et penser la testabilité dès le départ.

#### Crossplane + Kratix

Deux niveaux d'abstraction à concevoir et à maintenir en cohérence : les Promises Kratix doivent produire des XRs conformes aux XRDs Crossplane. Toute modification d'une XRD peut impacter les Promises qui la ciblent. Cette coordination est un travail permanent qui requiert une vision d'ensemble des deux outils simultanément.

### Débogage

#### Backstage seul
Le débogage est direct : logs du pipeline CI/CD, `kubectl describe`, etc.. Il n'y a pas beaucoup d'étapes et les outils sont familiers. La principale difficulté est d'identifier si un problème vient du template Backstage, de la génération des fichiers, du pipeline CI/CD, ou du cluster.

#### Crossplane

`Paragraphe étoffé par l'IA`
Le débogage d'une réconciliation en échec nécessite de traverser plusieurs couches : état de la XR (`kubectl describe`), events Kubernetes associés, logs du controller Crossplane, état des managed resources intermédiaires, logs du Provider. La chaîne de causalité peut être longue et les messages d'erreur ne sont pas toujours explicites. Crossplane 2.2 a introduit un pipeline inspector pour aider, mais le débogage reste un travail d'expert.

#### Kratix

`Paragraphe étoffé par l'IA`
Le débogage d'un pipeline en échec est plus accessible : logs du conteneur en erreur, inspection du State Store pour vérifier ce qui a été écrit, logs ArgoCD pour vérifier ce qui a été appliqué. Les pipelines étant du code que l'équipe a elle-même écrit, le débogage reste dans un périmètre familier. La chaîne Kratix -> Git -> ArgoCD -> Cluster introduit néanmoins plusieurs points de défaillance potentiels qu'il faut savoir identifier rapidement.

#### Crossplane + Kratix

Le débogage cumule les complexités des deux outils. Un problème peut se situer dans le pipeline Kratix, dans la génération de la XR, dans la réconciliation Crossplane, ou dans l'application par ArgoCD. Identifier rapidement dans quelle couche se situe le problème est la première difficulté, avant même de résoudre le problème lui-même.

### Règles organisationnelles

#### Backstage seul

Les règles organisationnelles (quotas, restrictions par environnement, approbation humaine) peuvent être encodées dans le formulaire Backstage : champs conditionnels, validations croisées, vérification d'une API externe avant soumission, étape d'approbation dans le workflow du template. Ces règles sont efficaces pour les utilisateurs passant par le formulaire, mais restent contournables : elles n'existent que dans l'interface et ne s'appliquent pas si quelqu'un ouvre une MR directement ou fait un `kubectl apply` manuel.

#### Crossplane

Crossplane ne gère que la validation de schéma (types, valeurs autorisées dans la XRD). Les règles organisationnelles complexes (quotas d'équipe, restrictions conditionnelles, approbation humaine, notifications externes, ...) nécessitent l'ajout d'outils externes (comme OPA/Kyverno, encore). Ces outils sont à installer, configurer, et maintenir en plus du reste. Ils offrent un enforcement côté serveur, mais ne supportent pas nativement l'approbation humaine.

#### Kratix

Toutes les règles organisationnelles sont encodées directement dans le pipeline de la Promise, sans outil externe. Un conteneur peut appeler n'importe quelle API, vérifier n'importe quelle condition, et envoyer des notifications. C'est la solution la plus expressive et la plus complète sur cet aspect.

L'approbation humaine est également réalisable via le mécanisme natif de suspension de pipeline : un conteneur écrit un fichier `workflow-control.yaml` avec `suspend: true`, ce qui met le pipeline en pause jusqu'à validation. La notification de l'approbateur et l'interface de validation restent à implémenter par l'équipe plateforme.

#### Crossplane + Kratix

Kratix gère les règles organisationnelles dans son pipeline (comme la solution 3), et Crossplane enforce le schéma en réconciliation continue. Les deux outils fonctionnent bien ensemble et couvrent l'ensemble des besoins sans outil externe supplémentaire.

### Réconciliation continue

#### Backstage seul

Aucune réconciliation continue. Une fois `helm upgrade` exécuté, l'état réel du cluster n'est pas surveillé. Toute dérive (modification manuelle, suppression accidentelle d'une ressource) passe inaperçue jusqu'au prochain déploiement. Il est en revanche possible d'ajouter ArgoCD pour surveiller le repo Git.

#### Crossplane

Crossplane surveille en permanence l'état réel des ressources et le compare à la XR. Toute dérive est détectée et corrigée automatiquement. La XR est la source de vérité, et elle est incontournable si le RBAC est correctement configuré.

#### Kratix

La réconciliation opère sur deux niveaux. D'abord, Kratix lui-même rejoue périodiquement les pipelines de chaque ResourceRequest (toutes les 10 heures par défaut, modifiable), ce qui permet de générer de nouveau les manifestes dans le State Store si une dérive a eu lieu. Ensuite, ArgoCD surveille le repo Git (State Store) et maintient le cluster conforme à son contenu en permanence. Ainsi, toute modification dans le repo est appliquée au cluster dans les minutes qui suivent.

Si quelqu'un pousse directement dans le repo Git en contournant Kratix, ArgoCD appliquera ces changements sans que Kratix ne le sache. Mais au prochain cycle de réconciliation de Kratix, les manifestes seront régénérés et les changements non désirés effacés. La source de vérité reste Git, pas la ResourceRequest.

#### Crossplane + Kratix

Même profil que Crossplane au niveau de la réconciliation continue.

### Enforcement côté serveur

#### Backstage seul

Aucun enforcement côté serveur. Les validations existent uniquement dans le formulaire Backstage. Un contournement du formulaire (MR directe, `kubectl apply` manuel, ...) ne rencontre aucune barrière technique côté cluster.

#### Crossplane

Le schéma de la XRD est "enforced" par Kubernetes à chaque `kubectl apply` : tout objet ne respectant pas le schéma est rejeté immédiatement, quel que soit le vecteur d'entrée. 

`Paragraphe ajouté par l'IA`
Pour les règles métier plus complexes, OPA/Kyverno peut être ajouté pour un enforcement complémentaire.

#### Kratix

Le pipeline de la Promise s'exécute à chaque ResourceRequest, quelle que soit son origine. Les validations métier et organisationnelles du pipeline sont donc systématiquement appliquées. Un contournement nécessiterait d'avoir des droits d'écriture directs sur le cluster plateforme, ce que le RBAC doit interdire.

#### Crossplane + Kratix

Double enforcement : le pipeline Kratix valide les règles organisationnelles, et le schéma XRD Crossplane valide la conformité technique.

### Source de vérité

#### Backstage seul

Les fichiers Helm dans le repo Git constituent la référence, mais rien ne garantit que le cluster y est conforme entre deux déploiements.

#### Crossplane

La XR Crossplane est la source de vérité. Crossplane reconcilie en permanence l'état réel vers cet état déclaré, indépendamment de Git.

#### Kratix

Le repo Git (State Store) est la source de vérité. ArgoCD maintient le cluster conforme au contenu du repo. Un changement dans Git se répercute sur le cluster, qu'il vienne de Kratix ou d'un push direct.

#### Crossplane + Kratix

La XR Crossplane est la source de vérité, comme dans la solution 2.

### Scalabilité

#### Backstage seul

La charge de l'équipe plateforme augmente avec le nombre d'équipes et d'applications (plus de templates à maintenir, plus de questions de support, ...). Sans enforcement technique, chaque nouvelle équipe génère potentiellement de nouveaux cas à étudier.

#### Crossplane

Une fois les Compositions écrites, elles s'appliquent à toutes les équipes sans effort supplémentaire. La charge de l'équipe plateforme ne dépend donc plus du nombre d'équipes servies, mais de la complexité des abstractions.

#### Kratix

Même logique que Crossplane : les Promises s'appliquent à toutes les équipes. La charge de maintenance des conteneurs de pipeline reste constante quel que soit le nombre d'applications.

#### Crossplane + Kratix

Même bonne scalabilité que les deux solutions précédentes, avec une complexité plus importante à maintenir.

## Résumé

Au moment où nous écrivons ce rapport, nous sommes à peu près sûr que l'outil Backstage sera retenu.

Ainsi, les évaluations de la difficulté de Backstage seront ici confondues avec les efforts propres à l'intégration de ce Golden Path à Backstage, qui sont donc "assez minces" comparé aux autres solutions qui nécessitent l'intégration complète d'outils tels que Crossplane ou Kratix (même si l'intégration de Backstage et le travail nécessaire pour le rendre opérationnel est conséquent).

Par ailleurs, il est important de noter que Backstage sera présent dans toutes les solutions. La distinction entre les solutions ne porte donc pas sur l'interface développeur, mais sur ce qui se passe en dessous.

| Dimension                   | Backstage                  | Crossplane                         | Kratix                     | Crossplane + Kratix           |
| --------------------------- | -------------------------- | ---------------------------------- | -------------------------- | ----------------------------- |
| Mise en place               | Facile                     | Compliqué                          | Moyen - Compliqué          | Très compliqué                |
| Expérience utilisateur      | Très agréable (Formulaire) | Très agréable (Formulaire)         | Très agréable (Formulaire) | Très agréable (Formulaire)    |
| Performance                 | Bien                       | Bien                               | Bien                       | Bien                          |
| Maintenance & Mise à jour   | Facile                     | Moyen - Compliqué                  | Moyen - Compliqué          | Très compliqué                |
| Support                     | Moyen                      | Moyen - Difficile                  | Facile                     | Facile, résolution compliquée |
| Accessibilité               | Base                       | Compliqué                          | Moyen                      | Très compliqué                |
| Conception des abstractions | Facile                     | Compliqué                          | Moyen                      | Très compliqué                |
| Débogage                    | Facile                     | Compliqué                          | Moyen                      | Très compliqué                |
| Vérifications               | Que dans formulaire        | Formulaire + XRD (+ Outil externe) | Pipeline Kratix            | Pipeline Kratix               |
| Réconciliation continue     | Non                        | Oui                                | Oui (Kratix + ArgoCD)      | Oui                           |
| Enforcement côté serveur    | Non                        | Schéma XRD                         | Pipeline Kratix            | Schéma XRD + Pipeline Kratix  |
| Scalabilité                 | Mauvaise                   | Bien                               | Bien                       | Bien                          |

## Décision

### Bilan

Les quatre solutions partagent la même interface développeur (formulaire Backstage) et des performances comparables une fois en place. Ce qui les différencie fondamentalement, c'est le niveau de contrôle et de robustesse offert à l'équipe plateforme, et le coût (en compétences, en temps, en complexité, ...).

**Backstage seul** est la solution la plus accessible et la plus rapide à mettre en place. Elle repose sur des outils maîtrisés (Git, Helm, CI/CD) et ne demande pas de compétences Kubernetes avancées. Sa faiblesse est l'absence d'enforcement côté serveur : les validations n'existent que dans le formulaire Backstage, contournable par une MR directe ou un kubectl apply manuel. La scalabilité est également limitée : la charge de l'équipe plateforme augmente avec le nombre d'équipes. C'est bien pour démarrer, mais ce sera de plus en plus compliqué au fur et à mesure que la plateforme grandit.

`Paragraphe étoffé par l'IA`
**Crossplane** introduit un niveau de rigueur technique important : le schéma XRD enforce les validations à chaque kubectl apply, et la réconciliation continue garantit que l'état du cluster reste conforme à la configuration déclarée en toutes circonstances. C'est la solution la plus adaptée aux équipes ayant une forte culture infrastructure et souhaitant un contrôle fin sur les ressources Kubernetes et cloud. En contrepartie, la courbe d'apprentissage est élevée (Composition Functions, mode Pipeline, Providers), le débogage peut être complexe, et les règles organisationnelles (quotas, approbation humaine) nécessitent des outils externes (comme OPA ou Kyverno apparemment ?).

**Kratix** adopte une approche différente : plutôt que de gérer l'état en continu, il gère des workflows. Son point fort est l'expressivité de ses pipelines : toute règle métier ou organisationnelle peut y être encodée directement en Python ou Go, sans outil externe. L'approbation humaine, la vérification de quotas, les notifications, etc. se passent dans le pipeline de la Promise. La complexité d'entrée est plus faible que Crossplane, notamment grâce au SDK Python. La réconciliation est assurée à la fois par la loop périodique de Kratix et par ArgoCD, ce qui est solide mais reste moins réactif que la réconciliation Crossplane.

**Crossplane + Kratix** combine le meilleur des deux solutions précédentes : la richesse des workflows Kratix pour la validation et la gouvernance, et la réconciliation continue de Crossplane pour la robustesse. C'est la solution la plus complète et la plus sécurisée, mais aussi la plus complexe à mettre en place, à maintenir et à déboguer. Elle exige des compétences dans les deux outils simultanément et un travail supplémentaire pour maintenir la cohérence entre les Promises Kratix et les XRDs Crossplane.

### Késkonfé

Cette sous-section est très généraliste et résume ce qui est dit dans ce rapport (et ce que j'ai compris). On adaptera à notre cas dans la sous-section suivante.

#### Privilégier Backstage seul si :

- L'équipe plateforme est peu disponible pour investir dans de nouveaux outils.
- Il faut livrer un Golden Path fonctionnel rapidement, quitte à l'enrichir plus tard.
- Les équipes de développement sont peu nombreuses et peuvent se reposer sur des conventions, des reviews humaines, etc.
- Il n'existe pas encore de culture Kubernetes avancée dans l'équipe plateforme.

Attention : la dette technique s'accumule vite si le nombre d'équipes et/ou d'applications augmente. Il faut envisager d'intégrer une des solutions suivantes dès que possible.

#### Privilégier Crossplane si :

- L'équipe plateforme a (ou peut acquérir) une solide culture Kubernetes et IaC.
- La priorité est la réconciliation continue : s'assurer qu'aucune dérive ne peut persister sur les clusters, avec ou sans intervention humaine.
- Les ressources à gérer incluent des ressources cloud (buckets S3, bases de données managées, réseaux...) en plus des ressources Kubernetes.
- Les règles organisationnelles sont relativement simples (la validation de schéma suffit).
- L'équipe est à l'aise avec un modèle purement déclaratif et ne ressent pas le besoin de workflows impératifs.

Attention : ne pas sous-estimer le temps d'apprentissage des Composition Functions. Prévoir une phase de montée en compétences avant de passer en production.

#### Privilégier Kratix si :

- L'équipe plateforme a une culture développement (Python, Go) plus qu'une culture infrastructure pure.
- Les règles organisationnelles sont complexes ou nombreuses : approbation humaine, vérification de quotas, notifications, intégrations avec des APIs externes.
- On préfère avoir des workflows flexibles plutôt que de la réconciliation continue.
- On veut garder la main sur la logique métier sans dépendre d'outils externes (OPA/Kyverno, encore et toujours).
- Le passage à l'échelle est un enjeu majeur (les Promises s'appliquent à toutes les équipes sans effort supplémentaire)

Attention : les conteneurs de pipeline doivent être traités comme de vrais projets logiciels (tests, CI/CD pour les images, versioning). Ne pas négliger cet investissement.

#### Privilégier Crossplane + Kratix si :

- La plateforme doit être robuste et évolutive sur le long terme, et l'équipe est prête à assumer la complexité.
- Les deux besoins sont présents simultanément : workflows organisationnels complexes (Kratix) et réconciliation continue stricte sur les ressources (Crossplane).
- L'équipe plateforme est suffisamment disponible (beaucoup de membres dans l'équipe, ...) pour maintenir deux outils en conditions opérationnelles, avec des profils couvrant à la fois la culture développement et la culture infrastructure.
- La gouvernance est un enjeu fort : on souhaite le double enforcement (pipeline Kratix + schéma XRD Crossplane) pour être certain qu'aucune configuration non conforme ne peut atteindre la production.

Attention : Il faut bien faire attention à ce que les besoins réels justifient la complexité de cette solution. Aussi, bien définir dès le départ la frontière de responsabilité entre les deux outils pour éviter les zones grises lors du débogage.

#### Trajectoire recommandée

`Paragraphes étoffés par l'IA`

Si l'équipe part de zéro et que les besoins de gouvernance sont amenés à croître, une trajectoire progressive est envisageable :

- Démarrer avec Backstage seul pour livrer rapidement un Golden Path fonctionnel et apprendre les patterns d'usage des équipes de développement.
- Migrer vers Kratix dès que les besoins de validation métier ou d'approbation humaine deviennent récurrents, ou que le nombre d'équipes rend la solution Backstage seul difficile à maintenir.
- Ajouter Crossplane si la réconciliation continue sur les ressources cloud devient un besoin, ou si la gestion de ressources cloud (AWS, GCP...) entre dans le périmètre du Golden Path.

Cette trajectoire permet de limiter le risque technique à chaque étape, tout en conservant une porte de sortie vers la solution la plus complète si le besoin s'en fait sentir.

### Késkonfé anvré

#### Situation

Dans notre cas :

L'équipe plateforme est composée de 6 personnes (si ça a pas changé) ayant une bonne culture Kubernetes, en développement (en Python notamment, ou en Go mais ce serait plus étonnant) et en CI/CD. ArgoCD est déjà en place. La plateforme a vocation à être utilisée par beaucoup d'équipes de développeurs, gérant à la fois de nouveaux projets et des applications existantes à mettre en conformité avec les bonnes pratiques. 
Le passage en production implique une validation humaine obligatoire (je suppose). La création d'environnement de test (des bacs à sable pour les développeurs s'ils veulent tester quelque chose rapidement) doit être simple. On a à la fois des VM, du Kubernetes et du Cloud.

Solution recommandée : Kratix, avec évolution vers Crossplane + Kratix

#### Dans un premier temps : Kratix

Kratix est la solution qui répond le plus directement à nos contraintes :

- **Scalabilité :** Avec beaucoup équipes, l'absence d'enforcement côté serveur de Backstage seul est problématique. Les Promises Kratix s'appliquent à toutes les équipes facilement, donc on peut avoir autant de développeurs qu'on veut sur la plateforme.
- **Validation humaine en production :** Le mécanisme de suspension de Kratix (suspend) est pile ce qu'il faut pour les workflows de passage en production. Avec Crossplane seul, cette fonctionnalité nécessiterait un outil externe.
- **Environnements différenciés :** Les Promises permettent de définir des workflows distincts selon l'environnement : un pipeline léger sans approbation pour le bac à sable de développement, et un pipeline complet avec validations et approbation pour la production.
- **Compétences disponibles :** L'équipe a possiblement le profil pour Kratix : Python/Go pour les conteneurs de pipeline, Kubernetes avancé pour le déploiement et le RBAC, et ArgoCD pour le GitOps (déjà là).
- **Support à l'échelle :** Les messages d'erreur du pipeline étant configurables par l'équipe plateforme, le support des développeurs reste gérable même à grande échelle.
- **Mise en conformité des applications déjà déployées :** Le pipeline Kratix peut être déclenché sur des applications existantes via une ResourceRequest, appliquant les nouvelles bonnes pratiques de manière contrôlée et traçable.

#### Dans un second temps : ajouter Crossplane

L'ajout de Crossplane devient pertinent dès que l'une des conditions suivantes se réalise :

- La gestion de ressources cloud (buckets S3, bases de données managées, réseaux VPC...) entre dans le périmètre du Golden Path, et la réconciliation continue sur ces ressources devient un besoin opérationnel.
- L'unification VM / Kubernetes / Cloud devient un objectif actif : Crossplane dispose de Providers pour VMware et les principaux clouds publics, ce qui en fait le candidat naturel pour un control plane unifié sur les trois mondes.
- Le besoin d'un enforcement déclaratif strict (correction automatique et immédiate de toute dérive de configuration, indépendamment des cycles de réconciliation Kratix) se fait sentir à l'échelle.

À ce stade, l'ajout de Crossplane en complément de Kratix est la solution la plus complète et la plus stable.

### Késkonfépa

`Sous-section étoffée par l'IA`

#### Pourquoi pas Crossplane + Kratix dès maintenant ?

L'équipe ne connaît aujourd'hui ni Crossplane ni Kratix. Démarrer avec les deux simultanément doublerait la courbe d'apprentissage et la complexité opérationnelle sans bénéfice immédiat : Kratix seul couvre la grande majorité des besoins identifiés. Introduire Crossplane une fois Kratix maîtrisé est une trajectoire plus sûre, qui permet à chaque étape de valider les acquis avant d'ajouter une nouvelle couche.

#### Pourquoi pas Crossplane seul ?

Crossplane seul ne gère pas nativement les workflows organisationnels : l'approbation humaine en production, la différenciation des pipelines par environnement, et les vérifications de quotas nécessiteraient des outils externes (OPA/Kyverno) dont la mise en place représente une charge supplémentaire. Le profil de l'équipe (forte culture dev) correspond par ailleurs mieux au modèle Kratix qu'au modèle déclaratif pur de Crossplane.

#### Pourquoi pas Backstage seul ?

Avec beaucoup équipes, l'absence d'enforcement côté serveur rend cette solution structurellement inadaptée. Toute convention non enforcée techniquement devient une source de dérive à cette échelle. La solution peut servir de point de départ pour travailler le formulaire et les templates, mais ne doit pas être envisagée comme solution finale.

## Questions

Dans cette section, je résume les questions que je me suis posé lors de la rédaction de ce rapport.
Ces questions ont été répondues à l'aide de la documentation (ce que j'ai compris d'elle) et, pour certaines questions, de l'IA.

### Crossplane est-il indispensable pour gérer des ressources Cloud ?

En vrai, Crossplane n'est pas forcément indispensable pour gérer des ressources Cloud dans le cadre de ce Golden Path. Kratix peut gérer des ressources Cloud via ses pipelines, en orchestrant des outils tiers qui parlent aux APIs Cloud à sa place.

Kratix propose deux approches :

- Via Terraform dans le pipeline : un step du pipeline exécute un `terraform plan` puis un `terraform apply`, ce qui provisionne la ressource Cloud (bucket S3, base de données, réseau...). C'est la combinaison la plus classique et elle est documentée.
- `Paragraphe ajouté par l'IA` Via un appel direct à une API Cloud : un step du pipeline appelle directement le SDK du provider (boto3 pour AWS, google-cloud-python pour GCP, etc.). C'est plus flexible mais plus artisanal.

La différence majeure avec Crossplane est que Kratix déclenche le provisioning Cloud (au moment de la ResourceRequest, puis lors de ses cycles de réconciliation), mais ne surveille pas en continu l'état des ressources Cloud créées. Si une ressource Cloud est modifiée ou supprimée hors du Golden Path, Kratix ne le détectera qu'à son prochain cycle de réconciliation (toutes les 10 heures par défaut), ce qui peut laisser une fenêtre de dérive ouverte.

Crossplane, lui, surveille l'état réel de chaque ressource Cloud qu'il gère via ses Providers, et corrige toute divergence en quelques minutes automatiquement.

`Paragraphe étoffé par l'IA`
**En résumé :** Kratix suffit pour du provisioning Cloud à la demande. Crossplane devient pertinent si la réconciliation continue stricte sur les ressources Cloud est un besoin opérationnel identifié (environnements critiques, ressources sensibles au drift).

### Quelle est la différence entre la réconciliation continue de Crossplane et celle d'ArgoCD ?

Les deux outils font de la réconciliation, mais ils ne surveillent pas la même chose.

`Paragraphe étoffé par l'IA`
ArgoCD est un opérateur GitOps : sa source de vérité est un repo Git. Il surveille l'écart entre ce que contient le repo et ce qui est déployé sur le cluster. Si une ressource est supprimée du cluster alors qu'elle est présente dans Git, ArgoCD la recrée. En revanche, ArgoCD ne surveille pas l'état interne des ressources : si un Deployment existe bien sur le cluster mais que son nombre de réplicas a été modifié manuellement, ArgoCD n'y voit rien d'anormal. Tant que la ressource est présente, il considère que c'est bon.

Crossplane surveille une XR (l'objet MyApp) et s'assure que toutes les ressources dérivées de cette XR (Deployment, PodDisruptionBudget, NetworkPolicy, Ingress, ressources Cloud, ...) sont bien conformes à ce que la Composition décrit. Si un développeur modifie manuellement le nombre de réplicas d'un Deployment, Crossplane détecte la divergence et le remet à la valeur attendue en quelques minutes.

La distinction peut se résumer ainsi :

`Tableau réalisé par l'IA`
|                                              | ArgoCD                                 | Crossplane                          |
| -------------------------------------------- | -------------------------------------- | ----------------------------------- |
| Source de vérité                             | Repo Git                               | XR (objet Kubernetes)               |
| Ce qu'il surveille                           | Présence des manifestes sur le cluster | État interne des ressources enfants |
| Détecte une modification manuelle d'un champ | ❌ Non                                 | ✅ Oui                              |
| Détecte une suppression de ressource         | ✅ Oui (si dans Git)                   | ✅ Oui                              |

ArgoCD et Crossplane sont donc complémentaires. Dans la solution Crossplane + Kratix, ArgoCD applique la XR depuis Git, et Crossplane prend ensuite le relais pour maintenir les ressources enfants conformes à cette XR.

`Paragraphe ajouté par l'IA`
À noter : dans de nombreux contextes, la combinaison ArgoCD + un RBAC strict (interdisant les `kubectl edit` en production) suffit à couvrir le besoin sans ajouter Crossplane. La réconciliation Crossplane apporte une garantie technique supplémentaire, mais elle a un coût en complexité.

### Si Crossplane est implémenté, les développeurs seront-ils bloqués pour modifier leur application autrement que via la plateforme ?

Oui, et c'est normal, mais ça doit être soigneusement encadré par le RBAC.
Crossplane surveille en permanence l'état des ressources qu'il gère et le compare à la XR. Toute modification qui diverge de la XR est automatiquement corrigée. 
Concrètement :

- Un `kubectl edit` direct sur un Deployment géré par Crossplane sera écrasé dans les minutes qui suivent.
- Un `kubectl apply` qui modifie une ressource enfant sera de même annulé.
- Un `git push` qui modifie directement la XR dans Git sera, lui, pris en compte. C'est le seul vecteur de modification légitime avec Backstage.

`Paragraphe ajouté par l'IA`
Cependant, ce comportement n'est garanti que si le RBAC est correctement configuré pour interdire aux développeurs de modifier directement les XRs ou les ressources enfants sur le cluster. Sans RBAC adapté, un développeur ayant un accès `cluster-admin` pourrait toujours contourner Crossplane, même si ses modifications seraient écrasées rapidement.

En pratique, cela signifie que la plateforme devient le seul canal officiel pour modifier la configuration d'une application. On peut noter que c'est quand même un objectif du Golden Path : centraliser et tracer toutes les modifications de configuration, et empêcher les dérives non contrôlées. Cependant, il est important de s'assurer que la plateforme couvre bien tous les cas d'usage légitimes des développeurs pour que ce canal unique ne devienne pas une friction pour eux.

### Qu'en est-il du monde VM avec Crossplane et Kratix ?

#### Kratix et les VMs

`Ces 3 paragraphes ont été étoffés par l'IA`

Kratix ne gère pas les VMs nativement, mais ses pipelines peuvent orchestrer n'importe quel outil de gestion de VMs existant. Si on dispose déjà d'outils pour gérer les VMs (scripts Ansible, modules Terraform, APIs internes...), un step du pipeline Kratix peut les appeler directement.

Cela signifie que Kratix peut servir de façade unifiée pour les trois mondes (VM, Kubernetes, Cloud) via Backstage : le développeur remplit le même formulaire, et c'est le pipeline de la Promise qui orchestre les bons outils selon l'environnement cible. La logique de routage ("cet environnement est sur VM, cet autre sur Kubernetes") peut être encodée dans le pipeline.

C'est une intégration souple, mais elle reste à la charge de l'équipe plateforme : il n'existe pas de support VM natif dans Kratix, et la qualité de l'intégration dépend entièrement de la qualité des outils appelés dans le pipeline.

#### Crossplane et les VMs

Crossplane dispose de Providers pour gérer des ressources VMware vSphere : création de VMs, gestion des datastores, des réseaux, etc. Cependant, il est important de nuancer leur maturité :

- Le provider officiel `provider-terraform-vsphere` de crossplane-contrib est déprécié et ne doit pas être utilisé.
- Le provider communautaire `ankasoftco/provider-vsphere` (disponible sur le marketplace Upbound) expose des ressources vSphere et est activement maintenu, mais il s'agit d'un projet communautaire, non d'un provider officiel Crossplane. Sa robustesse en production est donc à évaluer.
- Il existe également des providers pour VMware NSX-T et vCloud Director, également communautaire.

En pratique, si notre infrastructure VM repose sur vSphere (de souvenir, c'est le cas ?), Crossplane peut en théorie la gérer, mais avec un niveau de maturité et de support inférieur aux providers cloud officiels (AWS, GCP, Azure).

#### Recommandation pour les VMs

`Paragraphes étoffés par l'IA`

Compte tenu du contexte (des outils de gestion de VMs déjà en place, et l'unification VM souhaitée mais non bloquante à court terme), la trajectoire la plus pragmatique est la suivante :

- Court terme : Kratix orchestre les outils VM existants depuis ses pipelines. Pas de rupture avec l'existant, et les développeurs bénéficient déjà de l'interface unifiée Backstage.
- Moyen terme : si Crossplane est adopté pour le Cloud et Kubernetes, évaluer les providers vSphere communautaires pour déterminer s'ils couvrent les ressources VM utilisées en interne. Si c'est le cas, migrer progressivement la gestion VM vers Crossplane pour bénéficier du modèle déclaratif unifié.
- Alternativement : maintenir la gestion VM via Terraform (appelé depuis les pipelines Kratix), ce qui est une combinaison mature et bien documentée, et réserver Crossplane au Cloud et à Kubernetes.