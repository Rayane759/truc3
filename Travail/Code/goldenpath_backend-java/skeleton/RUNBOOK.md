# Runbook — ${{ values.name }}

Ce document décrit les procédures opérationnelles du service `${{ values.artifactId }}`.  
Il s'adresse aux développeurs et à l'équipe platform en cas d'incident.

---

## Informations générales

| Propriété       | Valeur                                      |
|-----------------|---------------------------------------------|
| Service         | ${{ values.name }}                          |
| Équipe          | ${{ values.team }}                          |
| Environnements  | dev · staging · prod                        |
| Repo GitLab     | <URL_REPO>                                  |
| ArgoCD          | <URL_ARGOCD>                                |
{%- if values.hasObservability %}
| Grafana         | <URL_GRAFANA>                               |
{%- endif %}

---

## Démarrage et arrêt

### Démarrer le service

Le service est géré par ArgoCD — il n'y a pas de démarrage manuel en production.  
Pour forcer une resynchronisation :

```bash
argocd app sync ${{ values.artifactId }}
```

### Redémarrer un pod

```bash
kubectl rollout restart deployment/${{ values.artifactId }} -n <NAMESPACE>
```

### Vérifier l'état du service

```bash
kubectl get pods -n <NAMESPACE> -l app=${{ values.artifactId }}
kubectl describe pod <NOM_DU_POD> -n <NAMESPACE>
```

---

## Consulter les logs

{%- if values.hasObservability %}
Les logs sont centralisés dans **Grafana / Loki** : `URL_GRAFANA`

Filtres utiles dans Loki :

`?????????`

{%- endif %}

Logs en temps réel via kubectl :

```bash
kubectl logs -f deployment/${{ values.artifactId }} -n <NAMESPACE>
```

---

## Health checks

| Endpoint                     | Description                  |
|------------------------------|------------------------------|
| `/actuator/health`           | État général du service      |
| `/actuator/health/liveness`  | Liveness probe               |
| `/actuator/health/readiness` | Readiness probe              |
{%- if values.hasObservability %}
| `/actuator/prometheus`       | Métriques Prometheus         |
{%- endif %}

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
argocd app history ${{ values.artifactId }}

# Revenir à une révision précédente
argocd app rollback ${{ values.artifactId }} <REVISION>
```

{%- if values.hasVault %}

### Problème d'accès aux secrets Vault

1. Vérifier que le pod a bien accès à Vault :

    ```bash
    kubectl exec -it <POD> -n <NAMESPACE> -- curl $VAULT_ADDR/v1/sys/health
    ```

2. Consulter [la documentation Vault]([LIEN_DOC_VAULT](https://gitlab.insee.fr/iahs/secrets/documentation/doc-publique/-/wikis/home))

3. Contacter l'équipe platform si le problème persiste
{%- endif %}

---

## Contacts

| Rôle               | Contact                                   |
|--------------------|-------------------------------------------|
| Équipe             | ${{ values.team }}                        |
| Responsable        | <Prénom NOM — `prenom.nom@insee.fr`>      |
| Équipe platform    | <CONTACT_EQUIPE_PLATFORM>                 |
| Astreinte          | <CONTACT_ASTREINTE>                       |
