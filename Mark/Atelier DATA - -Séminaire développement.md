# Atelier DATA - -Séminaire développement

## Préalable
- Objectifs
    - Se monter une infra data en local pour développer
    - Les fonctionnalités autours de postgres/duckdb
    - Les datalakehouses avec ducklake

- Récupérer le projet exemple
    - https://gitlab.insee.fr/fy2qeq/atelier_data
    - vous pouvez le récupérer au format zip : le projet java est simplement là pour démonstration et vous n'en aurez pas besoin durant l'atelier

- Installation de podman pour déployer en local les containers de notre infra data
    - https://codimd.dev.kube.insee.fr/s/2hkYFEpaF#

---

## Premiers cas d'utilisation de postgres et duckdb

![](https://codimd.dev.kube.insee.fr/uploads/upload_e5f261c1eec1278b3e8504f681f31469.png)


---

### Postgres
- Postgres : base de données relationel
    - optimiseur : calcul parcimonieux, OLTP
    - progression vers OLAP au fil des versions en proposant du parallélisme (lecture asynchrone, parallélisme de traitement) mais cela reste une base de données ligne
- Dossier data local de persistence
- Scalabilité verticale
- Socket de connection multi-connections
    - il est possible d'ouvrir plusieurs connections simultanément
    - chaque connection instancie au moins un thread de traitement qui lui est propre

---

### DuckDB
- DuckDB est un moteur de traitement léger de données orienté colonne
    - calculs priorisés en mémoire avec la possibilité de monter localement un dossier data de persistence, OLAP
- Scalabilité verticale
- Serverless
    - pas d'interface exposée, il vient se greffer sur un autre composant exposant un point d'accés comme java, python, cli, rust, ...
- Mono connexion
    - une instance duckdb = une seule connexion = 1 thread

- DuckDB est aussi un formidable ETL : multi-format, multi-support, compression, chiffrement, syntaxe homogène et normalisé > datalake
- Cela s'appuie sur de nombreuses extensions optionnelles
    - En fonctionnement normal, les extensions sont téléchargées et s'installées au runtime

---

### Atelier 1 : Monter localement une infrastructure data

- On va utiliser podman / docker-compose

- Aller dans le répertoire docker du projet atelier_data

- Lancer un terminal à cet endroit

- Créer / lancer la machine virtuelle podman
    ```bash=
    podman machine init
    podman machine start
    ```

- Regardons ensemble le fichier infra-data.yaml

- Lancer le yml de configuration situé dans le répertoire avec podman
    ```bash=
    podman compose --file infra-data.yaml up --detach
    ```

- Vérifier que les bases fonctionnent bien
    ```bash=
    podman stats
    podman logs 
    ```

- On peut se connecter avec dbeaver sur les bases pg1 et pg2

---

### Atelier 1 : Charger des données dans postgres grace à duckdb

- > Dans DBeaver, lancer une instance jdbc de duckdb

- > Avec DuckDB, charger les données par commune de la population dans la base de données pg1
    - Créer un schéma popref

    - Créer la table popref.popref2022 contenant la population de référence 2022 : https://www.insee.fr/fr/statistiques/8290591?sommaire=8290669

    - Créer la table popref.popref2023 contenant la population de référence 2023 : https://www.insee.fr/fr/statistiques/8680726?sommaire=8681011

---

```sql=

-- proxy pour aller piocher nos extensions et nos données sur internet
set http_proxy='proxy-rie.http.insee.fr:8080';

-- charger l'extension postgres
-- a noter que cela charge aussi l'extension httpfs !
-- car duckdb a besoin de httpfs pour charger les extensions
INSTALL postgres;
LOAD postgres;

-- inscrire la chaine de connexion vers la base de données postgres pg1 dans le catalogue duckdb
create or replace secret pg1
(
TYPE postgres,
HOST '127.0.0.1',
PORT 65001,
DATABASE pg1,
USER 'user',
PASSWORD 'password'
);

-- attacher les bases postgres au catalogue duckdb
ATTACH '' AS pg1 (TYPE postgres, SECRET pg1);

create schema pg1.popref;

-- charger l'extension zip
INSTALL zipfs FROM community;
LOAD zipfs;

select * from glob('zip://https://www.insee.fr/fr/statistiques/fichier/8290591/ensemble.zip')
;

create table pg1.popref.popref2022
as select * from read_csv('zip://https://www.insee.fr/fr/statistiques/fichier/8290591/ensemble.zip/donnees_communes.csv')
;

SELECT * FROM glob('zip://https://www.insee.fr/fr/statistiques/fichier/8680726/ensemble.zip');

-- duckdb sait inférer lles readers comme reader_csv, reader_parquet, ... en s'appuyant sur l'extension du fichier
create table pg1.popref.popref2023 as
select * from 'zip://https://www.insee.fr/fr/statistiques/fichier/8680726/ensemble.zip/donnees_communes.csv'
;

```

---

### Minio
- Expose un stockage "objet" s3
- Socket https
- Notion de bucket
    - La structure de base de S3 est le bucket : il s'agit d'un conteneur où les objets sont stockés
    - Un s3 peut exposer plusieurs buckets indépendant avec chacun leur propre politique d'accès
    - ~ analogue a la racine d'un répertoire dans un système de fichier
- Le dialogue avec le s3 s'appuie sur une API REST et ses ordres CRUD
    - POST : on poste un fichier
    - DELETE : on efface un fichier
    - GET : lire un fichier
- On va voir dans le prochain atelier que Duckdb fait cela très bien grace à l'extension httpfs
&nbsp;
- > Revoir ensemble le fichier infra-data.yaml sur la partie minio

---

## Atelier 2 : Exporter en parquet et en parquet chiffré

- > Exporter en parquet popref2022 sur votre système de fichier local
    - A noter : il n'est pas nécessaire d'avoir un stockage s3 pour créer des fichiers parquet

- > Archiver les données de popref2022 dans le s3
    - Sauvegarder les données popref2022 en parquet sur le s3 dans le bucket tp1
    - Supprimer la table popref2022

- > Utilisation de l'archive parquet et chiffrement
    - Réutiliser le fichier parquet 2022 pour créer un parquet chiffré contenant les données de 2022 et de 2023

---

## Atelier 2 : SQL

```sql=

-- déjà on a pas besoin de s3 pour exporter en parquet
COPY (select '2022' as millesime, * from pg1.popref.popref2022)
TO 'C:/atelier_data/popref2022.parquet';


-- pour exporter sur un point de stockage objet
-- on a besoin de l'extension httpfs
-- elle se télécharge toute seule si on a accès à internet

-- déclarer les informations du s3 dans le catalogue
CREATE OR REPLACE SECRET s3 (
    TYPE s3,
    PROVIDER config,
    KEY_ID 'ACCESS_KEY_DL',
    SECRET 'ACCESS_SECRET_DL',
    REGION 'us-east-1',
    ENDPOINT 'localhost:9000',
    USE_SSL 'false',
    URL_STYLE 'path'
);


-- Archiver popref2022 et dropper la table
-- ecriture du parquet dans notre bucket tp1 sur s3
COPY (select '2022' as millesime, * from pg1.popref.popref2022)
TO 's3://tp1/popref2022.parquet';

DROP TABLE pg1.popref.popref2022;


-- Archiver toutes les popref dans un parquet chiffré
PRAGMA add_parquet_key('key256', '01234567891123450123456789112345')

COPY
    (
	select * from read_parquet('s3://tp1/popref2022.parquet')
	union all by name
	select '2023' as millesime, * from pg2.popref.popref2023
)
    TO 's3://tp1/popref_encrypted.parquet'
    (ENCRYPTION_CONFIG {footer_key :'key256'});
    
```

---

## Atelier 2 : des remarques sur le cas d'utilisation ?
- Super ETL
    - Beaucoup de readers très configurables : csv, parquet, excel, json, ...
    - Mutiple point d'acces
        - dans l'atelier suivant, on va inscrire une nouvelle base postgres pg2 dans duckdb pour stocker des établissements
        - il sera possible de croisier les donénes entre bases, s3, ...
- Pas de possibilité de modifier le parquet sauf le recharger, le modifier et l'exporter à nouveau
- Pas d'alias d'accès au fichier parquet (on utilise des noms de fichiers qu'il faut connaitre voir stocker...)

---

## Atelier 3 : Duckdb, niveau performance OLAP, ca donne quoi ?

- > Calcul anaytique sur un gros fichier établissement
    - Sur la base pg2, on va récupérer les colonnes siret, codeCommuneEtablissement, etatAdministratifEtablissement du fichier des établissements sirene
        - https://www.data.gouv.fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret
        - Utilisez le parquet à disposition plutot que le csv, ca sera bien plus rapide : les données d'un fichier parquet sont rangées par colonne
    - Compter le nombre d'établissement et le nombre d'établissement actif par commune; selectionner les 20 premieres commune avec le plus d'établissements actifs


---

## Atelier 3 : SQL

```sql=
-- ajouter la base postgres pg2 au catalogue
create or replace secret pg2
(
TYPE postgres,
HOST '127.0.0.1',
PORT 65002,
DATABASE pg2,
USER 'user',
PASSWORD 'password'
);

ATTACH '' AS pg2 (TYPE postgres, SECRET pg2);


-- création du schéma et de la table dans postgres contenant le parquet des etablissements
-- sur les colonnes demandée
create schema pg2.sirene;
drop table if exists pg2.sirene.etablissement;
create table pg2.sirene.etablissement as
select siret, codeCommuneEtablissement as depcom,  etatAdministratifEtablissement as etat 
from read_parquet('https://object.files.data.gouv.fr/data-pipeline-open/siren/stock/StockEtablissement_utf8.parquet');

-- essayons d'attaquer la base postgres pour faire un comptage analytique
-- duckdb récupere les données de pg puis fait le calcul
-- durée = temps de récupération et de transformation ligne -> colonne
select depcom, count(case when etat='A' then true else null end) as nb_actif, count(*) as nb
from pg2.sirene.etablissement
where depcom is not null
group by depcom
order by nb_actif desc, nb desc
limit 20
;

-- si on met la table dans duckdb au préalable ?
-- ca vaut le coup de le faire si on utilise cette table souvent
create temporary table etablissement as select siret, depcom, etat from pg2.sirene.etablissement;

select depcom, count(case when etat='A' then true else null end) as nb_actif, count(*) as nb
from etablissement
where depcom is not null
group by depcom
order by nb_actif desc, nb desc
limit 20
;

-- essayons la meme requete dans notre postgres un peu optimisé

```

---

## Duckdb pour nos développements en java/python ?
- Intégrer duckdb en java / python est très facile
    ```pom=
            <dependency>
                <groupId>org.duckdb</groupId>
                <artifactId>duckdb_jdbc</artifactId>
                <version>${project.duckdb.version}</version>
            </dependency>
    ```


---

## Les foncitons d'ETL appuient beaucoup sur les extensions
- Le système d'extension de duckdb télécharge les binaires au runtime et ceci grace à l'extension httpfs qui est elle-même téléchargée au runtime... :exploding_head::exploding_head:
    -Pas vraiment compatible en environnement fermé comme nos productions

- Solution
1. Packager à minima l'extension httpfs nécessaire aux téléchargements des autres extensions
    - pour les applications sur kub, via docker comme dans RESIL (Stéphane Roger) 
        - https://gitlab.insee.fr/Individus-et-logements/resil/resil-back/-/blob/feat/recuperation_ti_chiffres/dockerfiles/batch/Dockerfile?ref_type=heads
    - via maven comme je fais dans ARC et présenté dans mon projet exemple
        - https://gitlab.insee.fr/fy2qeq/atelier_data
    - A noter que l'image docker de duckdb du ssp cloud contient httpfs (Romain Avouac)

2. Une fois l'extension httpfs intégré, on peut utiliser alors le proxy-cache sur le nexus pour que duckdb installe les autres extensions au runtime
    - en indiquant à duckdb l'adresse du repository sur nexus
        - https://gitlab.insee.fr/Individus-et-logements/resil/univers-de-reference/production/livrables/-/blob/main/src/config.py?ref_type=heads#L31-40

---

### Le projet java exemple
- https://gitlab.insee.fr/fy2qeq/atelier_data

    - ce programme insere des enregistrements dans la base pg1 et va les lire avec duckdb

- fonctionne avec spring docker compose

    - faire un lien symbolique de podman vers docker (ou installer docker) pour que spring docker compose fonctionne (pas de support podman pour l'instant)
    ```shell=
    cd C:\Program Files\RedHat\Podman
    mklink /H docker.exe podman.exe
    ```

    - au lancement de springboot, springboot va, si nécessaire, monter tous les containers déclarés infra-data.yaml comme si on lancait en line de commande podman docker-compose dessus
- les extensions duckdb sont packagés dans un fichier extension.zip au build et au moment d'utiliser duckdb, on les decompresse dans un dépot et on indique a duckdb d'utiliser ce dépot
    - voir le pom.xml pour ajouter simplement des extensions duckdb

---

## Alors duckdb ou postgres ?
- OLTP vs OLAP

![](https://codimd.dev.kube.insee.fr/uploads/upload_eef06b4c631168a186f6a61dd36b37a5.png)



---

## Atelier 4: pg_duckdb : le meilleur des 2 mondes !
- porté par Motherduck : https://github.com/duckdb/pg_duckdb
- C'est une base postgres avec un moteur duckdb
    - s'appuie encore sur le fait que duckdb est serverless
    - mais aussi sur la similarité des apis sql postgres/duckdb
- Embarque nativement les principales extensions :+1: : https, s3
- Opérateur kubernetes cnpg :heart_eyes:
    - On a donc un postgres qui sait communiquer ave un s3, ecrire, lire du parquet, ...
    - On peut demander explicitement au moteur duckdb d'intervenir sur les calculs analytiques
- Attention, c'est un projet jeune : la v1 date de fin 2025

- > Dans DBeaver, se connecter à la base postgres pg_duckdb
    - lire les fichiers parquets et parquets chiffré qu'on a stocké dans le s3
    - essayer des requetes analytiques et explorer leur explain plan

---

## Atelier 4: SQL

```sql=

-- inscrire le s3 au catalog
-- Attention utiliser host.containers.internal plutot que localhost 
-- (contrainte podman/docker pour qu'un container puisse accéder à un autre container localement)
SELECT duckdb.create_simple_secret(
    type := 's3', provider := 'config', key_id := 'ACCESS_KEY_DL', secret := 'ACCESS_SECRET_DL', region := 'us-east-1', endpoint := 'host.containers.internal:9000', use_ssl := 'false', url_style:='path'
);

-- c'est du postgres avec en dessous le moteur duckdb
-- on doit spécifier la conversion du modèle colonne en ligne si on attaque une seule colonne;
-- select * le fait automatiquement
select distinct r['millesime'] from read_parquet('s3://tp1/popref.parquet') r

-- un peu moins direct pour lire le parquet chiffré a cause du type struct mais ca reste simple
SELECT duckdb.raw_query($$ PRAGMA add_parquet_key('key256', '01234567891123450123456789112345') $$) r;
select * from duckdb.query($$ SELECT * FROM read_parquet('s3://tp1/popref_encrypted.parquet', encryption_config = {footer_key: 'key256'}) $$) r

-- calcul analytique sur notre table etablissement
-- proxy !
select duckdb.raw_query($$ set http_proxy='proxy-rie.http.insee.fr:8080'; $$)

-- creation d'une table temporarire etablissement au format colonne
-- c'est beaucoup plus rapide de faire comme cela que de remplir la table au format ligne directement
-- utiliser le mot clé using duckdb siginifie au moteur qu'on souhaite du stockage colonne
-- techniquement il est seulement possible de créer des tables temporaires au format colonne
create temporary table etablissement using duckdb as
select r['siret'] as siret, r['codeCommuneEtablissement'] as depcom,  r['etatAdministratifEtablissement'] as etat  
from read_parquet('https://object.files.data.gouv.fr/data-pipeline-open/siren/stock/StockEtablissement_utf8.parquet') r;

-- conversion au format ligne et stockage dans le schéma sirene de la base postgres
create schema sirene;
create table sirene.etablissement as select * from etablissement;
analyze sirene.etablissement;

-- on demande que cela soit du calcul postgres
-- executer 2 fois pour hit la shared mem
set duckdb.force_execution=false;

explain (verbose)
select depcom, count(case when etat='A' then true else null end) as nb_actif, count(*) as nb
from sirene.etablissement
where depcom is not null
group by depcom
order by nb_actif desc, nb desc
limit 20
;

-- on passe en mode duckdb
set duckdb.force_execution=false;
explain (verbose)
select depcom, count(case when etat='A' then true else null end) as nb_actif, count(*) as nb
from sirene.etablissement
where depcom is not null
group by depcom
order by nb_actif desc, nb desc
offset 200 limit 20
;

-- avec notre table temporaire en mode colonne
-- ca vaut le coup de convertir en table temporaire colonne avec using duckdb si on réutilise beaucoup cette table lors des calculs
explain (verbose)
select * from duckdb.query($$  select depcom, count(case when etat='A' then true else null end) as nb_actif, count(*) as nb
from pg_temp.etablissement
where depcom is not null
group by depcom
order by nb_actif desc, nb desc
offset 200 limit 20
; $$);


```

---

## OLAP, OLTP et datalakehouse
![](https://codimd.dev.kube.insee.fr/uploads/upload_bb082e06ac7bd3f68ffadf006f3f23ad.png)

---

## Les datalakehouses
- Combinaison de
    - (datawarehouse) données structurées exploitables pour réaliser des calculs analytiques
    - (datalake) stockage a faible cout
- Fonctionnnalités
    - transactionnel ACID

- Peut s'appuyer sur
    - des base de données orientée calcul analytique
    **OU ENCORE**
    - des moteurs de traitements s'appuyant sur des formats de données orientés datalake

---

### Les formats de données orientés datalake utilisent en général :
- Fichier parquets dans des s3 contenant des données et parfois des méta-data (fichier manifest)
    - par opposition aux stockage propriétaires locaux des bases de données
- Un catalogue
    - Assure la correspondance entre alias noms de tables SQL <-> les pointeurs vers les fichiers parquets
    - Prise en charge des opérations atomiques : garantir un état de table cohérent lors des lectures/écritures simultanées.
    - Stockage et gestion des métadonnées, assure leur accès et leur cohérence
- Fonctionnalités usuelles
    - voyage dans le temps (snapshots)
    - transactionnel
    - optimisation cachée : partitionnement, compression et filtrage des données, inlining
- Iceberg, Deltalake, **Ducklake**
    - https://ducklake.select/manifesto/

---

### Iceberg

- Le premier architecte – appelons-le le Rêveur Distribué – imagine un système en couches où les informations de chaque livre sont stockées sur des fiches, elles-mêmes regroupées dans des chemises cartonnées, référencées par des listes principales, et suivies dans un registre central. Toute modification nécessite la mise à jour simultanée de plusieurs fiches, chemises et listes. C’est Apache Iceberg

    - Scalable horizontalement à tous les niveaux
    - Complexe à mettre en oeuvre (stack assez lourde) et à maintenir (foret de fichiers, orphan, ...)
        - le catalogue sert peu, seulement à aliaser les méta data : le fonctionnement s'appuie sur beaucoup sur le s3

---

### Ducklake
- Le second architecte, le pragmatique spécialiste SQL, dit simplement : « Utilisons une base de données. » Une table pour les livres, une pour les transactions, et voilà. Imaginez une feuille de calcul où toutes les métadonnées sont centralisées. C’est DuckLake
  - https://motherduck.com/blog/ducklake-motherduck/

    - Scalable verticalement au niveau du catalogue mais pas horizontalement
    - Supporté par motherduck mais **pas encore de version de production**
    - Simple à mettre en oeuvre et à maintenir : on va le faire dans cet atelier
    - fonctionnalité supplémentaire
        - chiffrement
        - inlining

---

### Atelier 5: Utiliser le format ducklake...

![](https://codimd.dev.kube.insee.fr/uploads/upload_90bef70aef93e9ffecb12f768759bb82.png)

- > Créer un datalakehouse ducklake chiffré en utilisant
    - le bucket s3 appelé ducklake où seront stockés les parquet ducklake
    - la base postgres pg_ducklake_catalog comme catalogue
    - une instance duckdb dans dbeaver pour passer les instructions sql

- > Explorer les fonctionnalités inline, time travel, valider le chiffrement

---

### Atelier 5: Dans une instance de duckbd

```sql=

-- proxy pour aller piocher nos extensions et nos données sur internet
set http_proxy='proxy-rie.http.insee.fr:8080';

-- charger les extensions postgres et ducklake
INSTALL postgres;
LOAD postgres;
INSTALL ducklake;


-- déclarer le s3 dans le catalogue
CREATE OR REPLACE SECRET s3 (
    TYPE s3,
    PROVIDER config,
    KEY_ID 'ACCESS_KEY_DL',
    SECRET 'ACCESS_SECRET_DL',
    REGION 'us-east-1',
    ENDPOINT 'localhost:9000',
    USE_SSL 'false',
    URL_STYLE 'path'
);


-- déclarer la base postgres utilisé comme catalogue de ducklake

create secret pg_ducklake_catalog_info (
    type postgres,
    host '127.0.0.1',
    port 65004,
    database 'pg_ducklake_catalog',
    user 'user',
    password 'password'
);

-- déclarer le bucket s3 utilisé par ducklake
-- et le schéma de la base de catalogue utilisé pour stocker les méta données
create or replace secret ducklake_info (
    type ducklake,
    metadata_path '',
    metadata_schema 'ducklake', 
    data_path 's3://ducklake/',
    ENCRYPTED true,
    metadata_parameters map {'TYPE': 'postgres', 'SECRET': 'pg_ducklake_catalog_info'}
);

-- déclarer dans le catralogie l'utilisation de ducklake avec les informations fournies ci-dessus
-- toutes les tables prefixées par lake. iront dans le datalakehouse ducklake
attach 'ducklake:ducklake_info' as lake (AUTOMATIC_MIGRATION, OVERRIDE_DATA_PATH);

-- vérifier la création de la table xxx
CREATE TABLE lake.xxx as select i from generate_series(1,1000000) as t(i);

-- cette petite table a été inline c'est a dire stockée intégralement dans le catalogue
-- pas d'interet en parquet vec un delai vers le s3 pour les petites tables
CREATE TABLE lake.yyy as select i from generate_series(1,10) as t(i);

-- l'inline est configurable
SET ducklake_default_data_inlining_row_limit = 0;

-- update du parquet relatif à la table lake.xxx
-- on met à jour les 1000 premières ligne avec la valeur 0
update lake.xxx set i=0 where i<1000;

-- voyage dans le temps
-- voir les snapshots
SELECT * FROM lake.snapshots();

-- requete sur les versions ou les timestamp (demande de la version de la table à un moment t)
SELECT count(*) FROM lake.xxx AT (VERSION => 1) where i=0;
SELECT count(*) FROM lake.xxx AT (VERSION => 2) where i=0;
SELECT count(*) FROM lake.xxx AT (TIMESTAMP => timestamptz '2026-05-16 21:31:16') where i=0;

-- vérification du chiffrement
select * from parquet_metadata('s3://ducklake/main/xxx/*')

```

---

### Atelier 5: En se connectant en jdbc à la supere base postgres pg_ducklake
![](https://codimd.dev.kube.insee.fr/uploads/upload_e47177192f61d611eb5349a7303e984b.png)

- pg_ducklake = base postgres avec duckdb et support ducklake
    - OLAP / OLTP et format datalakehouse :heart_eyes:
    - S'appuie sur pg_duckdb et on dispose donc de ses fonctionnalités et extensions pré-installée

- Pas de base catalogue distante : la base pg_ducklake contient le catalogue du datalakehouse dans son schéma appelé "ducklake"

- La base contient le schéma duckdb qui expose les fonctions duckdb

- Pour l'instant le chiffrement n'est pas implémenté mais présent dans la roadmap
    - https://github.com/relytcloud/pg_ducklake/blob/main/docs/ducklake_feature_coverage.md

---

### Atelier 5: cela devient encore plus simple

- > Configurer et utiliser pg_ducklake pour configurer et utiliser le datalakehouse
    - Se connecter dans dbeaver à la base postgres pg_ducklake et allons-y !
    - Créer des tables 
        - sans utiliser la clause using met les tables dans postgres en stockage ligne
        - avec la clause **using ducklake** indique à postgres qu'on veut utiliser le datalakehouse ducklake
        - avec la clause **using duckdb** informe à postgres qu'on veut stocker les données au format colonne duckdb optimisé pour les calculs OLAP


```sql=
SELECT duckdb.create_simple_secret(
    type := 's3', provider := 'config', key_id := 'ACCESS_KEY_DL', secret := 'ACCESS_SECRET_DL', region := 'us-east-1', endpoint := 'host.containers.internal:9000', use_ssl := 'false', url_style:='path'
);


SET ducklake.default_table_path = 's3://pgducklake/';

-- on crée un schéma au lieu de mettre dans public :)
CREATE SCHEMA app;

-- le mot clé using indique a postgres qu'on veut une table non pas stockée dans la base mais dans le datalakehouse
-- vérifier la création de la table xxx
CREATE TABLE app.xxx using ducklake as select i from generate_series(1,1000000) t(i);

```

---

### Effacer ou arreter votre infra data

- Aller dans le répertoire docker du projet atelier_data

- Lancer un terminal à cet endroit

- Pour arreter les services montés par podman
    ```bash=
    podman stop --all
    ```

- Pour effacer les services et déploiements
    ```bash=
    podman compose --file infra-data.yaml down
    ```

- Pour effacer complétement y.c les images dockers téléchargées et libérer l'espace
    ```bash=
    podman system prune --all --force && podman rmi --all --force
    ```

---

### Conclusion
- infra en local avec podman. C'est bien ?

- pg_duckdb ou pg_ducklake = super postgres dopé avec duckdb et éventuellement un support datalakehouse (format ducklake)

- Ce qu'apportent ces solutions
    - Nos bases postgres pourraient très simplement charger, décharger, chiffrer des données sensibles, utiliser/générer des parquet, csv, etc., s'interconnecter sans composant annexe
    - Gain de performance sur les calculs OLAP
    - les fonctionnalités datalakouse vraiment pratique et performante (voyage dans le temps, optimisation des partition, …) 
        - iceberg dans resil et ddc
    - l'existence d'un opérateur cnpg est vraiment un atout > PDD ?
    - la migration vers ces bases postgres améliorées semble théoriquement simple

- Surveiller le niveau de maturité pour opportunité
    - chiffrement, mono-connexion dukdb dans postgres, interconnexions


---

### FIN

- N'hésitez-pas : manuel.soulier@insee.fr

---

<style>

.reveal body, body
    {
        background-color:#eeeeee !important;
        --r-heading-color : #000000;
        --r-main-color : #000000;
        color: #000000;
    }

.reveal ul, .reveal li
{
    font-size:1.9rem  !important;color: #000000;
}
    
.reveal h1 {font-size:1em !important;color: #000000;}

.reveal h2 {font-size:0.9em !important;color: #000000;}
    
.reveal h3 {font-size:0.8em !important;color: #000000;}

.reveal h4 {font-size:0.7em !important;color: #000000;}
    
.reveal table {color: #000000;font-size:0.4em}    

p {color: #000000;}
    
blockquote, .reveal blockquote { background-color:#3333aa; width:auto; margin: 5px auto; padding: 0; margin-top: 20px;}

blockquote > p , .reveal blockquote >p {color: #ffffff; margin:5px; }
    
.code {font-size:1.6rem;}
    
summary {display:revert;}
    
.reveal pre {
  width: 63em;
  left: -11em;
  line-height: unset;
    }

.reveal pre code {
  max-height: 600px;
}
    
</style>