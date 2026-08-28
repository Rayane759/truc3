# Comment construire un bon Golden Path ?

## Quelles propriétés doit respecter un bon Golden Path ?

Le Golden Path est conçu pour être :

- **Facile à utiliser**
- **Rapide à adopter**
- **Aligné avec les standards internes**

On peut l'utiliser pour créer de nouveaux services, déployer des
applications, configurer des environnements, etc.

### Flexibilité

Le Golden Path n'est pas obligatoire.

En cas de besoin (besoins spécifiques, contraintes techniques), il est
possible de s'en écarter et/ou d'adapter les configurations générées.

Cependant, cela implique généralement de gérer soi-même les choix
techniques, la configuration, la maintenance, etc.

------------------------------------------------------------------------

### Transparence

Les éléments générés (code, configuration, templates) restent
accessibles et modifiables.

Le Golden Path ne doit pas cacher les détails de l'infrastructure qu'il
construit. Il est important que :

- Les fichiers soient compréhensibles
- Les choix techniques soient explicites
- Les développeurs puissent garder le contrôle

------------------------------------------------------------------------
------------------------------------------------------------------------

## Comment y parvenir ?

Créer un bon Golden Path consiste à **concevoir une expérience développeur optimisée**.
Sa construction repose sur plusieurs principes.

------------------------------------------------------------------------

### 1. Partir des besoins réels des développeurs

Un Golden Path efficace doit répondre à des cas d'usage concrets.

- Identifier les **tâches fréquentes** (déploiement, CI/CD, observabilité...)
- Analyser les **points de friction majeurs**
- Prioriser les scénarios à forte valeur

**Objectif :** Résoudre des problèmes réels, pas imposer une abstraction.

------------------------------------------------------------------------

### 2. Standardiser les cas les plus courants

Le Golden Path doit **couvrir les plus grands besoins** avec **une solution simple**.

- Définir des conventions (structure de projet, observabilité, sécurité...)
- Fournir des **templates prêts à l'emploi**
- Réduire le nombre de décisions à prendre

Créer une route **Route pavée** pour rendre le bon chemin le plus simple à suivre.

------------------------------------------------------------------------

### 3. Simplifier

Un bon Golden Path doit réduire la complexité perçue par les développeurs.

- Limiter le nombre d'outils et de choix à faire
- Masquer la complexité inutile (sans la supprimer totalement)
- Fournir des interfaces simples (CLI, templates, portail)

L'objectif est de permettre aux développeurs de se concentrer sur
leur métier, pas sur l'infrastructure.

------------------------------------------------------------------------

### 4. Fournir une expérience "self-service"

Le Golden Path doit être **autonome et accessible**.

- Création de projets en quelques étapes
- Déploiement automatisé
- Documentation claire

Un développeur ne doit pas dépendre d'une autre équipe pour démarrer.

------------------------------------------------------------------------

### 5. Itérer en continu avec les utilisateurs

Un Golden Path n'est jamais réellement "terminé".

- Recueillir du feedback (usage réel, difficultés)
- Mesurer l'adoption
- Améliorer en continu

**Approche produit :** le Golden Path est un **produit** qui évolue constamment.

------------------------------------------------------------------------

### 6. Favoriser l'utilisation

L'usage du Golden Path doit être **voulu**, pas contraint.

- Être l'alternative la plus simple
- Être bénéfique (gain de temps, réduction d'erreurs)

Si les développeurs le contournent, c'est qu'il est mal conçu.

------------------------------------------------------------------------

### 7. Assurer la cohérence et la gouvernance

Le Golden Path est un vecteur de standardisation.

- Intégrer les bonnes pratiques (sécurité, observabilité, CI/CD...)
- Garantir la conformité aux standards internes
- Maintenir une cohérence entre les différents projets

Il permet d'aligner les pratiques le plus simplement possible.

------------------------------------------------------------------------

### 8. Documenter et rendre explicite

Un Golden Path doit être compréhensible sans effort.

- Documentation orientée usage (quickstart, exemples)
- Explication des choix techniques
- Cas d'usage couverts / non couverts

La documentation fait partie intégrante du Golden Path.

------------------------------------------------------------------------
------------------------------------------------------------------------

## Conclusion

Construire un bon Golden Path consiste à :

- **Simplifier** l'expérience développeur
- **Standardiser** sans contraindre les utilisateurs
- **Automatiser** sans masquer complètement l'infrastructure sous-jacente
- **Itérer** comme un produit
