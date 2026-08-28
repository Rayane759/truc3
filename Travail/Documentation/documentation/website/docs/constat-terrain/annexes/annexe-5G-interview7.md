# Compte‑rendu d’interview – Plateform‑Engineering  
*(Interview anonyme, développeuse / opérations, SNDI Orléans, 5 ans d’ancienneté, équipe « Donnée de Caisse », 2 développeuses)*  

---  

## 1️⃣ Contexte & missions quotidiennes  

| Aspect | Description |
|--------|-------------|
| **Rôle général** | Développeuse / opératrice (DevOps) sur le périmètre *Donnée de Caisse* (IHM, batch, bases de données). |
| **Organisation** | Petite équipe (2 développeuses). Répartition : l’une se concentre sur l’IHM, l’autre sur le batch, mais les deux interviennent sur les deux mondes selon les besoins. |
| **Activités récurrentes** | - **Vérification matinale** (≈ 1 h) : contrôle des jobs nocturnes, état des fichiers reçus, alertes IHM, cohérence base de données. <br>- **Gestion d’incidents** : relance manuelle de jobs Kube qui plantent, déplacement de VM entre data‑centers, suivi des alertes. <br>- **Déploiements** : mise en production manuelle (≈ 2 déploiements / semaine) via Magiba, sans pipeline automatisé. <br>- **Développement** : corrections / nouvelles fonctionnalités (≈ 30 % du temps). <br>- **Maintenance de plateformes** : création / suppression de VM, mise à jour de bases, gestion de Keycloak, S3, etc. |
| **Contraintes temporelles** | - Les relances manuelles de jobs Kube peuvent bloquer le traitement jusqu’à 9 h du matin si personne n’est disponible. <br>- Les migrations de VM entre DC1 / DC2 sont fréquentes et consomment du temps. |
| **Sentiment** | Le travail d’opération est perçu comme « non créateur de valeur », source de frustration lorsqu’il occupe la majeure partie de la journée. |

---  

## 2️⃣ Stack technique & outils utilisés  

| Domaine | Outils / Technologies |
|---------|-----------------------|
| **Développement** | - **IntelliJ** (Java) <br>- **VS Code** (GitOps) <br>- **Java** (principal langage) <br>- **JavaScript** (sans React) |
| **Gestion de code** | - **GitLab** (repos multiples) |
| **Déploiement / CI‑CD** | - Déploiement **manuel** via **Magiba** <br>- **Rendeck DevOps** (occasionnel) <br>- Pas de pipeline automatisé (pas encore de CI/CD complet) |
| **Observabilité** | - **Grafana** (monitoring) <br>- **Argos CD / Argos Workflow** (utilisés quotidiennement) |
| **Infrastructure** | - **VM** (principalement) <br>- **Kube** (environnement de type conteneur / batch) <br>- **PostgreSQL** (bases) <br>- **Keycloak**, **S3** (services complémentaires) |
| **Documentation & support** | - Documentation interne (notes personnelles) <br>- PDF « roue » (référence) <br>- Chat d’équipe (Slack/Teams) <br>- Canal de la prod (site PDF) |
| **Communication & veille** | - Annonces de nouveautés par l’architecte (mail / chat) <br>- Suivi d’incidents via les canaux de chat |

---  

## 3️⃣ Irritants & points de friction  

| Type | Description |
|------|-------------|
| **Manuel / répétitif** | - Relance manuelle des jobs Kube qui plantent. <br>- Déploiement manuel (Magiba) → risque d’erreur, lenteur. |
| **Documentation fragmentée** | - Pas de documentation centralisée ou de « run‑book » unique. <br>- Doit se reposer sur des notes personnelles. |
| **Multiplicité d’outils** | - 8 + outils différents (Grafana, Argos, Rendeck, Magiba, etc.) → perte de temps pour les retrouver, pas de vue d’ensemble. |
| **Manque de visibilité** | - Pas de tableau unique listant les tickets / tâches (les tickets sont disséminés). |
| **Responsabilités floues** | - Exemple du passage Nginx → incertitude sur qui doit intervenir. |
| **Performance des outils** | - **HyperX** jugé lent → abandonné. |
| **Complexité de la configuration** | - Installation d’un nouveau poste = listes longues, pas d’automatisation. |
| **Temps de mise en place d’une plateforme** | - Environ **1 jour** même pour une plateforme déjà connue, mais perçu comme long lorsqu’il faut refaire les étapes. |
| **Absence de pipeline CI/CD** | - Pas de visibilité claire sur les étapes de build / test / déploiement → « boîte noire ». |
| **Alertes non centralisées** | - Les alertes d’incident sont parfois perdues dans les chats, pas de tableau de bord unique. |

---  

## 4️⃣ Besoins exprimés (ou implicites)  

| Besoin | Pourquoi / Contexte |
|--------|---------------------|
| **Centralisation de la documentation** | Un seul endroit où retrouver run‑books, procédures de création / suppression de VM, checklist de mise à jour, etc. |
| **Automatisation des déploiements** | Un pipeline CI/CD fiable pour éviter les déploiements manuels et réduire les erreurs. |
| **Réduction du nombre d’outils** | Rationaliser la stack (ex. regrouper monitoring, déploiement, gestion de configuration) pour limiter le temps de recherche. |
| **Visibilité sur les tickets / tâches** | Un tableau partagé (ex. Kanban) où toutes les tâches sont listées, afin d’éviter les notes personnelles dispersées. |
| **Clarification des responsabilités** | Un contrat ou une matrice RACI entre dev et prod pour chaque type d’intervention (ex. Nginx, migration, sécurité). |
| **Support / formation à l’usage des outils** | Documentation « pas à pas » et formation ciblée (ex. comment créer une VM, comment relancer un job Kube). |
| **Mécanisme de relance automatique** | Un système qui redémarre automatiquement les jobs qui plantent, ou qui alerte immédiatement la bonne personne. |
| **Interface simplifiée (clic‑bouton)** | Un outil qui, à partir d’un formulaire, génère les scripts / YAML nécessaires, tout en expliquant les étapes (pédagogie). |
| **Recherche unifiée** | Un moteur de recherche qui parcourt tous les dépôts, docs, tickets, afin de retrouver rapidement une information. |
| **Gestion des environnements homogène** | Un moyen de rendre Kube aussi « confortable » que les VM (ex. documentation, tooling). |

---  

## 5️⃣ Insights clés pour le **Platform‑Engineering**  

| Insight | Implication pour le Platform‑Engineering |
|---------|------------------------------------------|
| **Le temps passé en ops est perçu comme non‑valeur** | automatiser ces tâches libère les développeurs pour du vrai développement. |
| **Fragmentation des outils crée une surcharge cognitive** | une plateforme unifiée (ou un portail) qui regroupe monitoring, déploiement, gestion d’infrastructure serait très bénéfique. |
| **Documentation ad‑hoc = perte de connaissance** | le Platform‑Engineering doit fournir des run‑books standardisés, versionnés et facilement accessibles. |
| **Responsabilités floues génèrent des blocages** | formaliser les SLA / RACI entre dev et prod, voire intégrer ces règles dans la plateforme (ex. tickets auto‑assignés). |
| **Relance manuelle des jobs Kube = point de friction majeur** | mettre en place un orchestrateur qui détecte les échecs et relance automatiquement ou crée un ticket. |
| **Absence de pipeline CI/CD empêche la rapidité** | le Platform‑Engineering doit proposer un pipeline « as‑code » (GitOps) prêt à l’emploi, avec des templates pour les projets Java/Batch. |
| **Besoin d’une interface « clic‑bouton » avec explications** | un générateur de configuration (ex. UI qui produit YAML/Helm) avec documentation contextuelle serait très apprécié. |
| **Recherche d’information difficile** | un catalogue de services (catalogue interne) avec recherche plein‑texte faciliterait la prise en main. |
| **Performance des outils (ex. HyperX) influence l’adoption** | choisir des outils rapides, bien intégrés, ou optimiser les existants. |
| **Le besoin d’une vue globale des tâches** | un tableau de bord partagé (Kanban) intégré à la plateforme permettrait de suivre l’avancement et d’éviter les notes isolées. |

---  

## 6️⃣ Autres éléments observés  

- **Culture de la « note personnelle »** : la développeuse garde ses propres check‑lists, signe d’un manque de standardisation.  
- **Utilisation de deux environnements (VM & Kube)** : la préférence reste pour les VM, Kube est perçu comme plus opaque.  
- **Formation initiale lourde** : le premier poste a nécessité beaucoup d’autodidaxie (installation poste, configuration).  
- **Communication des nouveautés** : les annonces par l’architecte sont utiles, mais le timing peut être perdu si la personne n’est pas disponible.  
- **Attente d’un « bouton magique »** : même si elle accepte d’ouvrir des fichiers YAML, elle souhaite que le processus soit guidé et explicite.  

---  

*Ce compte‑rendu se veut factuel et ne comporte aucune recommandation ni feuille de route. Il synthétise les besoins, irritants et insights exprimés par la personne interviewée afin d’alimenter la réflexion autour du Platform‑Engineering dans votre organisation.*