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

# Crossplane

## Le control plane universel pour industrialiser l'infrastructure

Une opportunité pour notre plateforme interne (Platform Engineering)

---

<!-- _class: section -->

# Le constat

<p>Pourquoi le Platform Engineering, et pourquoi un portail ne suffit pas</p>

---

# Pourquoi on fait du Platform Engineering ?

<div class="grid4">
<div class="card">
<h3>🔀 Livraisons lentes</h3>
<p>Des délais dûs aux tickets et aux allers-retours manuels</p>
</div>
<div class="card">
<h3>🧩 Hétérogénéité</h3>
<p><b>Ops</b> : outils et scripts fragmentés propres à chaque équipe.</p>
<p><b>Devs</b> : complexité d'apprentissage</p>
</div>
<div class="card">
<h3>🌍 Trois mondes, des dizaines d'outils</h3>
<p>Plusieurs workflows, complexité portée par chaque équipe</p>
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

# Un portail développeur ne suffit pas

La première réponse envisagée est un **portail** (Backstage chez nous). Utile, mais partiel :

<div class="grid2">
<div class="card">
<h3>✅ Ce qu'il apporte — day 0</h3>
<p>Il <b>expose</b> un catalogue et <b>génère</b> des dépôts.</p>
</div>
<div class="card">
<h3>⛔ Ce qui manque — day 2</h3>
<p>Il <b>ne gère pas</b> le cycle de vie : évolutions, mises à jour, conformité dans la durée.</p>
</div>
</div>

<div class="keypoint">
C'est une <strong>vitrine</strong> ; il manque le <strong>moteur</strong> qui provisionne et gouverne réellement. → Il faut un <strong>moteur d'orchestration</strong> sous le portail (un <em>control plane</em>).
</div>

---

# Un moteur d'orchestration, à quoi ça sert ?

<p class="lead">Il ne se contente pas d'exécuter une action une fois : il maintient un système dans l'état voulu, en continu.</p>

<div class="grid3">
<div class="card">
<h3>🎯 État désiré déclaratif</h3>
<p>Côté dev, on décrit le <b>résultat</b> attendu, pas la suite d'étapes pour l'obtenir.</p>
</div>
<div class="card">
<h3>🔄 Boucle de réconciliation</h3>
<p>En arrière-plan, il compare en permanence l'état réel à l'état voulu et agit pour combler l'écart.</p>
</div>
<div class="card">
<h3>🔧 Auto-réparation</h3>
<p>En cas de panne ou de modification hors cadre, il corrige de lui-même.</p>
</div>
</div>

<div class="keypoint">
→ L'implémentation la plus courante dans les démarches de platform engineering est l'outil <strong>Crossplane</strong>.
</div>

---

# Articulation avec Backstage

<p class="lead">Backstage et Crossplane ne se concurrencent pas : deux couches complémentaires.</p>

<div class="grid2">
<div class="card">
<h3>🖥️ Backstage = la vitrine</h3>
<p>Portail développeur : catalogue de services, documentation, responsabilités, formulaires self-service (<em>Software Templates</em>). Aucun moteur pour provisionner réellement — il pousse des fichiers dans des dépôts.</p>
</div>
<div class="card">
<h3>⚙️ Crossplane = le moteur</h3>
<p>Control plane : reçoit la demande, provisionne, maintient conforme. Pas de portail (UI) par lui-même.</p>
</div>
</div>

---

# Backstage : générer n'est pas gérer

<div class="grid2">
<div class="pros">
<h3>Day 0 — l'amorçage</h3>
<ul>
<li>Les <em>Software Templates</em> <b>génèrent un dépôt</b> à partir d'un modèle (fichiers, structure, création du repo).</li>
<li>Excellent pour démarrer vite et de façon standardisée.</li>
</ul>
</div>
<div class="cons">
<h3>Day 2 — le cycle de vie</h3>
<ul>
<li>Une action <b>ponctuelle</b> : une fois le dépôt créé, le lien avec le template est rompu.</li>
<li>Il suit des <b>métadonnées</b>, mais ne pilote pas l'<b>état réel</b> des ressources.</li>
<li>Lors d'une évolution, les dépôts déjà générés <b>ne bougent pas</b> : migration à la main, dépôt par dépôt.</li>
</ul>
</div>
</div>

---

# Orchestrer plutôt qu'exécuter : pourquoi pas Terraform ?

<div class="grid2">
<div class="cons">
<h3>Script / pipeline — impératif & ponctuel</h3>
<ul>
<li>Enchaîne des étapes, puis s'arrête.</li>
<li>Si l'état dérive ensuite, <b>personne ne le sait</b>.</li>
<li>Ex. Terraform / OpenTofu, Ansible, Puppet.</li>
</ul>
</div>
<div class="pros">
<h3>Moteur d'orchestration — déclaratif & permanent</h3>
<ul>
<li>Porte la responsabilité <b>continue</b> de l'état.</li>
<li>On raisonne en <b>résultat voulu</b>, pas en procédures.</li>
<li>Dérive et pannes gérées automatiquement ; on fait évoluer le « voulu » et le système <b>converge</b>.</li>
</ul>
</div>
</div>

<div class="keypoint">
→ C'est le principe qui a fait le succès de <strong>Kubernetes</strong> pour les applications. <strong>Crossplane l'étend à toute l'infrastructure.</strong>
</div>

---

<!-- _class: section -->

# Crossplane

<p>L'outil, son fonctionnement et le contrat d'interface</p>

---

# L'outil Crossplane

<div class="grid2">
<div class="card">
<h3>📖 Un standard ouvert</h3>
<p><b>Open source</b> (licence Apache 2.0), créé par Upbound, à <b>gouvernance neutre</b> — pas de dépendance à un éditeur.</p>
<p><b>Projet CNCF « gradué »</b> (28 octobre 2025) : plus haut niveau de maturité, aux côtés de Kubernetes, Prometheus et Helm. Gage de pérennité et de sécurité.</p>
</div>
<div class="card">
<h3>🧱 Comment il s'installe</h3>
<p>Idéalement, il s'installe dans un cluster Kubernetes <b>dédié</b>, qui joue le rôle de <em>control plane</em> : il <b>pilote</b> l'infrastructure, il <b>n'héberge pas</b> les applications.</p>
<p>De base, Crossplane est une brique vide : il fonctionne avec des <b>Providers</b>.</p>
</div>
</div>

<div class="keypoint">
<strong>Prérequis principal :</strong> disposer d'un cluster Kubernetes → les compétences K8s sont le socle nécessaire.
</div>

---

# Comment ça marche, en simplifié

<p class="lead">Une boucle de réconciliation permanente (héritée de Kubernetes) : on décrit l'état voulu, le système corrige en continu les écarts avec le réel.</p>

<div class="grid3">
<div class="card">
<h3>1 · La brique de base</h3>
<p>Chaque ressource (Bucket / client Keycloak / VM…) a une représentation dans Kubernetes, fournie par un <em>provider</em>.</p>
</div>
<div class="card">
<h3>2 · L'abstraction</h3>
<p>L'équipe DevExperience (ou une équipe service) assemble des briques en un service de plus haut niveau et en définit l'interface (la <em>Composition</em> = la recette qui traduit en ressources concrètes).</p>
</div>
<div class="card">
<h3>3 · La demande</h3>
<p>Le dev réclame le service via cette interface (la <em>Claim</em>) ; Crossplane compose, appelle les API, puis surveille et répare.</p>
</div>
</div>

---

# La notion de contrat d'interface

L'équipe DevExperience (ou les équipes services) n'expose pas une implémentation, mais un **contrat** : une interface stable de ce que le dev peut demander.

- Dans Crossplane, ce contrat est une **API** (appelée XRD) que le dev consomme via une simple demande (YAML poussé dans un dépôt Git).
- Le dev dépend du **contrat**, jamais de ce qu'il y a derrière.
- L'implémentation (la *Composition*) peut changer librement : changer de provider, ajouter du chiffrement, durcir une règle, corriger une faille — **sans casser le contrat**.

<div class="keypoint">
C'est ce découplage <strong>interface / implémentation</strong> qui rend l'évolution possible à grande échelle, sans impact pour le dev.
</div>

---

# L'évolution, gérée en continu

Quand l'équipe DevExperience (ou les équipes services) fait évoluer l'implémentation derrière le contrat :

- **toutes les instances existantes** se réconcilient vers le nouvel état désiré.
- **aucune action** requise de chaque dev, **aucune migration** dépôt par dépôt.
- la nouvelle règle ou le correctif s'applique partout, automatiquement.

<div class="keypoint">
<strong>La différence clé :</strong> Backstage <strong>génère une fois</strong> ; Crossplane <strong>gouverne en continu</strong>, derrière un contrat stable.
</div>

---

# Articulation avec Backstage : le flux

<div class="grid2">
<div class="card">
<h3>Le schéma d'assemblage typique</h3>
<p>1. Le dev remplit un formulaire dans <b>Backstage</b></p>
<p>2. → génération d'une demande Crossplane (un manifeste)</p>
<p>3. → déposée dans <b>Git</b></p>
<p>4. → appliquée par <b>GitOps</b> (Argo CD)</p>
<p>5. → <b>Crossplane</b> provisionne et gouverne</p>
<p>6. → Backstage réaffiche l'état des ressources</p>
</div>
<div class="card">
<h3>En une phrase</h3>
<p><b>Backstage</b> répond au « comment le dev demande et suit sa ressource ».</p>
<p><b>Crossplane</b> répond au « comment elle est réellement livrée et gouvernée ».</p>
</div>
</div>

---

# Exemple avec un bucket

![w:700](assets/archi2.drawio.png)

---

# À l'Insee : chacun sa brique, la plateforme assemble

- Chaque **équipe service** publie **sa** partie comme une brique réutilisable (ex. base de données, client Keycloak, Bucket), et en reste **responsable**.
- La **plateforme assemble** ces briques en services de plus haut niveau (composition de compositions).
- On répartit ainsi la charge : pas besoin de tout concentrer sur une seule équipe.

<div class="keypoint">
<strong>Consommation directe possible :</strong> comme chaque brique est une API, un dev peut la consommer <strong>directement</strong> (Git / kubectl), <strong>sans passer par la plateforme</strong> ni par un intermédiaire. Le portail (Backstage) reste une commodité, pas un péage obligatoire.
</div>

---

<!-- _class: section -->

# Les arguments & les bénéfices

<p>Ce que Crossplane change, concrètement</p>

---

# Les arguments pour Crossplane
## Réduction des tickets

- L'équipe DevExperience (ou une équipe service de la prod) publie **une fois** une brique réutilisable ; les équipes se servent seules.
- Une demande n'est plus un ticket traité à la main, mais une déclaration prise en charge automatiquement.
- Le goulot d'étranglement humain disparaît.

---

# Les arguments pour Crossplane
## Une consommation « as a service »

- L'infrastructure devient un **catalogue de services internes**.
- Le dev « commande » une ressource comme un service managé cloud, mais avec **garde-fous intégrés** (grâce aux outils Kubernetes).

---

# Les arguments pour Crossplane
## La richesse des providers

- Couverture des trois grands clouds, mais aussi Kubernetes, Helm, bases SQL, GitHub, Cloudflare, divers SaaS…
- Les providers officiels sont générés depuis les API cloud et couvrent des **milliers de ressources**.
- On ne pilote pas que « du cloud » : presque tout l'écosystème technique, avec le même modèle.

---

# Les arguments pour Crossplane
## Une interface pensée pour les devs

- Le développeur manipule une **abstraction simple**.
- Il reste dans ses outils habituels (YAML dans un dépôt Git, ou le portail Backstage).
- L'équipe DevExperience garde la main sur ce qu'il y a derrière.

---

# Les arguments pour Crossplane
## Uniformiser la manière d'exposer ses services

- L'ensemble des équipes de la prod diffuse ses services **sous la même forme**.
- Trois modes de consommation cohabitent :

<div class="grid3">
<div class="card">
<h3>Équipes services</h3>
<p>gèrent et publient leurs briques.</p>
</div>
<div class="card">
<h3>DevExperience</h3>
<p>propose un assemblage prêt à l'emploi aux développeurs.</p>
</div>
<div class="card">
<h3>Développeurs</h3>
<p>consomment l'assemblage… ou une brique directement.</p>
</div>
</div>

---

# Les arguments pour Crossplane
## Politiques d'enforcement directement dans Kubernetes

- Tout passe par l'API Kubernetes → on récupère son écosystème de gouvernance (RBAC, Kyverno, OPA/Gatekeeper).
- On impose des règles **à la création** de la ressource :
  - « en prod, toute base doit être chiffrée »
  - « pas de policy contenant public »
  - « calcul de quotas »

<div class="keypoint">
La conformité devient <strong>systématique</strong>, plus une vérification manuelle après coup.
</div>

---

# Résumé — les bénéfices côté développeur

<div class="grid2">
<div class="card">
<h3>🚀 Self-service</h3>
<p>Il obtient sa ressource sans ticket ni attente.</p>
</div>
<div class="card">
<h3>🧭 Simplicité</h3>
<p>Une abstraction claire, sans connaître AWS/Azure/GCP ni l'outillage infra sous-jacent.</p>
</div>
<div class="card">
<h3>🛠️ Outils familiers</h3>
<p>Il reste dans Git / kubectl, son workflow habituel.</p>
</div>
<div class="card">
<h3>🔓 Autonomie & garde-fous</h3>
<p>Il consomme l'API avec ou sans portail ; sécurité et conformité sont gérées pour lui.</p>
</div>
</div>

---

# Résumé — les bénéfices côté ops / plateforme

<div class="grid2">
<div class="card">
<h3>🛡️ Gouvernance centralisée</h3>
<p>Politiques appliquées à la création (Kyverno / OPA), RBAC.</p>
</div>
<div class="card">
<h3>📐 Standardisation</h3>
<p>Un seul modèle, un seul workflow GitOps pour toutes les infras.</p>
</div>
<div class="card">
<h3>🔁 Évolution maîtrisée</h3>
<p>On change l'implémentation derrière le contrat → ça se propage tout seul.</p>
</div>
<div class="card">
<h3>👁️ Contrôle continu</h3>
<p>Moins de tickets répétitifs ; l'état réel est réconcilié en permanence, la dérive corrigée.</p>
</div>
</div>