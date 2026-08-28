# Runbook — Test-applijava

Ce document décrit les procédures opérationnelles du service `applitestlocal`.  
Il s'adresse aux développeurs et à l'équipe platform en cas d'incident.

---

## Informations générales

| Propriété       | Valeur                                      |
|-----------------|---------------------------------------------|
| Service         | Test-applijava                          |
| Équipe          | team-platform                          |
| Environnements  | dev · staging · prod                        |
| Repo GitLab     | <URL_REPO>                                  |
| ArgoCD          | <URL_ARGOCD>                                |

---

## Démarrage et arrêt

### Démarrer le service

Le service est géré par ArgoCD — il n'y a pas de démarrage manuel en production.  
Pour forcer une resynchronisation :

```bash
argocd app sync applitestlocal
```

### Redémarrer un pod

```bash
kubectl rollout restart deployment/applitestlocal -n <NAMESPACE>
```

### Vérifier l'état du service

```bash
kubectl get pods -n <NAMESPACE> -l app=applitestlocal
kubectl describe pod <NOM_DU_POD> -n <NAMESPACE>
```

---

## Consulter les logs

Logs en temps réel via kubectl :

```bash
kubectl logs -f deployment/applitestlocal -n <NAMESPACE>
```

---

## Health checks

| Endpoint                     | Description                  |
|------------------------------|------------------------------|
| `/actuator/health`           | État général du service      |
| `/actuator/health/liveness`  | Liveness probe               |
| `/actuator/health/readiness` | Readiness probe              |

```bash
# Vérification rapide depuis l'extérieur
curl https://<!--URL_SERVICE-->/actuator/health
```

---

## Procédures en cas d'alerte

### Le service ne répond plus

1. Vérifier l'état des pods : `kubectl get pods -n <NAMESPACE>`
2. Consulter les logs du pod défaillant : `kubectl logs <POD> -n <NAMESPACE>`
3. Vérifier l'état ArgoCD : `<URL_ARGOCD>`
4. Si le problème persiste : contacter <!--CONTACT_ASTREINTE-->

### Erreurs en masse dans les logs

1. Identifier l'erreur dans Grafana / Loki : `<URL_GRAFANA>`
2. Vérifier les derniers déploiements dans ArgoCD
3. Si lié à un déploiement récent : effectuer un rollback (voir ci-dessous)

### Effectuer un rollback

```bash
# Lister les révisions disponibles
argocd app history applitestlocal

# Revenir à une révision précédente
argocd app rollback applitestlocal <REVISION>
```

---

## Contacts

| Rôle               | Contact                                   |
|--------------------|-------------------------------------------|
| Équipe             | team-platform                        |
| Responsable        | <Prénom NOM — `prenom.nom@insee.fr`>      |
| Équipe platform    | <CONTACT_EQUIPE_PLATFORM>                 |
| Astreinte          | <CONTACT_ASTREINTE>                       |
