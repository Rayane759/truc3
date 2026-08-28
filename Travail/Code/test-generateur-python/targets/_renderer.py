"""
Utilitaires partagés : rendu Jinja2 et écriture de fichiers.
Ce module est le seul endroit où Jinja2 est utilisé.
"""

from pathlib import Path
from jinja2 import Environment, FileSystemLoader, StrictUndefined


def render(template_path: Path, values: dict) -> str:
    """Rend un template Jinja2 avec les valeurs fournies."""
    env = Environment(
        loader=FileSystemLoader(str(template_path.parent)),
        trim_blocks=True,
        lstrip_blocks=True,
        undefined=StrictUndefined,   # erreur immédiate si une variable est absente
    )
    return env.get_template(template_path.name).render(**values)


def write(dest: Path, content: str) -> None:
    """Crée les répertoires parents si nécessaire, puis écrit le fichier."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding="utf-8")