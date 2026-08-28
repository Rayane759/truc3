# À quoi va ressembler le Golden Path ?

## Fonctionnement général

Dans la pratique, un Golden Path repose souvent sur un mécanisme de
**génération automatisée**.

Exemple de fonctionnement :

1. Le développeur fournit des paramètres (via un formulaire par exemple)
2. Ces paramètres sont donnés au système
3. Le système génère (par exemple) :

    - Un projet
    - Des fichiers de configuration
    - Des artefacts de déploiement (ex : Helm charts)

4. Le développeur peut ensuite déployer directement l'application

Ce modèle permet la reproductibilité, la conformité aux standards et un gain de temps significatif

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

## Fonctionnement global du Golden Path

### Objectif

L'objectif du Golden Path est

### Étapes clés

![alt text](assets/fonct_global.drawio.png)

Le Golden Path est, d'un point de vue global, constitué de 4 étapes clés :

#### 1. **Complétion du formulaire Web**  

Le développeur remplit un formulaire où il renseigne, entre autres :

- Le namespace
- Le port réseau
- Les ressources souhaitées (RAM, CPU)
- Les besoins en BDD (OUI / NON) (Si OUI : détailler)

---------------------------------------------------------------------------------

#### 2. **Envoie des données du formulaire au Backend**  

Le formulaire est alors envoyé au BackEnd au format JSON.

---------------------------------------------------------------------------------

#### 3. **Génération des Charts Helm entièrement configurés**  

Grâce aux données du formulaire, le Backend génère des Charts Helm entièrement configurés.
Plus précisément

---------------------------------------------------------------------------------

#### 4. **Ajout du code applicatif au projet**  

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

## Fonctionnement détaillé du Golden Path
