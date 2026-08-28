import pandas as pd
import numpy as np
from jinja2 import Environment, FileSystemLoader


def determine_choice(reponse: str):
    try:
        options = reponse.split(",")
        for option in options:
            choice = option.split(":")
            if choice[1] == "1":
                return choice[0]
    except:
        return "unknown"


## PréTraitement
df = pd.read_csv(filepath_or_buffer="./documents/devexp_2026-01-26.csv", sep=";")
df = df.drop(columns=["Prénom", "Nom", "E-mail"])
for i in range(0, 13):
    cols = df.columns.tolist()
    if i == 0:
        df = df.drop(columns=["Q1: Réponse"])
    if i >= 1:
        idx = cols.index(f"Q{i+1}: Type")
        df.insert(
            idx,
            f"Q{i+1}: Question",
            df[[f"Q{i+1}: Label", f"Q{i+1}: Description"]]
            .fillna("")
            .astype(str)
            .agg(" ".join, axis=1)
            .str.strip(),
        )
    df = df.drop(columns=[f"Q{i+1}: Type", f"Q{i+1}: Label", f"Q{i+1}: Description"])

df["Q2: Réponse"] = df["Q2: Réponse"].apply(determine_choice)
df["Q13: Réponse"] = df["Q13: Réponse"].apply(determine_choice)
df = df.replace(["-", "--", "", " ", "N/A", "na", "null", "unknown"], np.nan)
df = df.replace(r"\|", "", regex=True)
df = df.fillna("Non renseigné")
df.to_csv("./documents/devexp_2026-01-26_treated.csv", index=False)


# --- Métadonnées ---
context = {
    "taille": len(df),
    "description_colonnes": "\n".join(
        [
            "- `Q2: Question` : description de la question Q2",
            "- `Q2: Réponse` : réponse à la question Q2 (note/5)",
            "- `Q2: Commentaire`: commentaire additionnel de la question Q2",
            "- `Q3: Question` : description de la question Q3",
            "- `Q3: Réponse` : réponse à la question Q3 (note/5)",
            "- `Q3: Commentaire`: commentaire additionnel de la question Q3",
            "- `Q4: Question` : description de la question Q4",
            "- `Q4: Réponse` : réponse à la question Q4 (note/5)",
            "- `Q4: Commentaire`: commentaire additionnel de la question Q4",
            "- `Q5: Question` : description de la question Q5",
            "- `Q5: Réponse` : réponse à la question Q5 (note/5)",
            "- `Q5: Commentaire`: commentaire additionnel de la question Q5",
            "- `Q6: Question` : description de la question Q6",
            "- `Q6: Réponse` : réponse à la question Q6 (note/5)",
            "- `Q6: Commentaire`: commentaire additionnel de la question Q6",
            "- `Q7: Question` : description de la question Q7",
            "- `Q7: Réponse` : réponse à la question Q7 (note/5)",
            "- `Q7: Commentaire`: commentaire additionnel de la question Q7",
            "- `Q8: Question` : description de la question Q8",
            "- `Q8: Réponse` : réponse à la question Q8 (note/5)",
            "- `Q8: Commentaire`: commentaire additionnel de la question Q8",
            "- `Q9: Question` : description de la question Q9",
            "- `Q9: Réponse` : réponse à la question Q9 (note/5)",
            "- `Q9: Commentaire`: commentaire additionnel de la question Q9",
            "- `Q10: Question` : description de la question Q10",
            "- `Q10: Réponse` : réponse à la question Q10 (note/5)",
            "- `Q10: Commentaire`: commentaire additionnel de la question Q10",
            "- `Q11: Question` : description de la question Q11",
            "- `Q11: Réponse` : réponse à la question Q11 (note/5)",
            "- `Q11: Commentaire`: commentaire additionnel de la question Q11",
            "- `Q12: Question` : description de la question Q12",
            "- `Q12: Réponse` : réponse à la question Q12 (note/5)",
            "- `Q12: Commentaire`: commentaire additionnel de la question Q12",
            "- `Q13: Question` : description de la question Q13",
            "- `Q13: Réponse` : réponse à la question Q13 (note/5)",
            "- `Q13: Commentaire`: commentaire additionnel de la question Q13",
        ]
    ),
    "fichier_joint": "devexp_2026-01-26_treated.csv",
}

# --- Charger le template Jinja ---
env = Environment(
    loader=FileSystemLoader("./tools/devexp/resources/"),
    autoescape=False,  # IMPORTANT pour Markdown
)

template = env.get_template("template.md.j2")

# --- Rendu final ---
prompt_md = template.render(**context)

# --- Écriture du fichier ---
with open("./documents/prompt_final.md", "w", encoding="utf-8") as f:
    f.write(prompt_md)
