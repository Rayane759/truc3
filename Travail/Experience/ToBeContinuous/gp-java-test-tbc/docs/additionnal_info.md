# Golden Path — Java Backend Starter

Ce projet a été généré automatiquement via le Golden Path Java Backend.

**Objectif :** Fournir un socle prêt à l’emploi, standardisé, pour démarrer rapidement le développement d’un service backend.

## 1. Ce que le Golden Path a généré

Le Golden Path vous fournit un projet immédiatement exécutable, structuré selon les bonnes pratiques internes.

### Structure générale

Le projet contient :

- Un squelette Spring Boot fonctionnel
- Une organisation standard des packages Java
- Un endpoint REST minimal
- Une configuration applicative prête à l’emploi
- Un fichier de build (pom.xml)
- Une configuration Kubernetes (Helm)
- Un catalog-info.yaml pour l’intégration Backstage
- Des tests unitaires de base

### Peut-on lancer le projet immédiatement ?

Oui !

**Lancer l’application :**
`./mvnw spring-boot:run`

**Tester le endpoint exposé :**
`curl http://localhost:8080/api/health`

**Réponse attendue :**
`OK`

Cela permet de vérifier que :

- L’application démarre correctement
- L’environnement est fonctionnel

## 2. Ce qui est déjà fait pour vous

Le Golden Path prend déjà en charge un certain nombre d’éléments techniques.

- Configuration du projet
  - Dépendances Spring Boot configurées
  - Version Java définie
  - Plugin Maven prêt à l’emploi
  - Wrapper Maven inclus (`./mvnw`)

- Structure du code
  - Point d’entrée (`Application.java`)
  - Organisation des packages
  - Exemple de contrôleur REST
  - Gestion globale des erreurs

- Observabilité de base
  - Spring Boot Actuator activé
  - Endpoint `/healthcheck` disponible
  - Métriques de base exposées

- Tests
  - Test de démarrage du contexte Spring
  - Test d’un endpoint REST

- Intégration plateforme
  - Dépôt GitLab créé
  - Projet enregistré dans Backstage
  - Structure compatible Kubernetes / GitOps

Ainsi, il n'y a pas besoin de :

- Configurer Spring Boot
- Structurer le projet
- Ajouter les dépendances de base
- Créer les premiers tests

## 3. Ce qu’il vous reste à faire

### 3.1 Implémenter votre logique métier

Ajoutez votre code dans :

`src/main/java/fr/insee/.../`

Typiquement :

- Nouveaux contrôleurs (`controller/`)
- Services métier (à créer si besoin)
- Logique applicative

Le fichier `HealthController.java` peut être modifié ou supprimé.

### 3.2 Ajouter vos endpoints

Exemple :

```bash
@GetMapping("/api/users")
public List<User> getUsers() {
    ...
}
```

### 3.3 Écrire les tests associés

Les tests se trouvent dans :

`src/test/java/.../`

Vous devez :

- Ajouter des tests pour vos endpoints
- Tester votre logique métier
- Maintenir une couverture minimale

### 3.4 Gérer la configuration

Le fichier :

`src/main/resources/application.properties`

Vous pouvez :

- Ajouter vos variables applicatives
- Configurer vos accès (DB, API externes…)

### 3.5 Variables d’environnement

Créer un fichier `.env` en s'inspirant du fichier `.env.example` :

```bash
cp .env.example .env
```

Puis renseignez vos variables.

### 3.6 Ajouter des dépendances

Dans `pom.xml`, ajouter :

```bash
<dependency>
    <groupId>...</groupId>
    <artifactId>...</artifactId>
</dependency>
```

Il faut respecter :

- La cohérence avec Spring Boot
- Les versions compatibles

## 4. Fonctionnalités optionnelles (à venir)

Certaines briques pourront être activées via le Golden Path :

- Sécurité (Spring Security + OAuth2)
- Observabilité avancée (Prometheus, logs structurés)
- Gestion des secrets (Vault)

(Pour l’instant, ces fonctionnalités ne sont pas activées par défaut.)

## 5. Fichiers importants

| Fichier                | Rôle                   |
|------------------------|------------------------|
| Application.java       | Point d’entrée         |
| application.properties | Configuration          |
| pom.xml                | Dépendances            |
| README.md              | Documentation projet   |
| catalog-info.yaml      | Intégration Backstage  |
| helm/                  | Déploiement Kubernetes |

## 6. Philosophie du Golden Path

Ce projet est volontairement :

- Minimaliste
- Fonctionnel

L’objectif est de :

- Démarrer rapidement
- Ne pas imposer de logique métier
- Garantir un cadre standard

## 7. Prochaines étapes

1. Implémenter vos endpoints
2. Ajouter vos tests
3. Configurer votre environnement
4. Préparer le déploiement

## Support

En cas de question :

- Contactez l'équipe plateforme : `CONTACT_EQUIPE_PLATEFORME`
- Consultez la documentation interne : `LIEN_DOC_GP`
- Utilisez Backstage pour explorer les services existants : `LIEN_PLATEFORME`

Bon développement !
