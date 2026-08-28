# ADR-006 - Modèle de support : self-service et interlocuteur unique

| | |
|---|---|
| **Référence** | ADR-006 |
| **Statut** | Proposé : en cours de validation |
| **Auteurs** | Équipe DevExperience |
| **Public** | Équipe DevExperiencee · équipes capabilities · utilisateurs de la plateforme |


## Contexte

Le constat terrain révèle un problème systémique de support :

- Les développeurs ne savent pas à qui s'adresser ("est-ce KubeApp, IDDA, PDD, IAHS, le réseau ?")
- La connaissance repose sur une poignée de sachants (syndrome Anatole, mentionné dans plusieurs SNDI)
- Les canaux de communication sont fragmentés (50 canaux Tchap, mails, bouche à oreille)
- L'information arrive sans coordination ni visibilité

Verbatims terrain :
- *"Je demande à Anatole"* — mentionné plusieurs fois, dans plusieurs SNDI
- *"Les incidents ça arrive, mais communiquez"*
- *"Je ne sais pas, c'est pas dans mon périmètre"*

Le modèle de support doit répondre à deux attentes exprimées par les utilisateurs :

1. La plateforme doit être suffisamment bien conçue pour fonctionner en autonomie
2. En cas de besoin, un seul interlocuteur doit suffire

## Décision

### Principe : self-service d'abord, interlocuteur unique en fallback

Le modèle de support s'organise en **deux niveaux** :

#### Niveau 1 — Self-service (cible : 80% des interactions)

La plateforme doit permettre aux développeurs de trouver et faire ce dont ils ont besoin **sans assistance humaine** :

- **Documentation centralisée et contextualisée** : TechDocs liées à chaque service dans le portail, documentation des capability teams intégrée
- **Golden Paths guidés** : CLI et formulaires avec validation, pré-remplissage, messages d'erreur clairs
- **Annuaire et catalogue** : qui contacter pour quel sujet, état des services, dépendances
- **Runbooks et aide au diagnostic** : procédures documentées pour les incidents courants
- **Feed des changements** : historique centralisé, pas de surprise

L'investissement dans le self-service est la clé de la scalabilité (6 personnes pour 250 devs).

#### Niveau 2 — Interlocuteur unique (cible : 20% des interactions)

Quand le self-service ne suffit pas, un **canal unique** permet de poser des questions :

- **Un canal Tchap dédié** pour les questions rapides
- **Un système de ticketing** pour les demandes structurées
- L'équipe Platform Experience **qualifie** le besoin :
  - Si c'est dans son périmètre → elle traite
  - Si c'est du ressort d'une capability team → elle redirige vers la bonne équipe et suit la résolution
- Le développeur n'a **jamais** besoin de savoir quelle capability team contacter

### Ce que ce modèle remplace

| Avant | Après |
|-------|-------|
| "Je demande à Anatole" | Je cherche dans le portail |
| "C'est KubeApp ou IAHS ?" | Je contacte la plateforme, elle redirige |
| "J'ai vu un message sur Tchap en mars" | Je consulte le feed des changements |
| "Qui est responsable de ce service ?" | Je regarde le catalogue |
| "La doc est où ?" | TechDocs dans le portail, liée au service |

### Engagements de l'équipe Platform Experience

- Réponse sous 24h ouvrées sur le canal Tchap
- Qualification et redirection sous 48h pour les tickets
- Alimentation continue du self-service à partir des questions récurrentes (chaque question qui revient 3 fois → devient de la doc ou de l'automatisation)

## Conséquences

**Positif :**

- Fin du syndrome Anatole : la connaissance est dans la plateforme, pas dans les têtes
- Scalable : le self-service absorbe la majorité des interactions
- Expérience développeur simplifiée : un seul point de contact

**Négatif :**

- Le self-service n'est aussi bon que la documentation et les outils qui le portent → investissement initial important en Phase 1
- L'interlocuteur unique ne doit pas devenir un goulet d'étranglement → nécessite une bonne qualification et une redirection rapide
- Les capability teams doivent jouer le jeu de la documentation et de l'exposition d'interfaces

**Lien avec les ADR existantes :**

- S'appuie sur l'[Annexe 1 — Modèle d'interaction dev / Platform / Capability Teams](./annexe1/annexe-1-interaction-dev-platform.md)
