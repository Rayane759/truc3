---
marp: true
theme: uncover
title: Platform Engineering
author: Donatien ENEMAN
_class: invert
transition: fade
markdown.marp.enableHtml: true
style: |
  section {
    font-size: 20px;
    text-align: left;
    background: 
      linear-gradient(rgba(47, 34, 78, 0.5), rgba(20, 1, 71, 0.5)),
      url('ton-image.jpg') center/cover no-repeat;
    color: white;
    
  }

  section.title {
    position: relative;
    background: #1e1e1e;
    color: white;
    padding: 60px;
  }

  section.title img {
    position: absolute;
    top: 40px;
    right: 40px;
    width: 100px;
  }

---

<!-- _class: title -->

![w:160](./../dev/assets/title.svg)
# Platform Engineering 

**Objectifs** : Découvrons les pouvoirs de la plateforme

---

## Un monde sans plateforme 

- Un Board rempli par des devs, estimons la charge pour chacune des grandes cases
[https://platform-engineering.gitlab-pages.insee.fr/documentation/autres/focusgroupe/board.drawio.png](https://platform-engineering.gitlab-pages.insee.fr/documentation/autres/focusgroupe/board.drawio.png)
- Un board détaillé : [https://platform-engineering.gitlab-pages.insee.fr/documentation/autres/focusgroupe/sndil-board.drawio.png](https://platform-engineering.gitlab-pages.insee.fr/documentation/autres/focusgroupe/sndil-board.drawio.png)
- Pour participer : https://poker-planning.demo.insee.io/game/a1aad4f8-4fec-431d-9dee-65acac0fb8c5

![](./assets/image.png)


---

## Un monde avec plateforme

- Présentation des capabilities

---

# Les fonctionnalitées potentielles de la platformEngineering

---


# 🟩 C1 — Golden Path (Template applicatif complet)

## **🎯 Problème :**

- setup projet long
- configs répétées (Spring, sécurité, Swagger)
- différences entre équipes

## **⚙️ Fournit :**

- template prêt à l’emploi (Spring Boot)
- sécurité + Swagger + config de base intégrés
- conventions standard (structure, config, dépendances)

## **🧠 Impact :**

- onboarding rapide
- homogénéité des services
- réduction du cognitive load

---

# 🟩 C2 — Dev Environment Standardisé

## **🎯 Problème :**

- “ça marche sur ma machine”
- dépendances locales instables

## **⚙️ Fournit :**

- environnement dev standard (Docker / devcontainer)
- versions figées
- scripts de démarrage

## **🧠 Impact :**

- moins de bugs liés à l’environnement
- onboarding accéléré

---

# 🟩 C3 — CI/CD Pipeline Standard

## **🎯 Problème :**

- pipelines fragiles et différents
- duplication de config

## **⚙️ Fournit :**

- pipeline GitLab standardisé
- stages prêts (build, test, scan)
- cache et optimisation

## **🧠 Impact :**

- fiabilité
- gain de temps
- standardisation

---

# 🟩 C4 — Build & Dependency Management sécurisé

## **🎯 Problème :**

- Dockerfiles incohérents
- dépendances cassent le build

## **⚙️ Fournit :**

- Dockerfile template
- règles Renovate maîtrisées
- validation automatique


## **🧠 Impact :**
- builds stables
- moins d’incidents

---

# 🟩 C5 — Environnements de test éphémères

## **🎯 Problème :**

- tests instables
- dépendances partagées
- validation manuelle

## **⚙️ Fournit :**

- environnement isolé par feature
- auto-provisioning
- données de test

## **🧠 Impact :**

- tests fiables
- feedback rapide

---

# 🟩 C6 — Self-Service Infrastructure (KubApp)

## **🎯 Problème :**

- dépendance infra
- attente longue

## **⚙️ Fournit :**

- création namespace automatique
- provisioning à la demande

## **🧠 Impact :**

- autonomie équipes
- réduction du lead time

---

# 🟩 C7 — GitOps prêt à l’emploi

## **🎯 Problème :**

- config complexe et fragile

## **⚙️ Fournit :**

- repo GitOps généré
- config standard
- synchro automatique

## **🧠 Impact :**

- déploiements fiables
- auditabilité

---
# 🟩 C8 — Platform Integrations (Secrets + Auth + IAM)

## **🎯 Problème :**

- Vault, Keycloak, AD = complexe et manuel

## **⚙️ Fournit :**

- intégration automatique avec :
  - Vault (secrets)
  - Keycloak (auth)
  - IAM (droits)

## **🧠 Impact :**

- sécurité by default
- moins de dépendances externes

---
# 🟩 C9 — Provisioning automatisé (BDD + ressources)

## **🎯 Problème :**

- dépendance DBA / ops
- provisioning lent

## **⚙️ Fournit :**

- création BDD automatique
- ressources infra prêtes

## **🧠 Impact :**

- autonomie complète
- accélération delivery

---
# 🟩 C10 — Observability by Default

## **🎯 Problème :**

- logs difficiles
- manque de visibilité
- debugging lent

## **⚙️ Fournit :**

- logs, metrics, traces automatiques
- dashboards prêts
- alerting intégré

## **🧠 Impact :**
- MTTR réduit
- meilleure exploitation

---
# Résumé 

- 🟩 C1 — Golden Path (Template applicatif complet)
- 🟩 C2 — Dev Environment Standardisé
- 🟩 C3 — CI/CD Pipeline Standard
- 🟩 C4 — Build & Dependency Management sécurisé
- 🟩 C5 — Environnements de test éphémères
- 🟩 C6 — Self-Service Infrastructure (KubApp)
- 🟩 C7 — GitOps prêt à l’emploi
- 🟩 C8 — Platform Integrations (Secrets + Auth + IAM)
- 🟩 C9 — Provisioning automatisé (BDD + ressources)
- 🟩 C10 — Observability by Default

---
# Sondage:

- Laquelle préferez vous : 
    - Pour participer : https://poker-planning.demo.insee.io/game/a1aad4f8-4fec-431d-9dee-65acac0fb8c5

![](./assets/image.png)

---

# Let's Play Again

- Rejouons le jeu précédent avec ces nouvelles capabilities

