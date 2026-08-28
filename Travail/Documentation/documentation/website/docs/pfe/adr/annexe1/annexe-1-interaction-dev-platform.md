# ADR — Modèle d’interaction entre développeurs, Platform (DevEx) et Capability Teams

## Statut

Proposé

## Contexte

L’organisation actuelle comporte plusieurs équipes techniques (capabilities) fournissant des services (data, IAM, runtime, observabilité, etc.) utilisés par les équipes de développement.

Les développeurs interagissent fréquemment directement avec ces équipes pour :

* demander de nouvelles fonctionnalités
* configurer des services
* résoudre des problèmes

Cela entraîne :

* une fragmentation des demandes
* une forte dépendance entre équipes
* une incohérence dans les solutions mises en place
* une surcharge des équipes capabilities
* une coordination réalisée par les devs (parfois les archis)

Dans le cadre de la mise en place d’une Internal Developer Platform (IDP), il est nécessaire de clarifier les interactions entre :

* les développeurs
* l’équipe Platform / Developer Experience (DevEx)
* les capability teams

---

## Décision

Nous adoptons un modèle d’interaction structuré :

1. **La Platform (DevEx) devient le point d’entrée principal pour les développeurs**


   * self-service via un portail (IDP)
   * collecte et qualification des nouveaux besoins
   * Analyse du besoin et conseils de premier niveau

    **Objectifs**: Réduire le nombre d'interlocuteur différents pour les devs

2. **Les capability teams exposent leurs capacités via des interfaces standardisées**

   * APIs
   * Infrastructure as Code
   * services automatisés

    **Objectifs**: Permettre la consommation en X-as-a-service.


3. **Les développeurs utilisent les capabilities principalement via la plateforme**

   * sans interaction humaine dans les cas standards

    **Objectifs**: Catalogue centralisé, réduire la dette cognitive, favoriser l'onboarding rapide

4. **Les nouveaux besoins passent par la Platform (DevEx)**


   * consolidation
   * priorisation
   * transformation en fonctionnalités plateforme

    **Objectifs**: C'est l'équipe DevExp qui identifie si le besoin doit être intégrer dans la plateforme (mise à disposition pour tous) ou non. Dans le cadre de la mise à disposition par le biais de la plateforme l'équipe DevExp se positionne en tant qu'architecte/client auprès des différentes capabilities pour implémenter la solution dans sa globalitié. Si la demande du développeur n'a pas vocation a s'intégrer dans la plateforme elle est redirigé directement vers les équipes capabilities.

5. **Les interactions directes Dev ↔ Capability restent possibles mais limitées à :**


   * incidents
   * support technique ponctuel
   * collaboration sur des cas spécifiques
   * expertise technique sur des points clés

    **Objectifs**: Garder le contact avec les utilisateurs sur son domaine spécifique sans créer du service qui ne pourrait pas être intégrés dans la plateforme.

6. **Les évolutions de la plateforme ne sont pas implémentées directement suite à des demandes individuelles**

   * elles sont structurées et intégrées via la Platform

---

## Conséquences

### Bénéfices

* Réduction des dépendances entre équipes
* Amélioration de l’autonomie des développeurs
* Expérience développeur plus cohérente
* Diminution des demandes ad hoc
* Meilleure priorisation des évolutions plateforme
* Réduction de la charge sur les capability teams

### Inconvénients / Risques

* Risque de perception d’un point de passage central (DevEx)
* Nécessité d’une forte maturité produit côté Platform
* Besoin de gouvernance claire entre DevEx et capability teams
* Changement culturel important


## Alternatives considérées

### 1. Interaction directe Dev ↔ Capability uniquement

* Avantage : simplicité apparente
* Inconvénient : fragmentation, incohérence, dépendances fortes

### 2. Ajout d’une équipe DevEx sans changement des interactions

* Avantage : faible impact organisationnel
* Inconvénient : DevEx devient un intermédiaire / goulot


## Principes clés

- Self-service par défaut
- Interaction humaine uniquement lorsque nécessaire
- Standardisation des besoins récurrents
- Autonomie des équipes sans perte de cohérence
- Plateforme comme produit interne


## Résumé

Le développeur interagit principalement avec la plateforme pour les usages standards, tandis que les capability teams fournissent des capacités techniques consommées via des interfaces. La Platform (DevEx) structure les besoins et garantit la cohérence globale, tout en laissant possible une interaction directe ponctuelle avec les capabilities.