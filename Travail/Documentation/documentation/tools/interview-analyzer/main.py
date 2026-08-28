import logging
import os
from pathlib import Path
import httpx
from openai import OpenAI
from moviepy import AudioFileClip
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
load_dotenv(".env")
if os.path.exists(".env.local"):
    load_dotenv(".env.local", override=True)

URL = "https://litellm.recette.insee.fr"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

VIDEO_DIRECTORY = "tools/interview-analyzer/resources/data/mp4/"
PROMPT = f"""
    Tu es un UX designer engagé dans le cadre d'une mission consistant à étudier l'opportunité de la mise en place du platform-engineering
    au sein de mon entreprise. Ton but est d'identifer les besoins / les irritants / les insights abordés par la personne interviewée.  
    Tu viens de réaliser des interviews et voici la transcription audio. Rédige moi un compte rendu au format markdown de ce que tu en retiens.
    Je souhaite avoir les parties suivantes: 
    - Contexte & missions quotidiennes
    - Stack technique & outils utilisés
    - Irritants & points de friction
    - Besoins exprimés (ou implicites)
    - Insights clés pour le **Platform‑Engineering**
    Tu pourras rajouter une dernière partie avec d'autres élément mais tu ne feras pas de préconisation / ni de roadmap / ni de choix structurant, reste factuel.
    Tu anonymiseras l'interview.
    """

PROMPT_DOCUMENTATION = f"""
    L’INSEE mène une réflexion globale autour de la refonte et de l’homogénéisation de ses
    différents catalogues de services, aujourd’hui répartis sur une dizaine de plateformes,
    hétérogènes en forme, en sémantique, en profondeur de contenu et en modes d’accès (GitLab, URL
    directes, DPII Planet, etc.).
    Les utilisateurs déclarent peu ou mal utiliser ces catalogues, notamment du fait de leur dispersion,
    de l’absence d’ergonomie homogène, d’une logique documentaire variable selon les équipes, de
    difficultés de navigation, de recherche et d’identification des bons contenus (ModOp, doc
    techniques, équipes responsables, limites de services, etc.).
    Tu es un UX designer engagé dans le cadre de cette mission au sein de mon entreprise. Ton but est d'identifer les besoins / les irritants / les insights abordés par la personne interviewée concernant ce sujet.  
    Tu viens de réaliser des interviews et voici la transcription audio. Rédige moi un compte rendu au format markdown de ce que tu en retiens.
    Je souhaite avoir les parties suivantes: 
    - Synthèse des points positifs et irritants / incohérences (protopersonae)
    ▪ CR des échanges
        Tu pourras rajouter une dernière partie avec d'autres élément mais tu ne feras pas de préconisation / ni de roadmap / ni de choix structurant, reste factuel.
        Tu anonymiseras l'interview.
"""


def convert_mp4_to_mp3(mp4: str):
    logger.info(f"Conversion du fichier {mp4} en mp3")
    path_to_mp3 = mp4.replace("mp4", "mp3").replace("video", "audio")
    if not Path(path_to_mp3).exists():
        logger.info(f"Fichier non existant génération du fichier dans {path_to_mp3}")
        FILETOCONVERT = AudioFileClip(mp4)
        FILETOCONVERT.write_audiofile(path_to_mp3)
        FILETOCONVERT.close()
    else:
        logger.info(f"Skip conversion le fichier {path_to_mp3} existe déjà")
    return path_to_mp3


def generate_openai_client(url, api_key):
    client = OpenAI(
        base_url=url, api_key=api_key, http_client=httpx.Client(verify=False)
    )
    return client


def asr_transcription(oai_client: OpenAI, path_to_audio_file: str):

    if path_to_audio_file is None:
        return " "

    else:
        with open(path_to_audio_file, "rb") as audio_file:
            response = oai_client.audio.transcriptions.create(
                model="whisper-large-v3-turbo",
                file=audio_file,
                response_format="verbose_json",
                timestamp_granularities=["segment"],
            )

        # return complete transcription
        return response.text


def analyze_transcription(
    oai_client: OpenAI, transcription: str, prompt: str, model=""
) -> str:
    """Envoie la transcription + un prompt à un LLM et retourne la réponse."""
    response = oai_client.chat.completions.create(
        model=model,  # adaptez selon les modèles dispo sur votre LiteLLM
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\nTranscription :\n{transcription}",
            },
        ],
        temperature=0,
    )
    return response.choices[0].message.content


def export_transcription(transcription: str, path):
    with open(path, "w", encoding="utf-8") as text_file:
        text_file.write(transcription)


def export_analysis(analysis: str, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as text_file:
        text_file.write(analysis)


def make_transcription(oai_client: OpenAI, path_to_audio_file: str) -> str:
    logger.info(f"Transcription du fichier {path_to_audio_file} en texte")
    path_to_transcription = path_to_audio_file.replace(".mp3", ".txt").replace(
        "mp3", "transcription"
    )
    if not Path(path_to_transcription).exists():
        logger.info(
            f"Fichier non existant génération du fichier dans {path_to_transcription}"
        )
        transcription = asr_transcription(
            oai_client=oai_client, path_to_audio_file=path_to_audio_file
        )
        export_transcription(path=path_to_transcription, transcription=transcription)
    else:
        logger.info(
            f"Skip transcription le fichier {path_to_transcription} existe déjà"
        )

    return path_to_transcription


def make_analysis(
    oai_client: OpenAI,
    path_to_transcription: str,
    prompt: str,
    export_analysis_in_folder: str = "",
    model: str = "",
) -> str:
    logger.info(f"Analyse du fichier {path_to_transcription}")
    path_to_analysis = path_to_transcription.replace(
        "transcription",
        (
            "analysis"
            if export_analysis_in_folder == ""
            else f"analysis/{export_analysis_in_folder}"
        ),
    ).replace("txt", "md")
    if not Path(path_to_analysis).exists():
        logger.info(
            f"Export de l'analyse du fichier {path_to_transcription} vers {path_to_analysis}"
        )
        transcription = ""
        with open(path_to_transcription) as f:
            transcription = f.read()
        analysis = analyze_transcription(
            oai_client=oai_client,
            transcription=transcription,
            prompt=prompt,
            model=model,
        )
        export_analysis(
            path=path_to_analysis,
            analysis=analysis,
        )
    else:
        logger.info(f"Skip analyse car le fichier {path_to_analysis} existe déjà")
    return path_to_analysis


def process(path_to_video_file: str):
    video_file_path = path_to_video_file
    audio_file_path = convert_mp4_to_mp3(mp4=video_file_path)
    client = generate_openai_client(url=URL, api_key=ACCESS_TOKEN)
    path_to_transcription = make_transcription(
        oai_client=client, path_to_audio_file=audio_file_path
    )
    make_analysis(
        oai_client=client,
        path_to_transcription=path_to_transcription,
        prompt=PROMPT,
        model="gpt-oss-120b",
        export_analysis_in_folder="",
    )


if __name__ == "__main__":
    files = os.listdir(VIDEO_DIRECTORY)
    for _file in files:
        process(path_to_video_file=f"{VIDEO_DIRECTORY}{_file}")
