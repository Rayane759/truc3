# COMPAS
## Objectifs de Compas
- **C**ollecter des informations (sans rechercher la justesse - un indicateur ne représente pas la vérité)
- **O**bserver le SI et ses composantes
- **M**esurer les avancements, les écarts aux objectifs fixés et aux prévisions
- **P**révoir l'évolution des performances des SI, les risques potentiels (saturation, goulet d'étranglement)
- **A**nalyser l'avancement des projets et maintenance, les tendances 
- **S**uivre des opérations, des chantiers
## Principes généraux
- privilégier autant que possible les collectes automatisées
	- sinon, il faut une sollicitation de la source de l'information (le TdB  invitera les personnes concernées)
- agréger un indicateur selon plusieurs niveaux pour un usage/une vision adaptée à chaque niveau
	- domaine fonctionnel
	- service
	- groupe/domaine de développement
- prévoir le regroupement de plusieurs indicateurs en un autre pour améliorer le côté qualitatif de l'observation (un indicateur n'est pas une fin en soi)
	- ex : couverture de test + nombre d'incidents ▶ qualité 
	- en cas d'un indicateur regroupé, il faut pouvoir avoir accès aux indicateurs primaires
- s'appuyer sur le référentiel Oscar
- préciser l'état de l'indicateur : valeur, sans objet, non défini
- historiser pour connaître l'évolution d'un indicateur

## Les règles
### Granularité des indicateurs
Un indicateur est alimenté au niveau du *module* présent dans le référentiel Oscar. 

Si la source permettant de valoriser un indicateur ne propose que le niveau *application*, alors la valeur de l'indicateur est répercutée sur l'ensemble des modules constitant l'application.

### Fréquence de mise à jour des indicateurs
Pour les premières versions de Compas, les valeurs des indicateurs sont valorisées à un rythme **mensuel**. 

La fréquence pourra être revue à terme.

## Les indicateurs
### Univers _Qualité_
#### Météo des équipes
**Garant** : SNDIO - Abdou Papa Diaw

L'indicateur présente le ressenti des équipes sur une base déclarattive prenant en considération des éléments techniques et organisationnels.

- **Source** : saisie manuelle
- **Agrégation** : 
- **Visualisation** : les états sont présentés sour la forme d'îcone (soleil, nuage, pluie et orage).
- **Stockage** 
	- valeur stockée numérique 
		- 1 soleil ;
		- 2 nuage ;
		- 3 pluie ;
		- 4 orage.
	- commentaire (obligatoire dès lors que l'indicateur n'est pas un soleil (1))
	- date de saisie de l'information
- **Périodicité** : mensuellement, une vérification est réalisée de la *fraicheur* de la dernière information saisie. Si aucune mise à jour n'a été faire au cours du mois précédent, une sollicition est transmise aux personnes identifiées (pour la première version il s'agit du RGA et RIA inscrits dans le référentiel Oscar)
#### Couverture des tests
**Garant** : SNDIP - Philippe Clément

L'indicateur présente le taux de couverture calculé par sonarQube du module considéré. 

- **Source** : sonarQube
- **Agrégation** : les valeurs récupérées sont les métriques des modules. Pour calculer, une valeur agrégée correspond à la sommation des indicateurs unitaires pondérés par le nombre de lignes de code.
- **Visualisation** : la visualisation de l'indicateur est présentée sous la forme d'une lettre (A, B, C D et E). L'échelle est équirépartie entre les cinq lettres (donc par tranche de vingtaine de pourcent) 
- **Stockage**
	- valeur récupérée du taux de couverture du module ;
	- nombre de lignes de code du module - nécessaire à l'agrégation.

Pour retrouver la légende de l'indicateur : [voir la page wiki de l'indicateur](https://gitlab.insee.fr/dsi/compas/documentation/compas-wiki/-/wikis/couverture/home-couvtest)
### Univers _Responsabilité sociale_
#### Accessibilité
**Garant** : Gcoc - Cécile Merlat

L'indicateur présente le résultat des audits d'accessibilité des applications, ayant une IHM, et la *distance* au prochain audit (dans un délai maximal de 3 ans).
Cet indicateur est le plus pertinent, malheureusement seul un petit nombre d'IHM (moins de 20% du parc à ce jour) sont auditées aussi on imagine des sources complémentaires qui permettront d'avoir une idée de l'accessibilité ou plus exactement de repérer des défauts d'accessibilité repérés par des automates.

- **Source** : saisie manuelle
- **Agrégation** : 
- **Visualisation** :
- **Stokage**
    - date de réalisation de l'audit d'accessibilité
	- version du RGAA servant de référence à l'audit
	- score obtenu à l'issue de l'audit
	- type d'audit (total-externe, total-interne, partiel-externe, partiel-interne)
	- ⚠ la distance au prochain audit n'est pas stockée (calculée lors de la mise à jour du tableau de bord)
- **Périodicité** : la saisie des données de l'audit n'a pas de périodicité définie. Le calcul de la *distance* au prochain audit est rafraichie selon la périodicité de mise à jour du tableau de bord.
- **Source complémentaire 1** : sonarQube, issues taggées "accessibility"
	- étude en cours sur la pertinence des règles et la définition d'une métrique synthétique dédiée
- **Source complémentaire 2** : automate DINUM sur base de Tanaguru
	- en attente de réponse de la DINUM pour lancer l'étude, MVP prévu pour la fin du T1 2025


#### Green IT
**Garant** : SNDIN - Patrick Pothier


### Univers _Développement logiciel_
#### Mises en production
**Garant** : SDNIL - Geoffroy Wyckaert

L'indicateur présente la distance (en jour) entre la date de mise à jour et la date de la dernière mise en production du livrable.

- **Source** : 
- **Agrégation** :
- **Visualisation** :
- **Stokage**
	- date de la dernière mise en production
	- numéro de la vesion du livrable
