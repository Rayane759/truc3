# Analyseur des interviews développeurs dans le cadre du platform engineering

## Protocole

Le traitement a été réalisé avec l'aide de l'IA proposé par l'outil again-lab.recette.insee.fr

Les modèles suivants ont été utilisés :
- whisper-large-v3-turbo pour le traitement du speech_to_text
- gpt-oss-120b pour l'analyse de la transcription

Le prompt :

> Tu es un UX designer engagé dans le cadre d'une mission consistant à étudier l'opportunité de la mise en place du platform-engineering au sein de mon entreprise. Ton but est d'identifer les besoins / les irritants / les insights abordés par la personne interviewée.  Tu viens de réaliser des interviews et voici la transcription audio. Rédige moi un compte rendu au format markdown de ce que tu en retiens.

## Utilisation

- Installer les dépendances : `uv sync`
- Créer un fichier `.env.local` avec la clé `ACCESS_TOKEN="YourS€cretK€Y"`
- Placer vos fichiers mp4 dnas le dossier `resources/data/mp4/`
- Lancer le fichier main.py
- Enjoy !

## Résultat 

Les résultats sont disponibles [ici](./resources/data/analysis/)