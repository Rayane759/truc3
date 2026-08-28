# Observabilité — piste à explorer

!!! warning "Statut"
    Contrairement aux autres pages de cette section (Backstage, Crossplane), **aucune expérimentation n'a été menée à ce jour** sur ce périmètre. Cette page pose le scope d'un POC à mener, pas un compte-rendu de résultats obtenus.

## Pourquoi ce POC

L'offre de service ([Domaine 6 — Observabilité & gestion d'incident](../index.md)) prévoit un dashboard unifié, des alertes pertinentes et une aide au diagnostic exposés au développeur depuis le portail. La stack d'observabilité elle-même (Argocd, Prometheus, Grafana, Loki, Elastic) reste hors périmètre de la plateforme — elle est produite et opérée par la capability team Observabilité (voir [ADR-002](../adr/adr-002-architecture-fonctionnelle.md)). Le rôle de la plateforme se limite à **consommer** cette stack et à en restituer une vue cohérente : c'est cette couche de restitution qui reste à expérimenter.

## Scope à tester

- **Intégration Backstage** : plugin(s) Grafana / ArgoCD déjà évoqués dans [pocs/index.md](./index.md) — vérifier ce qu'ils exposent réellement (dashboards embarqués, état de synchro, alertes) et ce qu'il faut développer en plus pour une vue par service.
- **Alertes filtrées et pertinentes** : aujourd'hui perçues comme du bruit (constat terrain — voir [UC13](../../constat-terrain/synthese/cas_utilisation.md)) ; un POC devrait tester un mécanisme de filtrage/priorisation avant restitution dans le portail, pas seulement un relais brut des alertes existantes.
- **Aide au diagnostic automatisé** (UC14) : à quel point peut-on croiser logs/métriques/traces automatiquement pour proposer une première piste de recherche, sans réimplémenter l'expertise de la capability team Observabilité ? Un POC avec un MCP branché sur les différents outils d'observabilité pourrait être intéressant.

## Questions ouvertes

- Dashboard unifié : que veulent vraiment les devs ? 