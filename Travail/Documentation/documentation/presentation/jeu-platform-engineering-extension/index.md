---
marp: true
theme: uncover
title: Platform Engineering
author: Donatien ENEMAN
_class: invert
transition: fade
markdown.marp.enableHtml: true
style: |
  section.obstacle {
    font-size: 20px;
    text-align: left;
    background: 
      linear-gradient(rgba(255, 5, 5, 0.78), rgb(182, 5, 5)),
      url('ton-image.jpg') center/cover no-repeat;
    color: white;
  }


  section.dsi {
    font-size: 20px;
    text-align: left;
    background: 
      linear-gradient(rgba(5, 255, 234, 0.5), rgba(122, 211, 252, 0.5)),
      url('ton-image.jpg') center/cover no-repeat;
    color: white;
  }

---


<!-- _class: obstacle -->

# 🟥 Poste mal configuré

## **Contexte :** configuration locale incomplète  

## **Effet :**

- ⏱ +10 min
- 🔁 Retour `Dev`

---

<!-- _class: obstacle -->

# 🟥 Initializer incomplet

## **Contexte :** Spring Initializr mal configuré  

## **Effet :**

- 🔁 Rejouer bloc setup projet

---

<!-- _class: obstacle -->

# 🟥 Repo mal initialisé

## **Contexte :** repo sans règles, README, conventions  

## **Effet :**

- ⏱ +10 min

---

<!-- _class: obstacle -->

# 🟥 Sécurité mal configurée

## **Contexte :** Spring Security / Swagger incorrect  

## **Effet :**

- 🔁 Retour `Dev`

---

<!-- _class: obstacle -->

# 🟥 GitLab CI KO

## **Contexte :** pipeline ne démarre pas  

## **Effet :**

- 🔁 Retour `Build`

---

<!-- _class: obstacle -->

# 🟥 Dockerfile invalide

## **Contexte :** image ne build pas  

## **Effet :**

- 🔁 Rejouer `Build`

---

<!-- _class: obstacle -->

# 🟥 Renovate casse le build

## **Contexte :** dépendance incompatible  

## **Effet :**

- 🔁 Retour `Build` + `Test`

---

<!-- _class: obstacle -->

# 🟥 Tests instables

## **Contexte :** flaky tests  

## **Effet :**

- 🔁 Rejouer `Test`

---

<!-- _class: obstacle -->

# 🟥 Sonar bloque

## **Contexte :** quality gate KO  

## **Effet :**

- 🔁 Retour `Dev`

---

<!-- _class: obstacle -->

# 🟥 Validation manuelle

## **Contexte :** QA obligatoire  

## **Effet :**

- ⏱ +1 min

---

<!-- _class: obstacle -->

# 🟥 GitOps mal configuré

## **Effet :**

- 🔁 Retour `Deploy`

---

<!-- _class: obstacle -->

# 🟥 Vault inaccessible

## **Effet :**

- 🔁 Retour `Test`

---

<!-- _class: obstacle -->

# 🟥 Keycloak mal configuré : refaîte le ticket

## **Effet :**

- 🔁 Retour `Deploy`
- Rejouer Bloc IAHS

---

<!-- _class: obstacle -->

# 🟥 KubeApp est en inter-ité

## **Effet :**

- ⏱ + 1 journée

---

<!-- _class: obstacle -->

# 🟥 BDD ma configuré

## **Effet :**

- 🔁 Retour `Deploy`
- Rejouer Bloc PDD

---

<!-- _class: obstacle -->

# 🟥 Jobs manquants

## **Effet :**

- 🔁 Rejouer Setup BDD

---

<!-- _class: obstacle -->

# 🟥 Backup non configuré

## **Effet :**

- 🔁 Rejouer Setup BDD

---

<!-- _class: obstacle -->

# 🟥 Logs introuvables

## **Effet :**

- 🔁 Ticket à Observabilité vous prenez +1j

---

<!-- _class: obstacle -->

# 🟥 Monitoring absent

## **Effet :**

- vous devez créer un autre environnement rejouer deploy

---

<!-- _class: obstacle -->

# 🟥 Debug prod difficile

## **Effet :**

- 🔁 Retour `Test`

---

<!-- _class: dsi -->

# ⚡ E1 — Audit sécurité surprise

## **🎯 Contexte :**
Une équipe sécurité lance un audit non prévu.
Tous les services doivent être conformes immédiatement.

## **💥 Effet jeu :**
- Équipes **sans Policy as Code** :
  - Réunion 1h avec PO LeadTech et DSMR
  - ⏱ +1 journée
  - doivent "justifier" leur config

<br/>


- Équipes **avec Policy as Code** :
  - ✅ aucun impact

## **🧠 Ce que ça démontre :**
- sans standardisation → effort manuel énorme
- avec plateforme → conformité automatique

---
<!-- _class: dsi -->

# ⚡ E2 — Black Friday (pic de trafic)

## **🎯 Contexte :**
Le trafic explose brutalement (x10).

## **💥 Effet jeu :**
- Sans Observability :
  - ⏱ 1/2 journée
  - confusion (logs difficiles, pas de métriques)

<br/>


- Avec Observability :
  - ✅ pas de pénalité
  - réaction rapide

## **🧠 Ce que ça démontre :**
- visibilité = clé en production
- sans métriques → perte de temps énorme

---
<!-- _class: dsi -->

# ⚡ E3 — Incident production

## **🎯 Contexte :**
Un bug critique apparaît en production.

## **💥 Effet jeu :**
- Sans runtime standardisé :
  - 🔁 retour `Test`
  - besoin de reproduire le bug

<br/>


- Avec runtime standardisé :
  - ⏱ +30 sec seulement

## **🧠 Ce que ça démontre :**
- environnement cohérent = debug rapide
- sinon → "works on my machine"

---
<!-- _class: dsi -->

# ⚡ E4 — Nouveau développeur arrive

## **🎯 Contexte :**
Un nouveau dev rejoint l’équipe.

## **💥 Effet jeu :**
- Sans Golden Path :
  - ⏱ 1/2 journée (onboarding)
  - confusion / setup manuel

<br/>

- Avec Golden Path :
  - ⏱ +1 minutes

## **🧠 Ce que ça démontre :**
- onboarding = indicateur clé DX
- plateforme réduit drastiquement le temps d’entrée

---
<!-- _class: dsi -->

# ⚡ E5 — Migration cloud

## **🎯 Contexte :**
L’entreprise migre une partie de ses workloads.

## **💥 Effet jeu :**

- Sans Self-Service Infra :

  - ⏱ +3 jours
  - dépendance forte à l’infra

<br/>

- Avec Self-Service Infra :
  - ✅ aucun impact

## **🧠 Ce que ça démontre :**
- abstraction infra = clé de résilience
- sinon → friction énorme

