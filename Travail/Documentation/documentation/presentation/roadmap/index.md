---
marp: true
theme: default
paginate: true
size: 16:9
header: "Plateforme Engineering - Equipe DevExperience"
footer: "Insee — Document interne"
style: |
  section {
    font-family: 'Calibri', 'Arial', sans-serif;
    font-size: 26px;
    padding: 50px 60px;
  }
  section.title {
    background: linear-gradient(135deg, #1E2761 0%, #0A1738 100%);
    color: #FFFFFF;
    justify-content: center;
    text-align: center;
  }
  section.title h1 { font-size: 60px; color: #FFFFFF; border: none; margin-bottom: 20px; }
  section.title h2 { font-size: 30px; color: #CADCFC; font-weight: normal; }
  section.section {
    background: #1E2761;
    color: #FFFFFF;
    justify-content: center;
    text-align: center;
  }
  section.section h1 { font-size: 56px; color: #FFFFFF; border: none; }
  section.section p { color: #CADCFC; font-size: 26px; margin-top: 20px; }
  h1 { color: #1E2761; border-bottom: 3px solid #1E2761; padding-bottom: 10px; font-size: 38px; margin-bottom: 30px; }
  h2 { color: #1E2761; font-size: 30px; }
  h3 { color: #3D4F8F; font-size: 22px; margin-top: 0; }
  strong { color: #1E2761; }
  ul { font-size: 26px; }
  li { margin: 10px 0; }
  table { font-size: 22px; margin: 0 auto; width: 100%; }
  th { background: #1E2761; color: #FFFFFF; padding: 12px; text-align: left; }
  td { padding: 12px; vertical-align: top; }
  tr:nth-child(even) { background: #F4F6FB; }
  .lead {
    font-size: 30px;
    text-align: center;
    color: #3D4F8F;
    margin: 20px 0;
  }
  .grid5 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
    gap: 20px;
    margin-top: 20px;
  }
  .grid4 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 20px;
    margin-top: 20px;
  }
  .grid3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
    margin-top: 20px;
  }
  .grid2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin-top: 20px;
  }
  .card {
    background: #F4F6FB;
    border-left: 4px solid #1E2761;
    padding: 18px 20px;
    border-radius: 4px;
  }
  .card h3 { margin: 0 0 10px 0; }
  .card p { margin: 0; font-size: 20px; }
  .pros, .cons {
    padding: 18px 22px;
    border-radius: 4px;
  }
  .pros { background: #E8F5E9; border-left: 5px solid #2E7D32; }
  .cons { background: #FFEBEE; border-left: 5px solid #C62828; }
  .pros h3 { color: #2E7D32; }
  .cons h3 { color: #C62828; }
  .pros ul, .cons ul { margin: 0; padding-left: 20px; font-size: 22px; }
  .pros li, .cons li { margin: 6px 0; }
  .keypoint {
    background: #FFF8E1;
    border-left: 5px solid #F9A825;
    padding: 16px 22px;
    margin-top: 20px;
    font-size: 24px;
  }
  .scope-in { color: #2E7D32; font-weight: bold; }
  .scope-out { color: #C62828; font-weight: bold; }
  .grid5 .card .promise {
    font-size: 0.9em;
    font-weight: 700;
    color: #16213e;
    margin: 0;
  }
  .grid5 .card .detail {
    font-size: 0.72em;
    color: #66707d;
    margin: 0.35em 0 0 0;
  }
  .grid5 .card.win {
    border-color: #1e7e4f;
    background: #eef7f1;
  }
  .grid5 .card.win h3 {
    border-bottom-color: #1e7e4f;
  }
  .quickwin {
    border-color: #1e7e4f;
    background: #eef7f1;
  }
---

<!-- _class: title -->

# Feuille de route Platform Engineering

## Un phasage progressif, du quick win à la maturité continue

Point de suivi — Equipe DevExperience

---

# Où on en est

<div class="grid3">
<div class="card"><h3>✅ Diagnostic</h3><p>9 irritants majeurs, 3 personas, 18 cas d'utilisation identifiés sur le terrain</p></div>
<div class="card"><h3>✅ Offre & organisation</h3><p>Option C validée, démarrage porté par IDDA dès septembre 2026</p></div>
<div class="card"><h3>✅ POC</h3><p>Backstage et Crossplane expérimentés et retenus</p></div>
</div>

<p class="lead">Reste à valider aujourd'hui : <strong>dans quel ordre on livre</strong></p>

---

# Ce que cette feuille de route ne fait pas

<div class="keypoint">
Elle ne revient pas sur le <strong>cadrage organisationnel</strong> (ADR-003, déjà validé) : équipe, positionnement vis-à-vis des capability teams, démarrage IDDA. Elle ne porte que sur le <strong>phasage</strong> — quoi livrer, dans quel ordre, avec quels critères de sortie.
</div>

**Principe directeur** : approche **itérative**, pas Big Bang. Chaque phase livre de la valeur mesurable avant d'attaquer la suivante.

---

<!-- _class: section -->

# Vue d'ensemble

Cinq phases, du quick win à l'amélioration continue

---

![](./assets/roadmap.png)


---

# Les phases en un coup d'œil

<div class="grid5">
<div class="card"><h3>0</h3><p class="promise">Fondations</p><p class="detail">Équipe, backlog, état des lieux</p></div>
<div class="card win"><h3>1</h3><p class="promise">Portail & doc</p><p class="detail">Quick win, tous les devs</p></div>
<div class="card"><h3>2</h3><p class="promise">Golden Path Kube</p><p class="detail">MVP de bout en bout</p></div>
<div class="card"><h3>3</h3><p class="promise">Self-service</p><p class="detail">Industrialisation</p></div>
<div class="card"><h3>4</h3><p class="promise">Maturité</p><p class="detail">Amélioration continue</p></div>
</div>

---

<!-- _class: section -->

# Phase 0 — Fondations

Mois 1-2 (sept.–oct. 2026)

---

# Phase 0 — Objectif

<p class="lead">Poser les bases organisationnelles et techniques avant de livrer de la valeur</p>

<div class="grid2">
<div class="card">
<h3>Organisationnel</h3>
<p>Une équipe DevExperience montée en compétence, un backlog défini, des équipes pilotes engagées et un canal de retour utilisateur en place</p>
</div>
<div class="card">
<h3>Technique</h3>
<p>Une vision claire de la documentation existante à intégrer, un premier Backstage accessible pour commencer à construire dessus</p>
</div>
</div>

---

# Phase 0 — Découpage en US techniques

| Priorité    | User story                                                                              |
| ----------- | --------------------------------------------------------------------------------------- |
| **Forte**   | Installer Backstage (vanilla) en environnement de dev                                   |
| **Forte**   | Cartographier la documentation existante nécessaire aux développeurs, équipe par équipe |
| **Forte**   | Définir le backlog initial de l'équipe DevExperience                                    |
| **Moyenne** | Identifier et engager 2-3 équipes pilotes volontaires                                   |
| **Moyenne** | Mettre en place un forum utilisateur (retours développeurs)                             |
| **Moyenne** | Identifier les besoins de formations / accompagnement                                   |

---

# Phase 0 — Critères de sortie

- Équipe constituée et opérationnelle
- Backstage accessible en environnement de dev
- Équipes pilotes identifiées et engagées
- Cartographie de la documentation existante réalisée
- Le contact avec les prestataires a été réalisé

---

<!-- _class: section -->

# Phase 1 — Portail, doc & découvrabilité

Mois 2-5 : Quick win — tous les devs, tous les SNDI

---

# Phase 1 — Objectif

<p class="lead">Résoudre l'irritant n°1 du constat terrain : documentation dispersée et syndrome « Martine »</p>

- **Trouver le bon service et son propriétaire en un clic** : catalogue centralisé de tous les composants
- **Ne plus chercher la doc au bon endroit** : documentation des capability teams centralisée et à jour
- **Savoir qui contacter, sans deviner** : annuaire des équipes et interlocuteurs
- **Voir ce qui a changé ou va changer** : feed des changements et incidents
- **Trouver l'info en cherchant, pas en naviguant** : moteur de recherche intégré

**BONUS** : un parcours d'onboarding pour prendre en main l'outil

---

# Phase 1 — Découpage en US techniques

| Priorité    | User story                                                                |
| ----------- | ------------------------------------------------------------------------- |
| **Forte**   | Déployer Backstage en production                                          |
| **Forte**   | Déployer le Software Catalog Backstage (composants, owners, dépendances)  |
| **Forte**   | Migrer la documentation des capability teams vers TechDocs (docs-as-code) |
| **Forte**   | Développer l'annuaire des équipes et interlocuteurs                       |
| **Forte**   | Documenter l'utilisation pour les différents utilisateurs                 |
| **Moyenne** | Documenter les choix d'architecture et d'implémentation (Homologation)    |
| **Moyenne** | Mettre en place le feed des changements et incidents                      |

---

| Priorité    | User story                                                                                    |
| ----------- | --------------------------------------------------------------------------------------------- |
| **Moyenne** | Identifier un moteur de recherche pour le portail (solution interne backstage / externe / IA) |
| **Moyenne** | Déployer le moteur de recherche pour le portail                                               |
| **Moyenne** | Collaborer avec l'urbanisation afin d'identifier le rôle de backstage par rapport à Oscar     |
| **Moyenne** | Initier l'intégration des briques des développeurs dans le catalogue     |
| **Bonus**   | Construire le parcours d'onboarding                                                           |

---

# Phase 1 — Critères de sortie

- Portail accessible à tous les devs, tous SNDI
- Documentation d'au moins **80%** des capability teams intégrée dans TechDocs
- Au moins **50%** des services/outils (de la prod) référencés dans le catalogue
- Trafic portail en croissance mois sur mois
- Réduction mesurable des questions « à qui je m'adresse ? » sur Tchap
- Demo de la solution en DevOpsAcc + des démos d'avancements régulières
- Un dossier d'archi est initialisé et complété
- Les équipes pilotes ont intégré une grande part de leur service dans le catalogue


---

<!-- _class: section -->

# Phase 2 — Mettre à disposition un premier GoldenPath pour l'appli springboot sur Kubernetes

Mois 4-7 · Chevauche la fin de la Phase 1

---

# Phase 2 — Objectif

<p class="lead">Livrer un premier parcours standardisé de bout en bout pour les applications Spring Boot sur Kubernetes</p>

- **Créer un service Spring Boot en quelques clics** : repo, pipeline et déploiement générés automatiquement, sans partir d'une page blanche
- **Obtenir son infrastructure sans ticket** : client Keycloak, policy Vault, bucket... disponibles en self-service, brique par brique
- **Trouver et comprendre le Golden Path sans aide extérieure** : parcours et documentation découvrables directement depuis le portail

---

# Phase 2 — Découpage en US techniques

## Créer un service en quelques clics

| Priorité    | User story                                                                       |
| ----------- | -------------------------------------------------------------------------------- |
| **Forte**   | Scaffolder un service Spring Boot (repo + pipeline CI/CD) depuis Backstage       |
| **Forte**   | Déployer automatiquement le service généré sur l'environnement Kube (GitOps)     |
| **Forte**   | Demander un client Keycloak via une Claim Crossplane                             |
| **Forte**   | Demander une policy Vault via une Claim Crossplane                               |
| **Forte**   | Demander un bucket via une Claim Crossplane                                      |
| **Moyenne** | Documenter le Golden Path dans TechDocs, référencé dans le catalogue             |
| **Moyenne** | Standardiser le pipeline avec des Components CI (To Be Continuous)               |
| **Moyenne** | Documenter comment intégrer le GoldenPath si j'ai déjà une application existante |

---
## Obtenir son infrastructure sans ticket



---

# Phase 2 — Critères de sortie

- Au moins **3 projets créés** via le Golden Path par les équipes pilotes
- Feedback collecté et intégré dans le backlog
- Temps de création d'un nouveau projet **< 15 minutes** (vs jours actuellement)

---

<!-- _class: section -->

# Phase 3 — Self-service, observabilité & industrialisation

Mois 6-10

---

# Phase 3 — Objectif

<p class="lead">Étendre le self-service, intégrer l'observabilité, généraliser au-delà des équipes pilotes</p>

<div class="grid2">
<div class="card"><h3>Self-service</h3><p>Provisionner un environnement sans ticket, être protégé par défaut, ne plus être seul face à un incident</p></div>
<div class="card"><h3>Observabilité</h3><p>Voir la santé de son service en un coup d'œil, être alerté seulement quand c'est pertinent</p></div>
</div>

- **Proposer d'autres GoldenPaths** : Capitaliser sur les outils mis en place pour le premier golden path pour en proposer d'autres (React / Python)
- **Profiter des évolutions du Golden Path sans tout refaire** : mise à jour des templates propagée automatiquement
- **Consommer les capability teams sans changer d'outil** : intégration étendue (PDD, IAHS, Observabilité)
- **Contribuer, pas seulement consommer** : catalogue ouvert aux équipes avancées

---

# Phase 3 — Découpage en US techniques

| Priorité    | User story                                                                                                     |
| ----------- | -------------------------------------------------------------------------------------------------------------- |
| **Forte**   | Provisionner un environnement via UI (ou as code), sans ticket                                                 |
| **Forte**   | Etudier les mécanismes de sécurité à intégrer dans le pipeline                                                 |
| **Forte**   | Construire le dashboard de santé des services (plugins ArgoCD et Elastic, intégration aux outils analyzer ...) |
| **Moyenne** | Générer des alertes pertinentes et filtrées                                                                    |
| **Moyenne** | Intégrer des runbooks et une aide au diagnostic dans le portail                                                |
| **Moyenne** | Propager les mises à jour de template aux projets existants (`copier update`)                                  |
| **Moyenne** | Étendre l'intégration aux capability teams PDD, IAHS, Observabilité                                            |
| **Faible**  | Ouvrir la contribution au catalogue de templates                                                               |

---

# Phase 3 — Critères de sortie

- Adoption mesurable **au-delà** des équipes pilotes
- Réduction mesurable du nombre de tickets d'infrastructure
- Satisfaction développeur en hausse (enquête DevExp)

---

<!-- _class: section -->

# Phase 4 — Maturité & évolution continue

Mois 10+ · Sans fin définie

---

# Phase 4 — Axes d'évolution

- **Extension au monde Cloud et VM** (selon résultats du questionnaire cloud prévu juin 2026)
- **Automatisation avancée** : Assembler l'ensemble des claims as a service en une macro claim (Par Exemple SpringBootApp)
- **Intégration IA** : aide au diagnostic, suggestion de résolution
- **Métriques DORA** : fréquence de déploiement, lead time, MTTR, taux d'échec
- **Contribution communautaire active** (inner source)

<div class="keypoint">
La plateforme est un <strong>produit</strong>, pas un projet : cette phase n'a pas vocation à se terminer.
</div>

---

<!-- _class: section -->

# Piloter la trajectoire

---

# Comment on mesure qu'on avance

<div class="grid3">
<div class="card"><h3>📈 Adoption</h3><p>Visites portail, services catalogués, projets créés via Golden Path</p></div>
<div class="card"><h3>🎯 Impact</h3><p>Temps de création de projet, temps d'onboarding, tickets d'infra, questions « à qui m'adresser »</p></div>
<div class="card"><h3>😊 Satisfaction</h3><p>Score DevExp, feedback qualitatif des pilotes, NPS interne</p></div>
</div>

<div class="keypoint">
Le détail des indicateurs et de la gouvernance produit est posé dans l'ADR-012.
</div>

---

<!-- _class: section -->

# Merci à vous !

Des questions ?
