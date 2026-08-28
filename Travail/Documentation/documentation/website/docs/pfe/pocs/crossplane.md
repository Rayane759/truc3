# Crossplane

Crossplane est un framework qui transforme un cluster Kubernetes en un control plane d'infrastructure. Il permet de définir et de gérer des ressources cloud (bases de données, buckets, réseaux...) et Kubernetes via des objets Kubernetes déclaratifs, en maintenant en permanence l'état réel conforme à l'état déclaré.

C'est un projet **open source** (licence Apache 2.0), créé par Upbound, à gouvernance neutre — pas de dépendance à un éditeur. C'est un **projet CNCF « gradué »** depuis le **28 octobre 2025** : le plus haut niveau de maturité CNCF, aux côtés de Kubernetes, Prometheus et Helm, ce qui est un gage de pérennité et de sécurité pour un choix d'infrastructure durable.

## Pourquoi un moteur d'orchestration, en plus du portail ?

La première réponse envisagée pour la plateforme est un portail développeur (Backstage). Il est utile mais partiel : il **expose** un catalogue et **génère** des dépôts (le *day 0*), mais il ne **gère pas** le cycle de vie dans la durée — évolutions, mises à jour, conformité (le *day 2*). Backstage est une vitrine ; il manque le moteur qui provisionne et gouverne réellement l'infrastructure derrière elle.

Un moteur d'orchestration ne se contente pas d'exécuter une suite d'actions une fois (à la différence d'un script ou d'un pipeline classique, de type Terraform/OpenTofu ou Ansible) : il maintient un système dans l'état voulu, en continu, via une **boucle de réconciliation** qui compare en permanence l'état réel à l'état désiré et corrige l'écart automatiquement — y compris en cas de panne ou de modification hors cadre. C'est le principe qui a fait le succès de Kubernetes pour les applications ; Crossplane l'étend à toute l'infrastructure. C'est l'implémentation la plus courante de ce rôle dans les démarches de Platform Engineering.

Crossplane repose sur quatre concepts fondamentaux : les XRDs, les Compositions, les Claims, et les XRs.

## XRD : Composite Resource Definition

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

## Composition

La Composition décrit comment Crossplane doit traduire une XR (instance de MyApp) en ressources réelles. C'est ici qu'il y a toute la logique technique : mapping des valeurs, création des ressources Kubernetes ou cloud, application des politiques de production, etc.

Une Composition peut créer autant de ressources que nécessaire à partir d'une seule XR : Deployment, Network Policy, Ingress, bucket S3, etc.

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

## Claim : ce que déclare le développeur

La **Claim** est l'objet que le développeur dépose dans son propre namespace : c'est la demande de service, au format défini par la XRD. C'est le contrat d'interface concret que le développeur consomme — il dépend de ce contrat, jamais de ce qu'il y a derrière.

Le développeur (ou l'IDP à sa place) ne l'applique jamais directement sur le cluster : il la **pousse dans un dépôt Git**, surveillé par **ArgoCD**, qui l'applique via son cycle de synchronisation GitOps habituel. C'est cette application par ArgoCD qui rend la Claim visible de Crossplane.

Une Claim est liée en coulisses à une **XR** (voir ci-dessous) que Crossplane crée et gère pour elle. Ce découplage Claim (namespacée, côté développeur) / XR (au niveau du cluster, côté plateforme) permet de garder les demandes des équipes applicatives isolées dans leur namespace, tout en laissant Crossplane orchestrer les ressources composites au niveau du cluster.

```yaml
# Exemple de Claim (objet app.yaml dans le repo Git du développeur, namespace de l'équipe)
apiVersion: platform.company.io/v1alpha1
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

## XR : Composite Resource

La XR est l'instance composite que Crossplane crée pour honorer une Claim (ou, plus rarement, directement par l'équipe plateforme, sans Claim, pour des ressources non namespacées). C'est l'objet concret qui exprime la configuration souhaitée au niveau du cluster. Crossplane détecte sa création ou sa modification et déclenche la réconciliation vers les ressources définies dans la Composition.

## Provider

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

## Expérience Développeur

Le développeur va sur Backstage, sur son application, et clique sur le bouton "Modifier la configuration". Un formulaire s'ouvre, similaire à celui du Golden Path, lui proposant les mêmes champs. Backstage génère alors le fichier app.yaml mis à jour dans son repo Git.

Ce fichier app.yaml est une Claim Crossplane, qui ressemble à ça :

```yaml
# Fichier app.yaml — Claim Crossplane (généré par Backstage, namespace de l'équipe)
apiVersion: platform.company.io/v1alpha1 # Groupe défini dans la XRD
kind: MyApp # Type défini dans la XRD
metadata:
  name: my-service
  namespace: my-team
spec:
  env: production
  replicas: 3
  resources: medium
  expose: public
```

Les champs sont assez explicites, le développeur peut les lire et les vérifier facilement avant de soumettre.
De plus, en cas d'erreur de schéma (mauvais type, valeur non prévue, champ obligatoire manquant), Crossplane rejette la modification et en informe le développeur.

Le développeur valide ses changements, Backstage ouvre une MR sur son dépôt Git. Celle-ci est relue rapidement car les champs sont simples et lisibles. Une fois mergée, c'est **ArgoCD** — qui surveille ce dépôt — qui applique le fichier sur le cluster, selon son cycle de synchronisation GitOps habituel (pas d'étape `kubectl apply` en pipeline CI). C'est à ce moment-là que Kubernetes valide le fichier par rapport au schéma de la **XRD** et rejette immédiatement toute valeur invalide (mauvais type, valeur non autorisée, champ obligatoire manquant), avant même que Crossplane ne traite la demande.

## Ce que fait la plateforme

Une fois le `app.yaml` appliqué sur le cluster par ArgoCD, Kubernetes enregistre la **Claim**, et Crossplane crée ou met à jour la **XR** associée.
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

## Expérience équipe plateforme (Ce qu'elle met en place, ...)

L'équipe plateforme doit : 

- Créer et maintenir les templates Backstage (formulaire de modification, action qui génère le fichier app.yaml et ouvre la MR)
- Rédiger les XRD et les Compositions pour chaque type d'application
- Configurer les Providers (Kubernetes, AWS, ...)
- Configurer ArgoCD pour surveiller les dépôts contenant les Claims et les appliquer sur le cluster (GitOps, pas de `kubectl apply` en pipeline CI)
- Gérer les maintenances + mises à jour de Crossplane, des XRD et des Compositions

## Mise en place

En plus des Software Templates Backstage, l'équipe doit installer Crossplane via Helm chart dans un namespace dédié, installer et configurer les Providers nécessaires (provider-kubernetes, provider-aws, provider-gcp...) avec leurs credentials et permissions IAM associés, écrire les XRDs (schéma de l'API développeur) et les Compositions (mapping vers les ressources réelles) pour chaque type d'application, et mettre en place le RBAC pour interdire les modifications directes des XRs sur le cluster.

La partie la plus exigeante est la conception des Compositions. Depuis Crossplane v1.17, le standard est le mode Pipeline avec des Composition Functions : la logique de mapping est exprimée via des functions (officielles comme `function-patch-and-transform`, ou custom). Ce standard est plus puissant que l'ancien mode `Resources` (déprécié), mais nécessite un apprentissage supplémentaire par rapport à celui-ci. Il faudra attendre plusieurs semaines avant d'avoir une première Composition fonctionnelle en production.

## Bénéfices attendus

**Côté développeur** :

- **Self-service** : la ressource est obtenue sans ticket ni attente.
- **Simplicité** : une abstraction claire (la Claim), sans connaître AWS/Azure/GCP ni l'outillage infra sous-jacent.
- **Outils familiers** : le développeur reste dans Git / le portail Backstage, son workflow habituel.
- **Autonomie et garde-fous** : il consomme l'API avec ou sans portail ; sécurité et conformité sont gérées pour lui par la Composition.

**Côté équipe plateforme** :

- **Gouvernance centralisée** : politiques appliquées à la création (RBAC, et le cas échéant Kyverno / OPA), pas de vérification manuelle a posteriori.
- **Standardisation** : un seul modèle, un seul workflow GitOps pour toutes les infras.
- **Évolution maîtrisée** : changer l'implémentation derrière le contrat (la Composition) se propage automatiquement à toutes les instances existantes, sans migration dépôt par dépôt.
- **Contrôle continu** : moins de tickets répétitifs ; l'état réel est réconcilié en permanence, la dérive corrigée.

## Recommandation

Crossplane est retenu comme moteur d'orchestration de la plateforme, en complément de Backstage (voir [ADR-008 — Format de la plateforme](../adr/adr-008-format-plateforme.md)) : Backstage répond au « comment le développeur demande et suit sa ressource » (day 0), Crossplane répond au « comment elle est réellement livrée et gouvernée dans la durée » (day 2). Cette articulation permet de répartir la charge entre équipes services (qui publient leurs briques de base sous forme de Providers/Compositions et en restent responsables) et équipe plateforme (qui assemble ces briques en services de plus haut niveau) : la consommation directe d'une brique par un développeur reste possible (Git / kubectl), sans passer par la plateforme — le portail Backstage est une commodité, pas un péage obligatoire.
