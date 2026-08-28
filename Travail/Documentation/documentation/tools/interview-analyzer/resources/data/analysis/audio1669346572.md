# Compte‑rendu d’interview – Étude d’opportunité du **Platform‑Engineering**  
*(Interview anonymisée – développeur full‑stack senior, 7‑8 ans d’expérience, intervenant sur la filière « enquête » du produit Sabian)*  

---  

## 1. Contexte & missions quotidiennes  

| Aspect | Description |
|--------|-------------|
| **Rôle** | Développeur front‑et‑back, responsable du développement de nouvelles fonctionnalités mutualisées pour la filière d’enquête, du suivi de production et de l’assistance aux utilisateurs. |
| **Missions principales** | - Développement de fonctionnalités (API questionnaires, front‑questionnaires, micro‑services). <br>- Gestion des mises en production (déploiements, hot‑fixes). <br>- Support de production : analyse de logs, requêtes DB, revue de code, assistance utilisateur (debug via le navigateur). <br>- Participation à la migration de modules (ex. migration vers « Kube », migration de bases PostgreSQL). |
| **Rythme de travail** | - Début de journée : suivi d’incidents (si présents) → tickets TEF. <br>- Réunions de conception (environ 1 × 2 semaines). <br>- Après‑midi : développement, revue de code, réunions d’équipe, suivi de production. |
| **Responsabilité** | Responsable du code qu’il peut modifier ; dépend de l’équipe Ops pour la création/gestion des VM et des droits d’accès. |

---

## 2. Stack technique & outils utilisés  

| Domaine | Technologies / Outils |
|---------|-----------------------|
| **Langages** | Java (Spring Boot), JavaScript/TypeScript (front), SQL (PostgreSQL). |
| **IDE** | IntelliJ IDEA (Java), VS Code (JS) – extension *ProGeek* pour VS Code. |
| **Frameworks** | Spring Boot (versions récentes), micro‑services (architecture modulaire). |
| **Conteneurisation / CI‑CD** | Docker (utilisé dans les pipelines GitLab), GitLab CI (templates, métacomposants), Nexus (artifacts), Sonar (qualité code), Magiba (déploiement prod). |
| **Gestion de configuration / orchestration** | Rundeck (jobs d’automatisation), Majiba (API interne), Renet (création de VM), Keycloak (authentification), observabilité maison (alerting, logs, métriques). |
| **Bases de données** | PostgreSQL (2 instances parallèles), JMS (utilisé ponctuellement). |
| **Monitoring / alerting** | Alerting interne (sons, mails), tableau de bord « observabilité » (affiche erreurs, CVE, volumes). |
| **Outils de support** | Outils maison de suivi d’incidents (canal métier dédié), tickets, documentation partagée (pas toujours centralisée). |
| **Environnements** | VM (déploiement sur infrastructure interne), Kube (en cours de migration), micro‑frontend (actuellement sans CSP, avec problèmes de headers HSTS). |

---

## 3. Irritants & points de friction  

| Domaine | Points de friction |
|---------|-------------------|
| **Déploiements** | - Fréquence variable : certaines API (questionnaires) sont mises à jour mensuellement, d’autres très rares (risques de régression). <br>- Processus de validation multi‑modules lourd : besoin que tous les modules soient synchronisés avant de déployer. |
| **Micro‑services / micro‑frontend** | - Gestion des headers (CSP, HSTS) difficile à cause du micro‑frontend. <br>- Absence de CSP → exposition à des risques de sécurité. |
| **Outils d’automatisation** | - Rundeck peu documenté : création/édition de jobs peu intuitive, références par ID uniquement. <br>- Majiba nécessite un token manuel → friction pour les appels API. |
| **Observabilité** | - Alerting bruyant (son, mail) mais peu de granularité : difficile de filtrer les alertes non critiques. <br>- Pas de tableau de bord unifié pour chaque application (doit naviguer entre plusieurs pages). |
| **Documentation** | - Documentation dispersée (pages multiples, pas de point central). <br>- Manque de self‑service : les développeurs doivent souvent demander de l’aide pour des tâches simples (ex. création de VM, configuration réseau). |
| **Environnement de travail** | - Installation locale d’outils (JDK, extensions) parfois lourde et peu automatisée. <br>- Migration de navigateurs (Edge vs. Firefox) impacte le stockage local des données (offline). |
| **Gestion des droits** | - Processus de demande de ressources (VM, accès) perçu comme « one‑shot » et parfois lent. |
| **CI/CD** | - Templates CI partagés mais manque de visibilité sur les valeurs injectées (difficulté à tracer les paramètres finaux). <br>- Charte multi‑module rend difficile le raccord fin des pipelines avec les valeurs d’application. |

---

## 4. Besoins exprimés (ou implicites)  

| Besoin | Détails |
|--------|---------|
| **Simplification du déploiement** | Outils qui permettent de déployer un micro‑service sans devoir synchroniser manuellement tous les modules associés. |
| **Documentation centralisée & self‑service** | Un hub unique contenant la documentation des IHM, des pipelines CI, des procédures d’on‑boarding (création VM, token Majiba, etc.). |
| **Meilleure observabilité** | Dashboard unique par application regroupant logs, alertes, métriques, liens vers les environnements (dev, test, prod). |
| **Automatisation plus fiable** | Jobs Rundeck plus documentés, possibilité de créer/éditer via UI plutôt que par ID, gestion des tokens automatisée. |
| **Gestion des headers de sécurité** | Support natif pour CSP/HSTS dans le cadre du micro‑frontend, afin d’éviter les work‑arounds manuels. |
| **Standardisation des CI/CD** | Templates CI qui exposent clairement les variables d’environnement, avec validation automatique des valeurs. |
| **Support d’infrastructure** | Processus de création de VM plus rapide (ex. via API) et visibilité sur les ressources allouées. |
| **Gestion des navigateurs offline** | Stratégie claire pour la synchronisation des données locales entre différents navigateurs (Edge, Firefox, Chrome). |
| **Formation & montée en compétences** | Accès à des guides « self‑service » pour les briques techniques (Docker, Kubernetes, observabilité) afin de réduire la dépendance à un seul « expert DevOps ». |

---

## 5. Insights clés pour le **Platform‑Engineering**  

| Insight | Implication pour le Platform‑Engineering |
|---------|------------------------------------------|
| **Le « friction » principal provient de la coordination multi‑module** | Une plateforme qui orchestre les dépendances entre micro‑services et automatise les déploiements groupés (ex. “release train”) pourrait réduire le temps de mise en prod et le risque d’erreur. |
| **Les développeurs souhaitent un point d’entrée unique** | Un **Developer Portal** (catalogue de services, docs, UI d’accès aux pipelines, tokens) répondrait à la demande de centralisation et de self‑service. |
| **Observabilité fragmentée** | Un **Observability Layer** partagé (ex. Grafana/Prometheus + alert routing) avec des dashboards pré‑configurés par service faciliterait le suivi et la résolution d’incidents. |
| **Automatisation (Rundeck, Majiba) manque de UX** | Le Platform‑Engineering doit fournir des **wrappers** ou des **extensions UI** qui masquent la complexité (ex. génération de jobs via formulaire, gestion de tokens via SSO). |
| **Sécurité des micro‑frontends** | Intégrer la gestion des politiques CSP/HSTS dans le pipeline de build (ex. via plugins) pour éviter les correctifs manuels. |
| **Documentation et onboarding** | Un **knowledge base** versionnée, liée aux dépôts Git, avec des guides d’on‑boarding automatisés (scripts d’installation, Docker‑compose) réduirait le temps de mise en route des nouveaux développeurs. |
| **Gestion des environnements de test** | Provisionner des environnements “sandbox” à la demande (via infra‑as‑code) pour tester les migrations de navigateurs et les scénarios offline. |
| **Processus de demande de ressources** | Mettre en place un **catalogue de services cloud** (VM, bases, secrets) avec approbation automatisée afin de réduire les délais de création. |
| **Formation continue** | Proposer des **workshops** et des **labs** (ex. CI/CD, observabilité) intégrés à la plateforme pour que chaque développeur devienne autonome sur les briques clés. |

---

## 6. Autres éléments notables  

* **Culture DevOps déjà partielle** – le développeur se décrit comme « U‑Build it, U‑Run it » mais estime que la partie « Run it » (monitoring, alerting, incident handling) reste lourde et peu intégrée.  
* **Migrations récurrentes** – plusieurs migrations (Kube, PostgreSQL, micro‑frontend) sont en cours ou prévues, ce qui crée une charge ponctuelle importante et nécessite un support de plateforme robuste.  
* **Gestion des incidents** – le suivi se fait via un canal métier dédié, mais l’automatisation de la détection et de la résolution (ex. auto‑remédiation) est limitée.  
* **Ressources humaines** – un seul « expert DevOps » (nommé Eric) porte une grande partie de la charge ; risque de silo de connaissances.  
* **Communication interne** – les informations sur les évolutions d’infrastructure (ex. fin de service, nouvelles versions) sont diffusées via divers canaux (mail, intranet, chat) sans centralisation, ce qui rend la veille difficile.  

---  

*Ce compte‑rendu se veut factuel et ne comporte aucune recommandation ou feuille de route. Il synthétise les besoins, irritants et insights exprimés par l’interviewé afin d’alimenter l’étude d’opportunité du Platform‑Engineering.*  