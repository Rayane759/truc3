# Kratix

Kratix est un orchestrateur de plateforme qui se concentre sur la définition et l'exécution de workflows : des étapes qui peuvent inclure des validations techniques ou humaines, des appels à des APIs externes,la génération de manifeste, etc.

Kratix se repose sur deux concepts fondamentaux : les Promises et le State Store.

## Vocabulaire

### Promise

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

### Conteneur de pipeline

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

### ResourceRequest

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
