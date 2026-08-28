# Etat des lieux Components

## Liste des components

### Scan

#### Trivy (DSI)

Lien du code source : `https://gitlab.insee.fr/dsi/analyzer/composants/gitlab-ci-trivy-component`
Component : `gitlab.insee.fr/dsi/analyzer/composants/gitlab-ci-trivy-component/scan@2.0.0`
Date de dernière mise à jour du dépôt : 25/03/2026
Utilisaton : 
```yaml
include:
  - component: gitlab.insee.fr/dsi/analyzer/composants/gitlab-ci-trivy-component/scan@2.0.0
    inputs:
      stage: "test"
      fail_on_severity: "CRITICAL|HIGH" # Facultatif
      TRIVY_IGNORE: "" # Facultatif
      rules:  # Facultatif
        - when: manual
          allow_failure: true
```

#### Trivy (KubeApp)

Lien du code source : `https://gitlab.insee.fr/kubernetes/kubeapp/components/trivy`
Component : `$CI_SERVER_FQDN/kubernetes/kubeapp/components/trivy/component@0.0.1`
Date de dernière mise à jour du dépôt : 16/12/2025
Utilisaton : 
```yaml
components:
  - name: $CI_SERVER_FQDN/kubernetes/kubeapp/components/trivy/component@0.0.1
    inputs:
      trivy_path_to_trivyignore: "" # Optionnel
```

#### GitLeaks

Lien du code source : `https://gitlab.insee.fr/dsi/analyzer/composants/gitlab-ci-gitleaks-component`
Component : `gitlab.insee.fr/dsi/analyzer/composants/gitlab-ci-gitleaks-component/scan@1.0.0`
Date de dernière mise à jour du dépôt : 09/12/2025
Utilisaton : 
```yaml
  - component: gitlab.insee.fr/dsi/analyzer/composants/gitlab-ci-gitleaks-component/scan@1.0.0
    inputs:
      stage: "test"
      rules:  # Facultatif
        - when: on_success
          allow_failure: false
      scan_path: "." # Facultatif
```

#### SAST

Lien du code source : `https://gitlab.insee.fr/dsi/analyzer/composants/gitlab-ci-sast-component`
Component : `gitlab.insee.fr/dsi/analyzer/composants/gitlab-ci-sast-component/sast@0.0.0`
Date de dernière mise à jour du dépôt : 26/05/2026
Utilisaton : 
```yaml
include:
  - component: gitlab.insee.fr/dsi/analyzer/composants/gitlab-ci-sast-component/sast@0.0.0
    inputs:
      stage: "security-app"
      fail_on_severity: "HIGH|CRITICAL" # Facultatif
      SAST_EXCLUDED_PATHS: "spec, test, tests, tmp" # Facultatif
      rules: # Facultatif
        - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
          when: on_success
        - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'
          when: on_success
        - when: never
```

#### Semgrep 

`https://gitlab.insee.fr/dsi/analyzer/composants/semgrep`

---

### Docker

#### Crane

Lien du code source : `https://gitlab.insee.fr/kubernetes/kubeapp/components/crane`
Component : `$CI_SERVER_FQDN/kubernetes/kubeapp/components/crane/component@0.0.1`
Date de dernière mise à jour du dépôt : 30/09/2025
Utilisaton : 
```yaml
components:
  - name: $CI_SERVER_FQDN/kubernetes/kubeapp/components/crane/component@0.0.1
    inputs:
      push_image_registry: "${CI_REGISTRY_IMAGE}"
      push_image_tags: "${CI_COMMIT_REF_NAME}"
      tar_path: "image.tar"
```

#### Docker (Lint + Build + Check + Push)

Lien du code source : `https://gitlab.insee.fr/kubernetes/kubeapp/components/docker`
Component (Lint): `gitlab.insee.fr/kubernetes/kubeapp/components/docker/gitlab-ci-docker-lint-component@0.0.2`
Component (Build): `gitlab.insee.fr/kubernetes/kubeapp/components/docker/gitlab-ci-docker-build-component@0.0.2`
Component (Check): `gitlab.insee.fr/kubernetes/kubeapp/components/docker/gitlab-ci-docker-check-component@0.0.2`
Component (Push): `gitlab.insee.fr/kubernetes/kubeapp/components/docker/gitlab-ci-docker-push-component@0.0.2`
Date de dernière mise à jour du dépôt : 26/11/2025
Utilisaton : 
```yaml
stages:
  - lint
  - build
  - check
  - push

include:
  - component: gitlab.insee.fr/kubernetes/kubeapp/components/docker/gitlab-ci-docker-lint-component@0.0.2
    inputs:
      path_to_dockerfile: "Dockerfile"
      stage: lint
  - component: gitlab.insee.fr/kubernetes/kubeapp/components/docker/gitlab-ci-docker-build-component@0.0.2
    inputs:
      path_to_dockerfile: "Dockerfile"  # Optionnel
      stage: build
  - component: gitlab.insee.fr/kubernetes/kubeapp/components/docker/gitlab-ci-docker-check-component@0.0.2
    inputs:
      trivy_path_to_trivyignore: "" # Optionnel
      stage: check
      allow_failure: true
      dependencies: [docker-build]
  - component: gitlab.insee.fr/kubernetes/kubeapp/components/docker/gitlab-ci-docker-push-component@0.0.2
    inputs:
      push_image_registry: "${CI_REGISTRY_IMAGE}"
      push_image_tags: "${CI_COMMIT_REF_NAME}"
      tar_path: "image.tar"
      stage: push
      dependencies: [docker-build]
```

#### Docker Lint (Hadolint)

Lien du code source : `https://gitlab.insee.fr/kubernetes/kubeapp/components/hadolint`
Component : `$CI_SERVER_FQDN/kubernetes/kubeapp/components/hadolint/component@0.0.1`
Date de dernière mise à jour du dépôt : 30/09/2025
Utilisaton : 
```yaml
components:
  - name: $CI_SERVER_FQDN/kubernetes/kubeapp/components/hadolint/component@0.0.1
    inputs:
      path_to_dockerfile: "Dockerfile"
      hadolint_disabled: "false"
```

#### Docker Build (Kaniko)

Lien du code source : `https://gitlab.insee.fr/kubernetes/kubeapp/components/kaniko`
Component : `$CI_SERVER_FQDN/kubernetes/kubeapp/components/kaniko/component@0.0.1`
Date de dernière mise à jour du dépôt : 30/09/2025
Utilisaton : 
```yaml
components:
  - name: $CI_SERVER_FQDN/kubernetes/kubeapp/components/kaniko/component@0.0.1
    inputs:
      path_to_dockefile: "Dockerfile" # Optionnel
```

#### Image Run

Lien du code source : `https://gitlab.insee.fr/kubernetes/kubeapp/components/image-run`
Component : `$CI_SERVER_FQDN/kubernetes/kubeapp/components/image-run/component@0.2.7`
Date de dernière mise à jour du dépôt : 10/06/2026
Utilisation : (Exemple, il y a d'autres exemples dans la doc)
```yaml
include:
  - component: $CI_SERVER_FQDN/kubernetes/kubeapp/components/image-run/component@0.2.7
    inputs:
      path_to_version_file: "dockerfiles/version.yaml"
      path_to_dockerfile: "dockerfiles/Dockerfile"
      path_to_container_test_file: ".ci/containers_test/config.yaml"
      image_tag_regex: "s/-jre.*//"
```

### Autre

#### GitOps Value Updater

Lien du code source : `https://gitlab.insee.fr/kubernetes/kubeapp/components/gitops-yaml-value-updater`
Component : `$CI_SERVER_FQDN/kubernetes/kubeapp/components/gitops-yaml-value-updater/component@2.0.0`
Date de dernière mise à jour du dépôt : 04/05/2026
Utilisaton : 
```yaml
include:
  - component: $CI_SERVER_FQDN/kubernetes/kubeapp/components/gitops-yaml-value-updater/component@2.0.0
    inputs:
      repository: "https://gitlab.com/mon-projet.git"
      branch: "main"
      file_to_change: "values.yaml"
      key_to_change: "image.tag"
      new_value: "v2.0.0"
      username: "bot-gitlab"
      password_var: "${BOT_GITLAB_TOKEN}"
      automerge: "true"
      job-prefix: "update-prod-"
      stage: "deploy"
```

#### Promote

Lien du code source : `https://gitlab.insee.fr/kubernetes/kubeapp/components/promote`
Component : `$CI_SERVER_FQDN/kubernetes/kubeapp/components/promote/application@1.0.0`
Date de dernière mise à jour du dépôt : 11/06/2026
Utilisaton : 
```yaml
include:
  - component: $CI_SERVER_FQDN/kubernetes/kubeapp/components/promote/application@1.0.0
    inputs:
      path_to_file: "helm/my-app/"
      email: "dev@insee.fr"
      environnement: "PD"
```

### ArgoCD

#### ArgoCD Refresh

Lien du code source : `https://gitlab.insee.fr/kubernetes/kubeapp/components/argocd-refresh`
Component : `gitlab.insee.fr/kubernetes/kubeapp/components/argocd-refresh@<VERSION>`
Date de dernière mise à jour du dépôt : 05/06/2026
Utilisation : (à la fin du CI)
```yaml
include:
  - component: gitlab.insee.fr/kubernetes/kubeapp/components/argocd-refresh@<VERSION>
    inputs:
      argocd_url: "[https://argocd-appli.dev.kube.insee.fr/](https://argocd-appli.dev.kube.insee.fr/)"
      gitlab_token: $GITLAB_API_TOKEN
      webhook_token: $GITOPS_ARGOCD_WEBHOOK_TOKEN_QF_APP
```

#### ArgoCD WebHook

Lien du code source : `https://gitlab.insee.fr/kubernetes/kubeapp/components/create_argocd_webhook`
Component : `$CI_SERVER_FQDN/kubernetes/kubeapp/components/create_argocd_webhook/component@0.0.1`
Date de dernière mise à jour du dépôt : 26/06/2026
Utilisation :
```yaml
stages:
  - setup

include:
  - component: $CI_SERVER_FQDN/kubernetes/kubeapp/components/create_argocd_webhook/component@0.0.1
    inputs:
      argocd_webhook_url: "https://gitops-kubernetes.developpement.insee.fr/api/webhook"
      gitlab_token: $GITLAB_API_TOKEN
      webhook_token: $GITOPS_ARGOCD_WEBHOOK_TOKEN_KUBE_DEV
      stage: "setup"
```