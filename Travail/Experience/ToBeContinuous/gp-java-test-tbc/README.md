# Test-TBC

> 

---

## Description

Ce service expose une API REST basée sur Spring Boot.

<!-- 
Décrivez ici votre service en quelques phrases : 
- Quel problème résout-il ? 
- Qui sont ses utilisateurs ou consommateurs ? 
- Quelles sont ses principales fonctionnalités ? 
-->

## Prérequis

Assurez-vous de disposer des éléments suivants avant de démarrer :

- Java 21
- Maven (via ./mvnw inclus dans le projet)
- Docker

## Installation et démarrage

### Cloner le dépôt

```bash
git clone <URL_DU_REPO>
cd testtobecontinuous
```

### Configurer les variables d'environnement

Copiez le fichier d'exemple `.env.example` dans un nouveau fichier `.env` et renseignez les bonnes valeurs.

<!-- 
Listez ici les variables d'environnement attendues, par exemple : 

| Variable              | Description               | Exemple               | 
|-----------------------|---------------------------|----------------------| 
| SPRING_DATASOURCE_URL | URL de la base de données | jdbc:postgresql://...| 
-->

### Lancer le projet

```bash
./mvnw clean spring-boot:run
```

Le service sera disponible sur `http://localhost:8080`.

## Utilisation

<!-- 
Donnez un exemple concret d'appel à votre service, par exemple :

bash
    curl http://localhost:8080/api/v1/health

Ajoutez la réponse attendue si possible. 
-->

Exemple d'appel :

```bash
curl http://localhost:8080/actuator/health
```

### Premier endpoint

Un endpoint de démonstration est disponible :

```bash
curl http://localhost:8080/api/health
```

## Documentation API (Swagger)

Une documentation interactive de l'API est disponible via Swagger UI.

### Accès

Une fois l'application démarrée, vous pouvez accéder à :

- Interface Swagger : `http://localhost:8080/swagger-ui`
- Spécification OpenAPI (JSON) : `http://localhost:8080/api-docs`

### Utilisation de Swagger

Swagger UI permet de :

- Visualiser l’ensemble des endpoints disponibles
- Consulter les paramètres attendus
- Tester les appels directement depuis le navigateur
- Vérifier les réponses de l’API

### Bonnes pratiques

Lors de l’ajout de nouveaux endpoints :

- Ajouter `@Tag` sur chaque controller
- Ajouter `@Operation` sur chaque endpoint
- Documenter les DTO avec `@Schema` si nécessaire

Exemple :

```java
@Tag(name = "User", description = "User API")
@Operation(summary = "Get a user by ID")
```

## Stack technique

| Composant       | Technologie                                 |
|-----------------|---------------------------------------------|
| Langage         | Java 21              |
| Framework       | Spring Boot 4.0.6 |
| Build           | maven                     |
| Déploiement     | Kubernetes (via ArgoCD + Helm)              |

## Liens utiles

| Ressource         | Lien           |
|-------------------|----------------|
| Repo GitLab       | <URL_REPO>     |
| Pipeline CI       | <URL_PIPELINE> |
| ArgoCD            | <URL_ARGOCD>   |
| Catalog Backstage | <URL_BACKSTAGE>|

## Équipe

- **Responsable :** <!--Prénom NOM — prenom.nom@BLABLABLA.fr-->
- **Équipe :** team-platform
- **Support :** <!--Salon Tchap, lien vers l'outil de ticketing, etc.-->

## Statut du projet

Actif
