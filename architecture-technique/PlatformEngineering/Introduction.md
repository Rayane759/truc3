# Introduction

## Objectif

_L'objectif de ce document est de maîtriser la cartographie du système d’information durant tout son cycle de vie, en vue d’en identifier les risques inhérents et d’y associer les mesures adaptées._

## Documents associés

_Le présent dossier comporte les parties fonctionnelles et applicatives d’un dossier d’architecture technique. La partie « technique » étant d’un cycle de vie et d’une sensibilité très différents, elle sera reconstruite, sur demande, auprès de l’exploitant et devra contenir à minima :_

- _une liste exhaustive des équipements (VM, sécurité) avec
  leurs niveaux de version en termes d'OS et de middleware_
- _une liste exhaustive des flux internes au SI et externes au SI_
- _une liste des procédures d'installation, d'exploitation et de MCS_
- _une liste des profils utilisateurs et leurs niveaux de droit_

| Document | Référence | Responsable de la mise à jour | Liens |
|---|---|---|---|
| Dossier architecture SI DevOps | TODO | IDDA | TODO |

<span style="color:red">**Document Interne, ne pas diffuser hors de l'INSEE**</span>

date de mise à jour : 31/08/2026

L'objectif de ce document est de maitriser la cartographie du système d'information durant tout son cycle de vie, en vue d'en identifier les risques inhérents et d'y associer les mesures adaptées.

> **Note préliminaire** — Le produit PlatformEngineering (abbrégé en PFE) est un produit technique transverse et non une application métier. Les rubriques du présent dossier sont renseignées en conséquence : les "utilisateurs" sont les équipes du SI Insee, les "données" sont essentiellement du code, de la configuration et des secrets opérationnels (et non des données métier statistiques).

## Présentation générale

Le PlateformEngineering (PFE) est un ensemble de produits techniques internes mis à disposition des équipes applicatives de l'Insee. Elle offre un parcours pour le développement unifié, du démarrage d'un projet jusqu'au déploiement en production et à son exploitation, couvrant les trois substrats d'exécution du SI : Kubernetes, parc VM on-prem (en best-effort), et cloud souverain (cible à moyen terme).

La PFE industrialise les bonnes pratiques DevOps construites au sein de l'Insee depuis 2020 : elle ne remplace ni les équipes services du DPII (aussi appelée capability-teams) ni les expertises métiers (Architectes/Urbanisation/DSMR), elle outille leur mise à disposition aux équipes applicatives sous forme de services self-service, accessibles par un point d'entrée unique (portail développeur). Elle s'inscrit dans le modèle organisationnel Team Topologies, l'équipe Platform Experience (au sein d'IDDA) étant propriétaire du produit "PlateformEngineering".

La démarche, les besoins, les décision fonctionnelle et stratégique de la PFE sont documentée dans l'espace documentaire suivant: [espace-documentaire-pfe](https://platform-engineering.gitlab-pages.insee.fr/documentation/) .

### Périmètre

Le périmètre du système d'information couvert par ce document est le suivant.

**Données traitées par la PFE** : code source des applications (via dépôts Git), code source des Compositions et templates de plateforme, manifestes de déploiement, artefacts construits (images de conteneurs, paquets), secrets opérationnels (tokens techniques, credentials de services), configuration GitOps, métadonnées du catalogue (services, équipes, propriétaires), métriques et logs de la plateforme elle-même.

**Hors périmètre** : les données métier statistiques traitées par les applications hébergées ne transitent pas par la PFE ; elles relèvent du DAT de chaque application cliente. La PFE fournit le substrat d'exécution et les services transverses, pas le stockage métier.

**Limites du SI** : la PFE est un produit interne sans exposition externe directe. Les seules interfaces extérieures sont les flux de récupération de dépendances logicielles depuis les registres publics (via miroirs Nexus internes), et à terme les flux vers le cloud souverain pour les workloads concernés.


