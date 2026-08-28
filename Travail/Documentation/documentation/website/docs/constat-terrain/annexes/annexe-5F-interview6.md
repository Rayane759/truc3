# Compte‑rendu d’interview – Plateforme Engineering  
*(interview anonyme – développeur Java/TS, arrivé fin 2025)*  

---  

## 1. Contexte & missions quotidiennes  

| Élément | Description |
|---|---|
| **Poste** | Développeur full‑stack : maintien et évolution de nouvelles fonctionnalités sur deux applications internes (« Compass » et « Gardien »). |
| **Ancienneté** | Arrivé en décembre 2025, après un master MIAGE et une alternance. |
| **Rôle principal** | *Maintain & develop new features* – refonte d’IHM, correction de bugs, montées de version, gestion de CVE. |
| **Organisation du travail** | - 9 h → ouverture de l’IDE. <br> - Consultation du backlog (GitLab ou Tuleap) pour choisir un ticket non assigné. <br> - Collaboration avec deux collègues (Colin & David) pour la priorisation. <br> - Conception rapide (draw.io) → implémentation → tests → merge request. <br> - Déploiement (dev → prod) via les pipelines CI/CD. |
| **Rituels** | - Weekly sur chaque projet (Compas & Gardien). <br> - Un weekly supplémentaire le mercredi (DevOps / Kube). <br> - Pas de daily stand‑up (habitude précédente, mais pas imposé). |
| **Déploiements** | 1 – 4 fois par semaine selon le besoin (features, bugs, correctifs de sécurité). |
| **Support** | Assistance ponctuelle auprès de l’équipe «Kube » (proxy, namespace) et de l’équipe « Gardien » (variables d’environnement). |

---

## 2. Stack technique & outils utilisés  

| Domaine | Outils / Technologies |
|---|---|
| **Back‑end** | Java 17, Spring Boot (3 → 4 en cours), Maven (POM), GitLab CI |
| **Front‑end** | TypeScript, React, Visual Studio Code |
| **IDE** | IntelliJ IDEA (back), VS Code (front) |
| **Gestion de tickets** | GitLab backlog, Tuleap (pour Gardien) |
| **CI / CD** | GitLab CI, Argo CD, Helm (chart générique via méta‑composants), run‑deck (migrations DB) |
| **Conteneurisation** | Docker (images, tags), Kubernetes «Kube » (déploiement) |
| **Secrets / Auth** | Vault (gestion de secrets), Keycloak (appelé « Kicklock ») |
| **Qualité & Sécurité** | SonarQube, Trivy, Tricium (CVE), lint/formatters |
| **Tests** | Anciennement Cypress (requiert image Docker), maintenant VTest |
| **Documentation / Design** | draw.io (schémas fonctionnels), Markdown (docs internes) |
| **Assistance IA** | Agent Mistral (aide à la rédaction de code, recherche d’info) |
| **Autres** | Metacomponents (bibliothèque interne « Île »), GitOps release, GitLab pipelines standards |

---

## 3. Irritants & points de friction  

| Type | Description |
|---|---|
| **Onboarding** | Installation du poste de travail peu documentée → perte de temps pour configurer IDE, accès aux repos, variables d’environnement. |
| **CI / CD** | - Méta‑composants de Lille c'est super ! Des défauts sur le fait qu'ils créent automatiquement des tags ; le développeur ne contrôle pas toujours ce comportement. <br> - Absence d’intégration Cypress prête à l’emploi (image Docker à fournir manuellement). <br> - Documentation des pipelines parfois « au hasard », pas de ligne directrice claire entre les équipes. |
| **Gestion des secrets** | Multiplicité d’outils (Vault, Keycloak) → besoin de connaître les conventions de chaque projet. |
| **Standardisation** | Chaque équipe (Nantes, Orléans, etc.) suit ses propres patterns ; manque d’une « ligne directrice » macro pour les conventions de code, de CI, de versionning. |
| **Communication inter‑équipes** | - Nécessité de solliciter l’équipe Kube pour des proxies ou namespaces. <br> - Canaux de discussion (Slack, IDDA, etc.) existent mais sont parfois sous‑utilisés ou peu structurés. |
| **Déploiement** | Parfois blocage sur la promotion d’image Docker (problème de token) → nécessite un suivi manuel. |
| **Visibilité des outils** | Certains outils (ex. Argo CD, Helm chart générique) sont « utilisés en arrière‑plan » sans que le développeur ne voie clairement leur configuration. |
| **Serverless** | Peu d’usage de fonctions Lambda / serverless alors que le contexte (coût, scalabilité) le permettrait. |

---

## 4. Besoins exprimés (ou implicites)  

| Besoin | Pourquoi / Contexte |
|---|---|
| **Documentation d’onboarding** | Guide pas à pas pour préparer le poste, configurer les accès, installer les outils (IDE, secrets, proxy). |
| **Templates CI/CD unifiés** | Un jeu de pipelines « starter » (GitLab + Argo CD) avec conventions claires (tags, versionning, secrets). |
| **Visibilité des métacomposants** | Documentation sur le fonctionnement des tags automatiques, comment les désactiver ou les personnaliser. |
| **Standardisation des bonnes pratiques** | Ligne directrice macro (ex. version Spring Boot, conventions de branche, naming) partagée entre toutes les équipes. |
| **Gestion centralisée des secrets** | Interface unique (ex. Vault) avec documentation d’usage pour Vault / Keycloak. |
| **Support serveur / serverless** | Étude de faisabilité et guide d’utilisation de fonctions Lambda ou autres services serverless pour réduire la dépendance aux VM/Kube. |
| **Amélioration du suivi des incidents** | Processus plus fluide pour les blocages de promotion d’image (tokens, droits) – alertes automatiques, run‑book. |
| **Meilleure visibilité des canaux** | Index des canaux (Slack, IDDA, etc.) avec description du sujet couvert, afin que les développeurs sachent où poser leurs questions. |
| **Outils de design rapide** | Intégration d’un outil de prototypage (ex. Figma, même draw.io) dans le flux de travail pour les nouvelles features. |

---

## 5. Insights clés pour le **Platform‑Engineering**  

| Insight | Implication pour la plateforme |
|---|---|
| **Les développeurs portent déjà la majeure partie du DevOps** (build, test, déploiement) | la plateforme doit **simplifier** ces étapes, pas les dupliquer. |
| **Le manque de standardisation crée du temps perdu** (ex. tags automatiques, conventions de CI) | un **catalogue de patterns** (templates, best‑practices) serait très bénéfique. |
| **L’onboarding technique est un point de friction majeur** | un **« developer‑experience kit »** (scripts d’installation, documentation interactive) accélérerait la prise de fonction. |
| **Les métacomposants sont puissants mais opaques** | fournir **une couche de visibilité** (logs, UI de configuration) aiderait à garder le contrôle. |
| **La gestion des secrets est fragmentée** | centraliser via un **secret‑manager** avec API unifiée et documentation claire. |
| **Les équipes utilisent des outils similaires mais sans gouvernance commune** | instaurer **une gouvernance de plateforme** (ex. comité de standards) pour aligner les pipelines, les versions de framework, les conventions de nommage. |
| **Le besoin de serverless est latent** | la plateforme devrait offrir **des modules serverless prêts à l’emploi** (templates Lambda, triggers) pour les cas d’usage simples. |
| **Les incidents de promotion d’image sont récurrents** | automatiser la **gestion des tokens** et les **vérifications de droits** dans le pipeline. |
| **Les canaux de communication sont nombreux mais peu structurés** | créer un **hub central** (ex. Confluence, Notion) listant les canaux, les owners, les sujets. |
| **L’assistance IA (Mistral) est déjà utilisée** | intégrer **des assistants IA** dans la plateforme (ex. suggestions de CI, génération de code) pour réduire le temps de recherche. |

---

## 6. Autres éléments pertinents  

* **Temps estimé pour créer un nouvel environnement** : < ½ jour (déploiement de nouvelles variables, secrets, chart).  
* **Fréquence des réunions** : weekly uniquement, ce qui montre une culture de **low‑ceremony** mais peut laisser des silos d’information.  
* **Culture du « you build it, you run it »** est partiellement appliquée ; le développeur se sent responsable du code en production, mais certaines tâches (ex. gestion du Kube) restent externalisées.  
* **Utilisation d’outils de visualisation** (draw.io) montre un besoin de **documentation fonctionnelle** avant le codage.  
* **Le développeur apprécie la visibilité sur les pipelines** (ex. étapes de formatage, sécurité, Sonar) – cela renforce la confiance dans le processus de livraison.  

---  

*Ce compte‑rendu se veut factuel et ne contient aucune recommandation ou feuille de route. Il synthétise les besoins, irritants et insights exprimés par l’interviewé afin d’alimenter la réflexion autour d’une éventuelle mise en place du Platform‑Engineering dans l’entreprise.*