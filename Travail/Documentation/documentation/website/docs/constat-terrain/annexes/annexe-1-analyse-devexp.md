# Analyse DevExp – Janvier 2026

## Méthodologie:

- retraitement du fichier original pour anonymiser/synthetiser/réduire le nombre de colonnes.
  - fichiers disponible ici : https://gitlab.insee.fr/platform-engineering/documentation/-/blob/main/documents/devexp_2026-01-26_treated.csv?ref_type=heads
  - code ici : https://gitlab.insee.fr/platform-engineering/tools/devexp
- Utilisation d'une IA à partir du jeu de données généré et d'un prompt 
  - Prompt disponible ici: https://gitlab.insee.fr/platform-engineering/documentation/tools/devexp/resources/template.md.j2
- Retraitement du rapport généré par IA


## Résumé exécutif

Cette analyse repose sur une enquête DevExp interne menée en janvier 2026 auprès de 250 développeurs, avec un échantillon exploitable de **134 répondants (54%)**.  
Globalement, l’expérience développeur est **plutôt satisfaisante (≈3,5/5)**, avec des points forts identifiés sur l’outillage et certaines offres DevOps.  
Les principales **frictions** concernent :

- la **clarté des responsabilités et des supports**
- la **formation**
- la **cohérence et la lisibilité de l’écosystème**
- la **communication transverse**

Les résultats suggèrent un fort potentiel pour une **plateforme engineering interne**, à condition qu’elle soit pensée comme un **point d’entrée unifié**, orientée autonomie et accompagnement.

---

## Démarche d’analyse

### Approche quantitative

- Calcul des moyennes par question (Q3 à Q10)
- Prise en compte du nombre de réponses effectives (fort taux de non-réponse sur certaines questions)
- Pas de normalisation ni de pondération

### Approche qualitative

- Lecture transversale des commentaires libres (Q3 à Q12)
- Regroupement thématique (outillage, support, formation, organisation, communication)
- Extraction de signaux faibles et récurrents

### Principe clé

👉 **Aucune inférence causale directe** : les interprétations sont présentées comme hypothèses.

---

## Synthèse des résultats quantitatifs (faits)

| Question | Thème                           | Moyenne /5 | Nb réponses |
| -------- | ------------------------------- | ---------- | ----------- |
| Q3       | Offre d’outils de développement | **3,81**   | 105         |
| Q4       | Services DevOps VM              | **3,40**   | 88          |
| Q5       | Services DevOps Kubernetes      | **3,96**   | 79          |
| Q6       | Déploiement & CI/CD             | **3,51**   | 89          |
| Q7       | Support & accompagnement        | **3,12**   | 67          |
| Q8       | Documentation                   | **3,45**   | 83          |
| Q9       | Formation                       | **3,55**   | 83          |
| Q10      | Expérience développeur globale  | **3,53**   | 93          |

**Constat factuel** :

- Les notes sont globalement homogènes (entre 3,1 et 4)
- Kubernetes est mieux perçu que les services VM (Bourrage d'urne du SNDIP ??)
- Le support est le point le plus faible
- Plus on avance dans le questionnaire moins on a de réponses.

---

## Points de convergence et de divergence

### Points de convergence (fort consensus)

**Faits observés**

- L’outillage progresse positivement
- Les briques DevOps sont globalement appréciées
- L’expérience sur les outils de développement est jugée correcte à bonne

**Verbatims récurrents**

- « les outils sont bien mais… »
- « l’offre existe mais manque de clarté »
- « difficile de savoir à qui s’adresser »

## Focus – Documentation : un irritant majeur mais souvent implicite

### Constat général

La documentation apparaît comme l’un des **principaux points de désagrément** de l’expérience développeur, bien qu’elle soit **rarement nommée explicitement comme telle** dans les réponses chiffrées.  
Elle constitue un **problème transversal**, qui alimente plusieurs autres irritants identifiés (support, formation, autonomie, lisibilité de l’écosystème).

---

### Éléments factuels

- La question relative à la documentation (Q8) obtient une note moyenne d’environ **3,45 / 5**
- Cette note intermédiaire masque une **forte hétérogénéité des expériences**
- Les verbatims font très fréquemment référence à des difficultés d’accès à l’information, de compréhension ou de fiabilité, même lorsque le terme “documentation” n’est pas explicitement utilisé

---

### Principales formes de désagrément liées à la documentation

#### Documentation inexistante ou insuffisante
- Information absente ou incomplète
- Connaissance détenue par un nombre limité de personnes
- Forte dépendance au support ou aux collègues

**Effets observés**
- Perte d’autonomie
- Temps de résolution allongé
- Frustration en cas d’indisponibilité des personnes clés

---

#### Documentation éparpillée
- Multiplication des espaces et des sources
- Difficulté à identifier la “bonne” documentation
- Informations redondantes ou contradictoires

**Effets observés**
- Charge cognitive élevée
- Manque de confiance dans l’information disponible
- Coût de recherche supérieur au bénéfice perçu

---

#### Documentation trop complexe ou trop experte
- Contenus orientés experts
- Peu de parcours progressifs ou pédagogiques
- Manque d’exemples concrets et actionnables

**Effets observés**
- Barrière à l’entrée pour certains profils
- Auto-censure dans l’usage des outils
- Apprentissage lent et non structuré

---

### Un problème transversal

Les problématiques de documentation se retrouvent indirectement dans :
- Les critiques sur le **support** (Q7)
- Les attentes en matière de **formation** (Q9, Q11)
- Le manque de **lisibilité globale de l’écosystème**
- Les difficultés d’**onboarding**

La documentation ne joue donc pas pleinement son rôle de **substitut au support humain**.

---

### Reformulation synthétique du problème

> L’information existe parfois, mais elle est difficile à trouver, à comprendre et à utiliser au bon moment.

Ou, de manière équivalente :

> La documentation actuelle ne permet pas aux développeurs d’être pleinement autonomes.

---

### Positionnement par rapport aux autres contraintes

En intégrant correctement le sujet de la documentation, la hiérarchie des principaux désagréments devient :

1. Manque de clarté et de lisibilité globale (outils, responsabilités, information)
2. Documentation inexistante, dispersée ou trop complexe
3. Support difficile à identifier et à activer
4. Formation insuffisamment structurée ou contextualisée
5. Expérience développeur très variable selon les services
6. Limites techniques de certains services (notamment VM)

---

### Hypothèse structurante (à expliciter comme telle)

> Une documentation centralisée, contextualisée et orientée usages pourrait réduire significativement les irritants liés au support, à la formation et à l’autonomie des développeurs.

⚠️ Cette hypothèse devra être validée par des investigations complémentaires (ateliers, tests utilisateurs, analyses d’usage).

---

### 4.2 Points de divergence (forte variabilité)

**Support & responsabilités**

- Certains équipes très autonomes
- D’autres en forte dépendance avec un sentiment d’abandon

**Formation**

- Jugée utile par certains
- Jugée insuffisante, mal ciblée ou trop tardive par d’autres

**Organisation**

- Variabilité forte selon le service (Q2)

---

## 5. Biais et limites

### 5.1 Biais d’échantillonnage

- 54% de taux de réponse : possible sur-représentation des profils engagés ou insatisfaits

### 5.2 Biais lié à la question Q2 (service)

- Forte hétérogénéité des réalités selon les services
- Certaines frustrations semblent organisationnelles plus que techniques
- ⚠️ Risque de surinterprétation globale de problèmes locaux

### 5.3 Biais de non-réponse

- Certaines questions clés ont moins de 70 réponses
- Les moyennes doivent être lues comme **indicateurs**, pas comme des vérités absolues

---

## 6. Profils utilisateurs (hypothèses)

> ⚠️ Profils construits par regroupement de signaux, non par clustering statistique.

### 6.1 Le Développeur Autonome

- Notes élevées
- Peu de commentaires
- Utilise efficacement l’existant
- Besoin principal : stabilité, cohérence, self-service

### 6.2 Le Développeur Bloqué par l’Organisation

- Frustration sur le support et la communication
- Problèmes de responsabilités floues
- Besoin : clarté, points de contact, parcours explicites

### 6.3 Le Développeur en Montée en Compétence

- Attentes fortes sur la formation
- Souvent utilisateur de Kubernetes / CI/CD
- Besoin : onboarding, documentation pédagogique, exemples

### 6.4 Le Développeur Dépendant du Support

- Notes faibles sur Q7
- Verbatims orientés « personne ne sait », « pas de réponse »
- Besoin : support structuré, SLA, visibilité

---

## 7. Besoins identifiés pour une plateforme engineering

### 7.1 Besoins transverses (faits + hypothèses)

**Faits**

- Difficulté à s’orienter
- Multiplicité des outils
- Manque de lisibilité du support

**Hypothèses**

- Une plateforme pourrait réduire la charge cognitive
- Centraliser ≠ simplifier automatiquement (risque)

---

### 7.2 Correspondance besoins ↔ profils

| Besoin                             | Profils concernés              |
| ---------------------------------- | ------------------------------ |
| Point d’entrée unique              | Tous                           |
| Documentation contextualisée       | Autonome, Montée en compétence |
| Parcours guidés                    | Montée en compétence           |
| Annuaire support & responsabilités | Bloqué, Dépendant              |
| Self-service DevOps                | Autonome                       |
| Visibilité roadmap outils          | Tous                           |

---

## 8. Opportunités pour la plateforme engineering

### 8.1 Opportunités fortes

- Réduire les frictions organisationnelles sans changer l’orga
- Rendre l’existant plus visible et actionnable
- Améliorer la perception du support sans nécessairement l’augmenter

### 8.2 Points de vigilance

- Ne pas devenir une couche de plus
- Éviter une plateforme uniquement « vitrine »
- Travailler l’expérience avant la couverture fonctionnelle

---

## 9. Conclusion

L’enquête met en évidence une **base solide mais fragmentée**.  
La valeur d’une plateforme engineering ne réside pas tant dans l’ajout de nouveaux outils que dans :

- la **clarification**
- la **cohérence**
- la **mise en capacité des développeurs**

👉 Le principal levier d’amélioration semble être **l’expérience d’usage**, plus que la technologie elle-même.
