"""
Golden Path — Générateur multi-cible
Entrée  : JSON (stdin ou fichier)
Sortie  : répertoire généré (chemin affiché sur stdout)

Cibles supportées : kubernetes | vm | cloud
"""

import json
import sys
import tempfile
from pathlib import Path

from targets.kubernetes import generate_kubernetes
from targets.vm        import generate_vm
from targets.cloud     import generate_cloud

# ---------------------------------------------------------------------------
# Validation commune
# ---------------------------------------------------------------------------

REQUIRED_FIELDS = ["appName", "teamName", "target"]
VALID_TARGETS   = ["kubernetes", "vm", "cloud"]
VALID_PROVIDERS = ["aws", "gcp", "azure"]


def validate(v: dict) -> None:
    for f in REQUIRED_FIELDS:
        if not v.get(f):
            raise ValueError(f"Champ obligatoire manquant : '{f}'")

    if v["target"] not in VALID_TARGETS:
        raise ValueError(f"'target' doit être parmi {VALID_TARGETS}")

    if v["target"] == "cloud":
        provider = v.get("cloudProvider", "")
        if provider not in VALID_PROVIDERS:
            raise ValueError(
                f"'cloudProvider' doit être parmi {VALID_PROVIDERS} "
                f"quand target=cloud (reçu : '{provider}')"
            )


# ---------------------------------------------------------------------------
# Valeurs par défaut communes
# ---------------------------------------------------------------------------

def apply_common_defaults(v: dict) -> dict:
    v = v.copy()
    v.setdefault("environnement", "dv")
    v.setdefault("appDescription", f"Application {v['appName']}")
    return v


# ---------------------------------------------------------------------------
# Point d'entrée
# ---------------------------------------------------------------------------

def generate(values_raw: dict, output_dir: str | None = None) -> str:
    validate(values_raw)
    values = apply_common_defaults(values_raw)

    dest = Path(output_dir) if output_dir else Path(tempfile.mkdtemp(prefix="golden-path-"))
    dest.mkdir(parents=True, exist_ok=True)

    target = values["target"]

    if target == "kubernetes":
        generate_kubernetes(values, dest)
    elif target == "vm":
        generate_vm(values, dest)
    elif target == "cloud":
        generate_cloud(values, dest)

    return str(dest)


if __name__ == "__main__":
    src = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    raw = json.load(src)
    print(generate(raw))