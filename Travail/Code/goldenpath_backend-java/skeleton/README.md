# ${{ values.name }}

> ${{ values.description }}

---

## Description

<!--
    Décrivez ici votre service en quelques phrases :
    - Quel problème résout-il ?
    - Qui sont ses utilisateurs ou consommateurs ?
    - Quelles sont ses principales fonctionnalités ?
-->

## Prérequis

Assurez-vous de disposer des éléments suivants avant de démarrer :

- Java ${{ values.javaVersion }}
- Maven <!-- ou Gradle ??? -->
- Docker
{%- if values.hasVault %}
- Accès à Vault (voir [la documentation Vault]([LIEN_DOC_VAULT](https://gitlab.insee.fr/iahs/secrets/documentation/doc-publique/-/wikis/home)))
{%- endif %}

## Installation et démarrage

### Cloner le dépôt

```bash
git clone <URL_DU_REPO>
cd ${{ values.artifactId }}
```

### Configurer les variables d'environnement

Copiez le fichier d'exemple et renseignez les valeurs :

```bash
cp .env.example .env
# Éditez .env avec vos valeurs
```

<!--
    Listez ici les variables d'environnement attendues, par exemple :
    | Variable              | Description                  | Exemple              |
    |-----------------------|------------------------------|----------------------|
    | SPRING_DATASOURCE_URL | URL de la base de données    | jdbc:postgresql://...|
-->

### Lancer le projet

```bash
./mvnw spring-boot:run
```

Le service sera disponible sur `http://localhost:8080`.

{%- if values.hasObservability %}
Les métriques Prometheus sont exposées sur : `http://localhost:8080/actuator/prometheus`
{%- endif %}

## Utilisation

<!--
    Donnez un exemple concret d'appel à votre service, par exemple :

    ```bash
    curl http://localhost:8080/api/v1/health
    ```

    Ajoutez la réponse attendue si possible.
-->

## Stack technique

| Composant       | Technologie                                 |
|-----------------|---------------------------------------------|
| Langage         | Java ${{ values.javaVersion }}              |
| Framework       | Spring Boot ${{ values.springBootVersion }} |
| Build           | ${{ values.buildTool }}                     |
{%- if values.hasSecurity %}
| Sécurité        | Spring Security + Keycloak (OAuth2/OIDC)    |
{%- endif %}
{%- if values.hasObservability %}
| Observabilité   | Micrometer + Prometheus + Logback JSON      |
{%- endif %}
{%- if values.hasVault %}
| Secrets         | Spring Cloud Vault                          |
{%- endif %}
| Déploiement     | Kubernetes (via ArgoCD + Helm)              |

## Liens utiles

| Ressource            | Lien                                    |
|----------------------|-----------------------------------------|
| Repo GitLab          | <URL_REPO>                              |
| Pipeline CI          | <URL_PIPELINE>                          |
| ArgoCD               | <URL_ARGOCD>                            |
{%- if values.hasObservability %}
| Grafana              | <URL_GRAFANA>                           |
{%- endif %}
| Catalog Backstage    | <URL_BACKSTAGE>                         |

## Équipe

- **Responsable :** <!--Prénom NOM — prenom.nom@insee.fr-->
- **Équipe :** ${{ values.team }}
- **Support :** <!--Salon Tchap, lien vers l'outil de ticketing, etc.-->

## Statut du projet

<!--
    Indiquez le statut actuel :
    - Actif — développement en cours
    - Maintenance — plus de nouvelles fonctionnalités, correctifs uniquement
    - Archivé — projet arrêté
-->

Actif
