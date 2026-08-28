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
---

<!-- _class: title -->

# Vers une plateforme unifiée pour nos développeurs

## Quel périmètre ? Comment insérer l'équipe ? Quelle composition ?

---

# Vocabulaire : Les capabilities Team

<img src="./assets/equipe_prod.png" width="350">

<div class="keypoint">
Une capability team fournit du service sur son domaine de responsabilité sur lequel elle dispose d'un haut niveau d'expertise.
</div>

---

# Vocabulaire : Développeur

<div class="keypoint">
<strong>Le développeur</strong> conçoit, développe et maintient les applications du SI de l'Insee.<br/> Un développeur ne se réduit pas à faire parti d'un SNDI, un ops qui développe une application est considéré comme un développeur.
C'est <strong>l'utilisateur (un des consommateurs) principal de la plateforme</strong> : il consomme les services exposés en self-service pour livrer de la valeur métier, sans avoir à maîtriser toute la complexité sous-jacente (les trois mondes d'exécution, les outils, les workflows).
</div>

</br>

<div class="keypoint">
À distinguer de la <strong>capability team</strong>, qui <em>produit</em> l'expertise infra ou de production ; le développeur, lui, la <em>consomme</em>.
</div>

---

# Le contexte en chiffres

<div class="grid3">
<div class="card">
<h3>250</h3>
<p>développeurs au sein du SI Insee (hors équipes de production, également concernées)</p>
</div>
<div class="card">
<h3>2 (bientôt 3)</h3>
<p>mondes d'exécution : VM, Kubernetes, (Cloud)</p>
</div>
<div class="card">
<h3>12</h3>
<p>équipes services de la production</p>
</div>
<div class="card">
<h3>6 ans</h3>
<p>d'adoption DevOps à uniformiser, standardiser, simplifier</p>
</div>
<div class="card">
<h3>10</h3>
<p>Nombre de tickets (déclarés) minimun à créer pour une nouvelle plateforme</p>
</div>
<div class="card">
<h3>12</h3>
<p>Moyenne du nombre de jours (déclarés) pour qu'une équipe mettent en place une nouvelle appli (code => déploiement) </p>
</div>
</div>

<p class="lead">Une démarche Platform Engineering pour <strong>homogénéiser sans recentraliser</strong></p>

---

# Des irritants à résoudre

<div class="grid3">
<div class="card">
<h3>🔀 Hétérogénéité</h3>
<p>Des connaissances hétérogènes entre individus / équipes / SNDI. Chaque équipe résout à sa manière les mêmes problèmes</p>
</div>
<div class="card">
<h3>🌍 Trois mondes, des dizaines d'outils, plusieurs workflows</h3>
<p>Complexité portée par chaque équipe</p>
</div>
<div class="card">
<h3>🔍 Découvrabilité</h3>
<p>Information dispersée, dépendance aux personnes</p>
</div>
</div>
<div class="keypoint">
<strong>Conséquence :</strong> effort dupliqué · charge cognitive · variance des pratiques · onboarding lent
</div>

---

# Ce qu'on veut obtenir

Une logique simple, voulue par les devs (empruntée aux standards du _Platform Engineering_) :

| Aujourd'hui                      | Demain                                       |
| -------------------------------- | -------------------------------------------- |
| Le dev parle à **N équipes**     | Le dev parle à **1 seule équipe**            |
| Tickets et coordination manuelle | **Self-service** via une plateforme          |
| « À chacun son périmètre »       | **Une offre cohérente**, une roadmap commune |

L'objectif : **rendre les développeurs autonomes** et réduire leur charge.

<div class="keypoint">
<strong>Remarque :</strong> le but n'est pas d'interdire le dialogue entre les développeurs et les POs des équipes de services, mais de proposer un point d'entrée unique pour l'expérience developpeurs aux utilisateurs de la plateforme.
</div>

---
<!-- _class: section -->

# 1. Le périmètre

---

# Domaine fonctionnel du service DevExpérience

<img src="./assets/architecture-fonctionnelle.drawio.png" width="600" />

Ce que le service **doit faire** — indépendamment de qui la porte

---

# Sept blocs fonctionnels

<div class="grid2">
<div class="card"><h3 class="scope-in">✅ Expérience développeur</h3><p>Portail, catalogue, support</p></div>
<div class="card"><h3 class="scope-in">✅ Self-Service</h3><p>Templates, Claims</p></div>
<div class="card"><h3 class="scope-in">✅ Fabrique logicielle</h3><p>CI, qualité, sécurité</p></div>
<div class="card"><h3 class="scope-in">✅ Orchestration self-service</h3><p>Routage, provisioning, cycle de vie</p></div>
<div class="card"><h3 class="scope-out">❌ Briques transverses</h3><p>Helm · Terraform · Ansible</p></div>
<div class="card"><h3 class="scope-out">❌ Capacités transverses</h3><p>IAHS · PDD · Observabilité…</p></div>
</div>
<div class="keypoint">
<span class="scope-in">✅ Dans le périmètre plateforme</span> &nbsp;·&nbsp; <span class="scope-out">❌ Hors périmètre, porté ailleurs</span>
</div>

---

# Expérience développeur

<p class="lead">Le visage de la plateforme — tout ce que le développeur voit</p>

- 🎯 **Portail développeur** — découverte, scaffolding, documentation
- 📚 **Catalogue de services** — IHM, API, CLI, librairies
- 📢 **Information sur les changements** — communication produit
- 👥 **Annuaire des équipes** — qui possède quoi
- 📊 **Suivi des opérations** — restitution des actions
- 🆘 **Support unique** — un canal de contact identifié (cela n'empêche pas les devs de parler aux autres équipes)

<div class="keypoint">
Aucune autre équipe ne porte cette fonction dans le SI aujourd'hui.
</div>

---

# Self-Service

<p class="lead">Transformer une intention en action industrialisée</p>

- 👨🏻‍💻 **Golden path applicatif** — Dépôt de code pour les devs embarquant directement du code applicatif pur Insee, du cicd, les bonnes pratiques...
- 🧱 **Briques de construction réutilisables** — templates CI/CD, dashboard préconstruit, Exemple de dockerfile...
- 📋 **Catalogue des outils en self-service** — l'offre exposée au dev
- 📜 **Claim / Contrat d'intention** — Contrat permettant de déclarer _ce que je veux_, pas _comment le produire_

<div class="keypoint">
<strong>Cible : une offre agnostique</strong> — la migration cloud future devient un changement d'implémentation, pas une réécriture côté équipes.<br/>
Agnostique <strong>ne veut pas dire neutre</strong> : le monde <strong>conteneurisé (Kubernetes/Cloud) reste privilégié</strong>, la cible par défaut.
</div>

---

# Fabrique logicielle

<p class="lead">Du code à l'artefact prêt à déployer, avec contrôles intégrés</p>

- 🏭 **Stockage du code applicatif / déploiement** — Forge logicielle
- 🔨 **Construction des artefacts** — pipelines CI mutualisés
- 🔐 **Qualité, signature, sécurité** — SAST, scan dépendances, scan images
- 📦 **Stockage des artefacts signés** — registre central

<div class="keypoint">
Intègre les <strong>gates qualité et sécurité transverses</strong> que tout artefact franchit avant la production.
</div>

---

# Orchestration self-service

<p class="lead">Exécuter une Claim — router, provisionner, accompagner</p>

- 🎯 **Routage selon la cible** — K8S, VM, Cloud
- ⚙️ **Provisionnement des ressources** — GitOps déclaratif
- 🔧 **Configuration Day-2** — agents, durcissement
- 🔄 **Gestion du cycle de vie** — création, évolution, suppression

<div class="keypoint">
<strong>Transverse aux trois mondes</strong> — aucune autre équipe ne couvre ce périmètre. Le <strong>conteneurisé (K8S/Cloud) est la cibles privilégiée</strong>,le monde VM restant pleinement supportés.
</div>

---

# Ce qui reste hors périmètre

| Bloc                                                      | Pourquoi hors plateforme                                              | Propriétaire                        |
| --------------------------------------------------------- | --------------------------------------------------------------------- | ----------------------------------- |
| 🧱 Briques transverses (Helm, TF, Ansible, Dépot de code) | Encodent l'expertise domaine                                          | Capability teams + Animation du dev |
| 🛡️ Capacités transverses (IAHS, PDD, Observabilité…)      | L'équipe s'appuie sur les briques proposées mais ne les maintient pas | Capability teams                    |
| 📦 Substrats d'exécution (K8s, VM, Cloud)                 | Opérés par l'infra                                                    | Équipes infrastructure              |

<div class="keypoint">
La plateforme est <strong>canal de distribution</strong> de l'expertise — pas son <strong>remplaçant</strong>.
</div>

---

# Technologie manipulée par l'équipe DevExperience

<img src="./assets/architecture.drawio.png" />

---

# Pourquoi ce découpage importe

<div class="grid3">
<div class="card">
<h3>📐 Dimensionnement</h3>
<p>Équipe à taille humaine — pas d'experts à recruter dans tous les domaines</p>
</div>
<div class="card">
<h3>🤝 Alignement</h3>
<p>Les capability teams gagnent un canal — pas une concurrente</p>
</div>
<div class="card">
<h3>📍 Clarté</h3>
<p>Le développeur sait à qui s'adresser pour quoi</p>
</div>
</div>
<div class="keypoint">
Sans ce découpage : goulot d'étranglement ou coquille vide.
</div>

---

<!-- _class: section -->

# 2. trois options d'insertion

Comment la Platform Experience se positionne-t-elle vis-à-vis des capability teams ?

---

# Trois positionnements

> Solution reposant sur une nouvelle équipe produit 100% autonome : une équipe DevExperience dédiée

<br/>

<div class="grid3">
<div class="card">
<h3>A — Equipe Plateforme indépendante (autonome)</h3>
<p>L'équipe DevExpérience <b>produit elle-même</b> la majorité des briques. Elle <b>réimplémente</b> tout pour ses utilisateurs</p>
</div>
<div class="card">
<h3>B — Equipe Plateforme produit + équipes capabilities (Consommatrice)</h3>
<p>Les capability teams <b>exposent en autonomie</b> — L'équipe DevExpérience n'opère que le portail</p>
</div>
<div class="card">
<h3>C — Equipe Plateforme produit (Intégratrice) + équipes capabilities</h3>
<p>L'équipe DevExpérience <b>assemble et distribue</b> ce que produisent les capability teams</p>
</div>
</div>

---

# Option A — Plateforme indépendante (autonome)

<p class="lead"> L'équipe DevExpérience internalise les expertises de domaine</p>
<div class="grid2">
<div class="pros">
<h3>✅ Avantages</h3>
<ul>
<li>Time-to-market rapide (et encore pas sûr)</li>
<li>Cohérence forte (un propriétaire)</li>
<li>Décisions techniques rapides</li>
<li>Interlocuteur unique</li>
</ul>
</div>
<div class="cons">
<h3>⚠️ Inconvénients</h3>
<ul>
<li>Risque de silo plateforme : <strong>un SI dans le SI</strong> — coût et maintenance en hausse</li>
<li>Effectif intenable à terme</li>
<li>Dette d'expertise inévitable</li>
<li>Concurrence avec capability teams</li>
</ul>
</div>
</div>

---

# Option B — Plateforme produit + équipes capabilities (Consommatrice)

<p class="lead">L'équipe DevExpérience fournit le portail — les équipes capabilities intègrent en autonomie leur service dans le portail</p>
<div class="grid2">
<div class="pros">
<h3>✅ Avantages</h3>
<ul>
<li>Effectif PFE minimal</li>
<li>Autonomie capability teams maximale</li>
<li>Pas de goulot plateforme</li>
<li>Modèle "marketplace interne"</li>
</ul>
</div>
<div class="cons">
<h3>⚠️ Inconvénients</h3>
<ul>
<li>Cohérence d'expérience fragile</li>
<li>Industrialisation dispersée</li>
<li>PFE sans levier sur les standards</li>
<li>Maturité élevée requise chez chaque équipe capabilities</li>
<li>Pas de vision globale</li>
</ul>
</div>
</div>

<div class="keypoint">
C'est le modèle à la rundeck DevOps, mais avec une jolie interface.
</div>

---

![](./assets/consommatrice.drawio.png)

---

# Option C — Plateforme produit (Intégratrice) + équipes capabilities

<p class="lead">L'équipe DevExpérience <strong>assemble et distribue ce</strong> que produisent les capability teams. Elle devient le <strong>principal client</strong> des capability teams et bénéficie d'un <strong>fort sponsoring</strong> de la DSI</p>
<div class="grid2">
<div class="pros">
<h3>✅ Avantages</h3>
<ul>
<li>Effectif soutenable</li>
<li>Expertises capability teams valorisées</li>
<li>Cohérence sans concurrence</li>
<li>Évolutivité naturelle</li>
<li>Cohérence de l'offre hors plateforme</li>
<li>Amélioration de l'offre des capability teams</li>
</ul>
</div>
<div class="cons">
<h3>⚠️ Inconvénients</h3>
<ul>
<li>Coordination inter-équipes</li>
<li>Démarrage plus lent</li>
<li>Maturité minimale requise</li>
<li>Responsabilité distribuée</li>
<li>Les bonnes pratiques poussées par l'équipe DevExperience peuvent ne pas être intégrées dans les équipes capabilities</li>
<li>Nécessite fort sponsoring de la DSI</li>
</ul>
</div>
</div>

---

![](./assets/collaboratrice.drawio.png)

---

# Comparaison synthétique

| Critère                       | A — Autonome | B — Consommatrice | C — Intégratrice |
| ----------------------------- | ------------ | ----------------- | ---------------- |
| Effectif PFE                  | 🔴 Élevé     | 🟢 Faible         | 🟡 Modéré        |
| Time-to-market initial        | 🟢 Rapide    | 🟡 Modéré         | 🟡 Modéré        |
| Pérennité 3-5 ans             | 🔴 Faible    | 🟢 Élevée         | 🟡 Modérée       |
| Cohérence d'expérience        | 🟢 Forte     | 🔴 Variable       | 🟢 Forte         |
| Valorisation capability teams | 🔴 Faible    | 🟢 Élevée         | 🟢 Élevée        |

---

| Critère                                 | A — Autonome | B — Consommatrice | C — Intégratrice               |
| --------------------------------------- | ------------ | ----------------- | ------------------------------ |
| Risque politique                        | 🔴 Élevé     | 🟡 Modéré         | 🟡 Modéré                      |
| Maturité requise du SI                  | 🟢 Faible    | 🔴 Élevée         | 🟡 Modérée                     |
| Cohérence hors plateforme               | ⚫ N/A       | 🔴 Faible         | 🟢 Élevée (si fort sponsoring) |
| Montée en maturité des capability teams | 🔴 Aucune    | 🟡 Indirecte      | 🟢 Forte (si fort sponsoring)  |

---

# Couverture fonctionnelle par option

<div class="grid3">
<div class="card">
<h3>A — Autonome</h3>
<p class="promise">Tout, mais rien de fiable</p>
<p class="detail">4 domaines réimplémentés · doublons fragiles</p>
</div>
<div class="card">
<h3>B — Consommatrice</h3>
<p class="promise">Ce que les équipes veulent bien exposer</p>
<p class="detail">Couverture partielle · conditionnelle à leur maturité</p>
</div>
<div class="card">
<h3>C — Intégratrice</h3>
<p class="promise">Une offre cohérente, assemblée</p>
<p class="detail">4 capacités intégrées · soutenable</p>
</div>
</div>

<div class="keypoint">
La couverture <strong>disqualifie A, B</strong> — reste <strong>C</strong>.<br/>
Le vrai choix : <strong>quelle promesse l'Insee peut tenir</strong> vis-à-vis de ses 250 développeurs — et, au-delà, de ses équipes de production.
</div>

---

# Trois questions pour arbitrer

<div class="grid3">
<div class="card">
<h3>1. Maturité capability teams ?</h3>
<p>Moyen/Faible → A, C<br/>Élevée → B</p>
</div>
<div class="card">
<h3>2. Effectif PFE à 2 ans ?</h3>
<p>&lt; 5 → B<br/>5-10 → C<br/>&gt; 10 → A possible</p>
</div>
<div class="card">
<h3>3. Culture de coopération ?</h3>
<p>Faible → A <br/>Forte → B, C</p>
</div>
</div>

<div class="keypoint">
Les fourchettes d'effectif sont des <strong>ordres de grandeur indicatifs</strong>, à confirmer selon le périmètre réellement staffé.
</div>

---

# Recommandation

L'**Option C** comme cible de référence moyen long terme

---

# Pourquoi l'option C

<div class="grid3">
<div class="card">
<h3>🏗️ Continuité culturelle</h3>
<p>Prolonge 6 ans de DevOps : industrialiser, pas tout recentraliser</p>
</div>
<div class="card">
<h3>♻️ Soutenable</h3>
<p>Effectif à taille humaine, expertises Insee valorisées</p>
</div>
<div class="card">
<h3>📖 Éprouvé</h3>
<p>Team Topologies + référence CNCF + ce qui est fait ailleurs</p>
</div>
</div>

---

# Décision (post-réunion)

L'option C est validée ✅

---

<!-- _class: section -->

# Insertion dans notre organisation

---

## Responsabilités Développeurs

- Développement du portail (Backstage), des templates, de la CLI
- UX développeur et intégration front
- Maintien du catalogue de composants et de la documentation TechDocs

---

## Responsabilités Ops

- Intégration avec les outils existants (Kubernetes, ArgoCD, Vault, GitLab CI, Nexus)
- MCO/MCS des briques constituant l'offre
- Automatisation des workflows d'infrastructure
- Liaison technique avec les capability teams

---

## Responsabilités DevOps

- Conception et maintenance des Golden Paths
- Pipelines CI/CD standardisés
- GitOps et déploiement continu
- Pont entre les besoins dev et les contraintes ops

---

# Composition théorique

La littérature conseille généralement **une équipe** de **6 personnes** avec trois profils complémentaires :

- 2 Développeurs (Développement du portail, apport de la vision dev)
- 2 Opérationnels (MCO/MCS des briques appartenant à la plateforme)
- 2 DevOps (Automatisation, orchestration des différents éléments)

---

# Quelle intégration dans la roue de la prod ?

<p class="lead">La cible reste une équipe / un service dédié (option A)</p>

- 🎯 **1 nouveau service** avec sa **roadmap** et son **PO** dédiés, et des **ressources** propres pour réaliser le service

<div class="keypoint">
<strong>Mais difficile à mettre en place dès septembre 2026 :</strong>
<ul>
<li>l'identification du PO, la construction de la roadmap et l'identification des ressources <strong>prennent du temps</strong></li>
<li>en septembre, on ajoute d'abord la roadmap <strong>KubeApp</strong> dans la roadmap IDDA</li>
</ul>
</div>

---

# En septembre 2026

<p class="lead">Un démarrage pragmatique, porté par IDDA</p>

- 🆕 **Création d'un nouveau service** dans la roue de la prod
- 🗺️ **Création d'une roadmap DevExpérience** par le CPO et les deux POs d'IDDA
- 🤝 **Travail collaboratif des deux POs** pour organiser les priorités de l'équipe IDDA
- ⚙️ **Réalisation des priorités** au sein de l'équipe IDDA

<div class="keypoint">
L'organisation des équipes <strong>sur le long terme</strong> sera instruite dans un second temps, par la <strong>hiérarchie</strong>, en collaboration avec les agents.
</div>

---

# Décision (post-réunion)

<p class="lead">Cible : un service DevExpérience dédié — démarrage porté par IDDA dès septembre 2026</p>

- ✅ **Cible** : un nouveau service dédié, avec PO et roadmap propres
- ⏳ **Démarrage sept. 2026** : porté par IDDA et les 2 POs, le temps de construire la roadmap de monter en compétences et de staffer l'équipe
- 🧭 **Organisation cible** instruite dans un second temps par la hiérarchie, en collaboration avec les agents

<div class="keypoint">
Il est demandé à IDDA et aux POs de bien mettre en avant <strong>dans les communications</strong> aux utilisateurs que le périmètre / backlog du produit DevExpérience est <strong>bien distinct</strong> de celui d'IDDA.
</div>

---

<!-- _class: section -->

# Merci à vous !

Des questions ?

---

# Trois périmètres, trois natures
 
<p class="lead">La confusion vient d'une comparaison de choses <strong>qui ne sont pas de même nature</strong></p>

| Objet | Nature | Question | En une phrase |
| --- | --- | --- | --- |
| **IDDA** | une **équipe** (org) | **QUI ?** | Une équipe existante qui héberge temporairement les ressources DevExpérience — tout en gardant son propre produit (service IDDA) / backlog |
| **Service DevExpérience** | un **produit** (responsabilité) | **QUOI ?** | La couche expérience + intégration : portail, self-service, fabrique, orchestration. Le *canal*. N'inclut **pas** l'expertise de domaine |
| **Plateforme** | une **offre** (vue du dev) | **RÉSULTAT ?** | Tout ce que le développeur consomme : la couche DevExpérience **+** toutes les capabilities distribuées |
 
<div class="keypoint">
IDDA = une <strong>équipe</strong> · DevExpérience = un <strong>produit</strong> · Plateforme = ce que le dev <strong>obtient au bout</strong>.
</div>

---
 
# Comment ils s'emboîtent

![](assets/perimetre.drawio.png)

---
 
# Les deux pièges à éviter
 
<div class="grid2">
<div class="trap">
<h3>⚠️ Piège 1 — IDDA ≠ DevExpérience</h3>
<p>Mêmes personnes en septembre 2026, mais <strong>deux backlogs distincts</strong>. Appartenir à IDDA (l'équipe) ne dit rien du périmètre du produit qu'on porte.</p>
</div>
<div class="trap">
<h3>⚠️ Piège 2 — DevExpérience ≠ Plateforme</h3>
<p>DevExpérience <strong>assemble et distribue</strong> ; la plateforme est plus large : elle inclut tout ce que les capability teams exposent à travers elle. On <strong>distribue</strong> l'expertise, on ne la <strong>possède</strong> pas.</p>
</div>
</div>
<div class="keypoint">
🛒 <strong>L'image :</strong> la plateforme, c'est le magasin tel que le client le vit ; DevExpérience range les rayons et tient la caisse ; les capability teams fabriquent les produits ; IDDA est un fournisseur qui prête aussi son personnel au démarrage.
</div>

---
 
# Le réflexe qui tranche
 
<p class="lead">Face à « périmètre X », se demander de quelle <strong>nature</strong> on parle</p>
<div class="grid3">
<div class="card">
<h3>« Qui fait ? »</h3>
<p>→ <strong>IDDA</strong> (l'équipe)</p>
</div>
<div class="card">
<h3>« Quel produit / backlog ? »</h3>
<p>→ <strong>DevExpérience</strong> (le produit)</p>
</div>
<div class="card">
<h3>« Qu'obtient le dev ? »</h3>
<p>→ <strong>la Plateforme</strong> (l'offre)</p>
</div>
</div>
<div class="keypoint">
Les deux phrases à marteler : « <strong>Être membre d'IDDA ≠ travailler sur le périmètre DevExpérience</strong> » &nbsp;·&nbsp; « <strong>DevExpérience distribue les capabilities, elle ne les possède pas</strong> ».
</div>
