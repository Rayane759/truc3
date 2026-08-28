# Compte‑rendu d’interview – Plateforme Engineering  
*(interview anonyme, développeur back‑end junior, INSEE – en poste depuis septembre 2024)*  

---  

## 1. Contexte & missions quotidiennes  

| Élément | Description |
|---|---|
| **Rôle** | Développeur back‑end (API, services Java / Spring Boot). Premier poste après l’ENS AI, intégré dans l’équipe « Concevoir » (back‑end). |
| **Ancienneté** | 1 an et ½ dans l’entreprise, 9 mois dans l’équipe actuelle. |
| **Objectifs principaux** | • Implémenter de nouvelles fonctionnalités (ex. API de nomenclature). <br>• Soutenir le développeur senior (Nico) sur le back‑end. <br>• Déployer les artefacts en environnements de **dev**, **recette** et **DV** via le pipeline CI/CD. |
| **Rythme journalier** | 9 h 30 : daily stand‑up. <br>Matin : travail sur une branche feature, création de PR. <br>Après le déjeuner : revue de PR, commentaires, merges. <br>En parallèle : suivi de tickets, participation à des salons transverses, réponses aux urgences (déploiement rapide en recette). |
| **Interactions** | • Support quotidien de la part de **Laurent** (lead tech) et **Nico**. <br>• Peu d’interaction directe avec les équipes Ops / Prod ; les incidents sont remontés via le lead tech. <br>• Participation à des réunions transverses (Litech) où les évolutions de la plateforme sont présentées. |

---

## 2. Stack technique & outils utilisés  

| Domaine | Outils / Technologies |
|---|---|
| **Développement** | IntelliJ IDEA, Spring Boot 4, Java, bases de données (Beaver), scripts SQL. |
| **Contrôle de version** | GitHub (principal) + GitLab (pour les nouveaux projets). |
| **CI / CD** | GitLab CI (pipelines YAML), Argo CD (déploiement continu), Zodorz (gestion de versions d’images), snapshots Docker, labels de déploiement. |
| **Gestion de code** | Git Bash (préférence), GitHub Desktop (occasionnel). |
| **Qualité & Sécurité** | SonarQube (analyse statique), scans de vulnérabilités (CVE), couverture de tests, tests unitaires et d’intégration. |
| **Observabilité** | Alertes GitHub, notifications par mail, tableau de bord Argo CD (vérification de l’état des déploiements). |
| **Documentation** | Docs internes (repo Git), mais perçues comme peu structurées. |
| **Collaboration** | Slack / salons de discussion transverses, tickets (probablement JIRA ou équivalent). |

---

## 3. Irritants & points de friction  

| Thème | Description de l’irritant |
|---|---|
| **Multiplicité des plateformes Git** | Utilisation simultanée de GitHub (historique) et GitLab (nouveaux projets) → confusion, besoin de switcher. |
| **Documentation** | Documentation de la plateforme et des processus jugée « foireuse », difficile à retrouver, surtout pour les nouveaux. |
| **Vocabulaire & concepts** | Terminologie (snapshot, chart, label, CVE, etc.) perçue comme du « chinois », source de perte de temps. |
| **Onboarding** | Nécessité de solliciter constamment les seniors (Laurent, Nico) pour chaque nouveauté (ex. gestion des tokens, secrets). |
| **Visibilité inter‑équipes** | Peu de connaissance des travaux des autres équipes, manque de transparence sur les évolutions de la plateforme. |
| **Gestion des versions / labels** | Processus manuel de mise à jour des labels dans les fichiers YAML, source d’erreurs et de perte de temps. |
| **Alertes & monitoring** | Alertes reçues par mail, mais pas de tableau de bord centralisé ; difficulté à suivre les incidents de production. |
| **Pipeline fragile** | Quelques incidents ponctuels de CI qui bloquent les déploiements (ex. conflits de version, CVE non résolues). |
| **Manque d’autonomie** | Sentiment de dépendance à un « gatekeeper » (Laurent) pour toute modification de la chaîne de déploiement. |

---

## 4. Besoins exprimés (ou implicites)  

| Besoin | Détails |
|---|---|
| **Plateforme unifiée** | Unifier GitHub & GitLab sous une même couche GitOps, avec un seul point d’entrée pour le CI/CD. |
| **Documentation centralisée & claire** | Guide d’onboarding, glossaire des termes, documentation vivante (ex. Confluence, Wiki) accessible depuis le repo. |
| **Self‑service** | Possibilité de créer / mettre à jour des environnements, de gérer les secrets et les versions sans passer par un senior. |
| **Dashboard de visibilité** | Tableau de bord global montrant l’état des pipelines, des déploiements, des alertes, et la cartographie des environnements (dev/recette/prod). |
| **Standardisation des processus** | Convention unique pour les labels, les snapshots, les versions d’image afin d’éliminer les étapes manuelles. |
| **Formation / accompagnement** | Sessions courtes sur GitOps, Kubernetes, gestion des secrets, afin de réduire la courbe d’apprentissage. |
| **Gestion centralisée des alertes** | Système d’alertes agrégé (ex. via Slack ou un outil de monitoring) plutôt que des mails dispersés. |
| **Réduction de la dépendance au lead tech** | Rôles de « platform champion » dans chaque équipe pour partager les bonnes pratiques et répondre aux questions. |

---

## 5. Insights clés pour le **Platform‑Engineering**  

| Insight | Implication pour la plateforme |
|---|---|
| **Le junior a besoin d’une chaîne de déploiement « plug‑and‑play »** | Un workflow GitOps bien documenté, avec des templates prêts à l’emploi, accélère la productivité et diminue les tickets d’assistance. |
| **La fragmentation des outils crée du bruit** | Consolidation ou abstraction (ex. façade API) entre GitHub et GitLab réduit le contexte switching et les erreurs de configuration. |
| **Le vocabulaire technique est un frein à l’autonomie** | Un glossaire intégré dans la UI (tooltips, docs contextuelles) aide à la prise en main rapide. |
| **La visibilité inter‑équipes est quasi inexistante** | Un catalogue de services / environnements partagé (ex. Service Catalog) favorise la collaboration et la réutilisation. |
| **Les incidents de pipeline sont rares mais critiques** | Des tests de validation pré‑merge (lint, CVE, versioning) automatisés et des roll‑backs simples augmentent la confiance dans le CI. |
| **Le besoin d’un point d’entrée unique pour les alertes** | Un système de notification centralisé (ex. Alertmanager + Slack) évite la surcharge de mails et améliore la réactivité. |
| **Le besoin d’une documentation vivante** | La plateforme doit intégrer un moteur de documentation (ex. MkDocs, Docs as Code) versionné avec le code. |
| **Le support actuel repose sur quelques personnes clés** | Encourager le « platform champion » ou le « dev‑ops buddy » dans chaque squad pour diffuser les connaissances. |
| **Le développeur veut plus de contrôle sur le cycle de vie** | Exposer des UI ou CLI pour gérer les releases, les tags et les secrets sans passer par le lead tech. |

---

## 6. Autres éléments observés  

* **Structure de l’équipe** – Une petite équipe back‑end (Laurent, Nico, le participant) avec un lead tech qui centralise les décisions de plateforme.  
* **Culture de la qualité** – Utilisation de Sonar, couverture de tests, scans de vulnérabilités, mais les règles sont parfois perçues comme trop restrictives (ex. merge blocking).  
* **Gestion des urgences** – Déploiement rapide en recette même avant la validation de la PR, ce qui montre une flexibilité opérationnelle mais aussi un besoin de processus clairs pour les hot‑fixes.  
* **Évolution de la stack** – Migration progressive de GitHub vers GitLab pour les nouveaux projets, mais le basculement complet n’est pas encore réalisé.  
* **Attitude du participant** – Curieux, désireux d’apprendre, se décrit comme « débutant » mais montre une bonne compréhension des concepts de GitOps et de la chaîne CI/CD.  

---  

*Ce compte‑rendu se veut factuel et ne comporte aucune recommandation ni feuille de route. Il synthétise les besoins, irritants et insights exprimés par le développeur afin d’alimenter la réflexion sur la mise en place d’une plateforme d’ingénierie (Platform‑Engineering) adaptée à l’organisation.*