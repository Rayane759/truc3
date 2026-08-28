# Compte‑rendu d’interview – Mise en place du Platform‑Engineering  
*(Interview anonymisée – participant : Responsable d’un groupe de maintenance applicative)*  

---  

## 1. Contexte & missions quotidiennes  

| Élément | Description |
|---|---|
| **Rôle** | Responsable d’un groupe de maintenance (≈ 7 personnes) chargé de la prise en charge de trois applications : deux en fin de vie, une « legacy » modernisée (Spring Boot / React). |
| **Activités récurrentes** | • Suivi de la production (dashboard interne, alertes, batchs). <br>• Gestion des incidents d’infrastructure (ex. : expiration de mots‑de‑passe, incidents d’environnement). <br>• Priorisation et suivi des US (user stories) de l’équipe. <br>• Pré‑préparation du travail des développeurs (formation, anticipation des difficultés, mise à disposition de scripts). <br>• Coordination avec la DSI/Production (demande de changements, suivi des tickets). |
| **Organisation** | Le chef de groupe agit comme relais entre les développeurs et la production ; il anticipe les besoins, prépare les environnements et veille à la visibilité des changements. |
| **Rythme** | Travail en itérations (sprints) ; les incidents majeurs sont traités dans le sprint en cours, les incidents critiques sont traités en urgence. |

---  

## 2. Stack technique & outils utilisés  

| Domaine | Outils / Technologies |
|---|---|
| **Applications** | Spring Boot, React, Tomcat, Apache, bases de données relationnelles, stockage d’objets (S3 / Minio). |
| **Conteneurisation / Orchestration** | Kubernetes (Kube), namespaces, YAML pour la configuration. |
| **CI / CD** | Pipelines internes (scripts RunDeck, pipelines « Majiba », templates CI‑CD). |
| **Gestion de configuration** | Tags manuels, micro‑segmentation, scripts maison. |
| **Monitoring & logs** | Dashboard maison (agrégation de logs, suivi de batchs, alertes). |
| **Gestion de fichiers / objets** | Applisher, S3, Minio (transfert de données entre services). |
| **Outils de support** | RunDeck (exécution de jobs), Spock (service transversal), Gravity (service de validation), libéa (support interne). |
| **Environnements de dev** | VM classiques, environnements « Kube » (K8s), outils portables, IDE (Eclipse, VS Code). |
| **Sécurité** | Double authentification, validation manuelle des requêtes, gestion des mots‑de‑passe applicatifs. |

---  

## 3. Irritants & points de friction  

| Catégorie | Description détaillée |
|---|---|
| **Lenteur / manque de visibilité** | • Déploiement via **Majiba** très lent (1 h vs 5 min en manuel). <br>• Absence de suivi en temps réel du déroulement des pipelines. |
| **Transfert de tâches Ops vers les devs** | • Opérations de micro‑segmentation, taggage, changements d’infrastructure imposées aux développeurs sans automatisation ni support dédié. |
| **Communication** | • Multiplicité de canaux (≈ 50 chats) → perte d’information. <br>• Annonces d’incidents ou de changements souvent tardives ou inexistantes (ex. : expiration de mots‑de‑passe, arrêt d’un service). |
| **Instabilité des services transverses** | • Services comme **Spock**, **Gravity**, **Applisher** plantent ou changent de version sans préavis, obligeant les équipes à bricoler des solutions temporaires. |
| **Manque de standardisation** | • Absence de processus automatisé pour la mise à jour des tags ou la micro‑segmentation. <br>• Chaque équipe utilise ses propres scripts, ce qui rend la coordination difficile. |
| **Outils qui ne répondent pas aux besoins** | • **Majiba** jugé moins performant que les solutions manuelles précédentes. <br>• Outils de stockage (Minio) qui disparaissent ou changent de console du jour au lendemain. |
| **Charge cognitive** | • Nécessité de jongler avec de nombreux « sources de vérité » (50 services différents) → impossible de garder une vision globale. |
| **Déploiement d’applications legacy** | • Besoin de ré‑implémenter des fonctions (ex. : red‑limit, filtrage) dans le code applicatif faute d’outils adéquats. |

---  

## 4. Besoins exprimés (ou implicites)  

| Besoin | Détails |
|---|---|
| **Visibilité & traçabilité** | Un tableau de bord unique qui montre l’état des pipelines, les temps d’attente et les raisons de lenteur. |
| **Automatisation des tâches Ops** | Tagging, micro‑segmentation, mise à jour de configuration automatisées et transparentes pour les développeurs. |
| **Communication centralisée** | Un canal ou une plateforme unique (type intranet ou outil de notification) où sont publiés incidents, changements, dates de mise à jour, jalons. |
| **Stabilité des services transverses** | Garanties de disponibilité et de versionnage contrôlé (ex. : Spock, Gravity) ou alternatives fiables. |
| **Templates & kits de démarrage** | Templates CI‑CD prêts à l’emploi (variables à remplir) pour chaque stack (Java / Spring, React, Kube, etc.). |
| **Réduction de la charge cognitive** | Un point d’entrée unique pour les informations d’infrastructure (catalogue de services, documentation à jour). |
| **Support d’autonomie** | Outils qui permettent aux équipes de déployer sans dépendre d’un ticket à chaque modification d’infrastructure. |
| **Qualité & tests automatisés** | Couverture de tests suffisante (≥ 75 %) pour valider les montées de version sans risque. |
| **Gestion du cycle de vie des environnements** | Processus clair pour créer, mettre à jour et supprimer des namespaces / environnements de dev, avec des temps d’attente prévisibles (ex. : quelques heures, pas plusieurs jours). |
| **Gestion des licences & IA** | Accès à des outils d’IA (ex. : Mistral) intégrés aux IDE sans contraintes de licence ou de compatibilité. |

---  

## 5. Insights clés pour le **Platform‑Engineering**  

| Insight | Implication pour la plateforme |
|---|---|
| **Le temps de déploiement est un facteur de friction majeur** | La plateforme doit offrir des pipelines rapides, observables et capables de rendre compte des goulots d’étranglement. |
| **Les développeurs sont surchargés par des tâches d’infrastructure** | Un vrai **self‑service** (tagging, micro‑segmentation, gestion des namespaces) doit être intégré, avec des abstractions qui masquent la complexité. |
| **La communication est fragmentée** | Un **hub de communication** (notifications, road‑maps, changelogs) est indispensable pour éviter les surprises et les doublons. |
| **Les services transverses sont des points de rupture** | La plateforme doit garantir la **fiabilité** et la **gestion de version** de ces services, ou proposer des alternatives standardisées. |
| **Les équipes apprécient les templates prêts à l’emploi** | Fournir un **catalogue de templates** (CI/CD, infra as code) pour chaque stack technologique réduit le temps de mise en place et les erreurs. |
| **La visibilité sur les environnements est cruciale** | Un **catalogue d’environnements** (catalogue de services, état, SLA) doit être accessible en temps réel. |
| **La qualité du code et les tests automatisés sont attendus** | La plateforme doit faciliter l’intégration de **tests de couverture** et de **qualité** dans le pipeline, afin que les montées de version soient sûres. |
| **Le besoin d’autonomie coexiste avec la nécessité d’un point de contact unique** | Un **owner de plateforme** (ou équipe dédiée) qui centralise les demandes, tout en offrant des APIs/self‑service, répond à ce double besoin. |
| **Les changements d’outils doivent être planifiés et communiqués** | La gouvernance de la plateforme doit inclure un **processus de dépréciation** et de **migration** clairement communiqué. |
| **Les contraintes de licence et d’intégration d’IA** | La plateforme doit prévoir un **catalogue de licences** et des **connecteurs** pour les outils IA afin d’éviter les blocages. |

---  

## 6. Autres éléments pertinents  

* **Culture du “craft”** : l’équipe a investi dans la modernisation (Spring Boot, React) et valorise la qualité du code. La plateforme doit soutenir cette dynamique en facilitant les bonnes pratiques.  
* **Gestion des incidents** : le tableau de bord maison est apprécié ; il pourrait être intégré à la plateforme pour offrir une visibilité globale à toutes les équipes.  
* **Ressources humaines** : réduction d’effectifs côté Ops a entraîné un transfert de charge vers les devs ; la plateforme doit compenser ce déséquilibre.  
* **Évolution technologique** : la migration vers des standards open‑source (Spring, Kubernetes) est en cours ; la plateforme doit rester agnostique et évolutive pour accueillir de futurs changements (ex. : migration de Minio vers S3).  

---  

*Ce compte‑rendu se veut factuel et ne comporte aucune recommandation ni feuille de route. Il synthétise les besoins, irritants et insights exprimés par le participant afin d’alimenter la réflexion autour du Platform‑Engineering dans l’entreprise.*