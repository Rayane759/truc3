"""
Cible : Cloud (AWS / GCP / Azure)
Génère du Terraform adapté au provider choisi.
"""

from pathlib import Path
from ._renderer import render, write

# ---------------------------------------------------------------------------
# Tailles d'instances par provider et profil
# ---------------------------------------------------------------------------

INSTANCE_SIZES = {
    "aws": {
        "xs": "t3.micro",      "s": "t3.small",       "m": "t3.medium",
        "l":  "t3.large",      "xl": "t3.xlarge",
    },
    "gcp": {
        "xs": "e2-micro",      "s": "e2-small",        "m": "e2-medium",
        "l":  "e2-standard-2", "xl": "e2-standard-4",
    },
    "azure": {
        "xs": "Standard_B1s",  "s": "Standard_B2s",    "m": "Standard_B4ms",
        "l":  "Standard_D4s_v3", "xl": "Standard_D8s_v3",
    },
}

DEFAULT_REGIONS = {
    "aws":   "eu-west-1",
    "gcp":   "europe-west1",
    "azure": "westeurope",
}

# Templates communs à tous les providers
COMMON_FILES = [
    ("_versions.tf.j2", "terraform/_versions.tf"),
    ("_variables.tf.j2","terraform/variables.tf"),
    ("_outputs.tf.j2",  "terraform/outputs.tf"),
]

# Templates spécifiques à chaque provider
PROVIDER_FILES = {
    "aws": [
        ("main.tf.j2",        "terraform/main.tf"),
        ("networking.tf.j2",  "terraform/networking.tf"),
        ("compute.tf.j2",     "terraform/compute.tf"),
        ("database.tf.j2",    "terraform/database.tf"),
    ],
    "gcp": [
        ("main.tf.j2",        "terraform/main.tf"),
        ("networking.tf.j2",  "terraform/networking.tf"),
        ("compute.tf.j2",     "terraform/compute.tf"),
        ("database.tf.j2",    "terraform/database.tf"),
    ],
    "azure": [
        ("main.tf.j2",        "terraform/main.tf"),
        ("networking.tf.j2",  "terraform/networking.tf"),
        ("compute.tf.j2",     "terraform/compute.tf"),
        ("database.tf.j2",    "terraform/database.tf"),
    ],
}


# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

def apply_defaults(v: dict) -> dict:
    v = v.copy()
    provider = v["cloudProvider"]

    v.setdefault("cloudRegion",        DEFAULT_REGIONS[provider])
    v.setdefault("cloudProfile",       "s")
    v.setdefault("appPort",            8080)
    v.setdefault("enableDatabase",     False)
    v.setdefault("dbEngine",           "postgres")
    v.setdefault("dbVersion",          "15")
    v.setdefault("enableLoadBalancer", True)
    v.setdefault("enableHttps",        True)
    v.setdefault("publicHost",         "")
    v.setdefault("configEnv",          {})
    v.setdefault("tags", {
        "team":        v["teamName"],
        "environment": v["environnement"],
        "managed-by":  "golden-path",
    })

    profile = v["cloudProfile"]
    sizes   = INSTANCE_SIZES.get(provider, {})
    if profile not in sizes:
        raise ValueError(f"cloudProfile '{profile}' inconnu pour '{provider}'. Valeurs : {list(sizes)}")
    v["instanceType"] = sizes[profile]

    return v


# ---------------------------------------------------------------------------
# Génération
# ---------------------------------------------------------------------------

def generate_cloud(values_raw: dict, output_dir: Path) -> None:
    v        = apply_defaults(values_raw)
    provider = v["cloudProvider"]
    tpl_base = Path(__file__).parent.parent / "templates" / "cloud"

    # Fichiers communs (indépendants du provider)
    for tpl_name, out_path in COMMON_FILES:
        src = tpl_base / "_common" / tpl_name
        write(output_dir / out_path, render(src, v))

    # Fichiers spécifiques au provider
    for tpl_name, out_path in PROVIDER_FILES[provider]:
        src = tpl_base / provider / tpl_name
        write(output_dir / out_path, render(src, v))

    _write_tfvars(v, output_dir)
    _write_readme(v, output_dir)


def _write_tfvars(v: dict, output_dir: Path) -> None:
    """Génère un terraform.tfvars prêt à l'emploi."""
    lines = [
        f'app_name    = "{v["appName"]}"',
        f'team_name   = "{v["teamName"]}"',
        f'environment = "{v["environnement"]}"',
        f'region      = "{v["cloudRegion"]}"',
        f'app_port    = {v["appPort"]}',
    ]
    if v["enableDatabase"]:
        lines += [
            f'db_engine  = "{v["dbEngine"]}"',
            f'db_version = "{v["dbVersion"]}"',
        ]
    write(output_dir / "terraform" / "terraform.tfvars", "\n".join(lines) + "\n")


def _write_readme(v: dict, output_dir: Path) -> None:
    provider = v["cloudProvider"].upper()
    content = f"""# {v['appName']} — Cloud ({provider})

Généré par le **Golden Path** (cible : Cloud / {provider}).

## Déploiement

```bash
cd terraform/

# 1. Initialiser les providers Terraform
terraform init

# 2. Vérifier le plan
terraform plan

# 3. Appliquer
terraform apply
```

## Modifier la configuration

Modifiez `terraform/terraform.tfvars` pour ajuster les paramètres,
puis relancez `terraform apply`.

## Informations

| Champ            | Valeur |
|---|---|
| Provider         | `{provider}` |
| Région           | `{v['cloudRegion']}` |
| Instance         | `{v['instanceType']}` |
| Load Balancer    | `{'oui' if v['enableLoadBalancer'] else 'non'}` |
| Base de données  | `{'oui (' + v['dbEngine'] + ' ' + v['dbVersion'] + ')' if v['enableDatabase'] else 'non'}` |
| HTTPS            | `{'oui' if v['enableHttps'] else 'non'}` |

## Structure générée

```
terraform/
├── _versions.tf     — versions des providers Terraform
├── variables.tf     — déclaration de toutes les variables
├── outputs.tf       — valeurs exposées après apply
├── main.tf          — provider + backend
├── networking.tf    — VPC / réseau / sous-réseaux
├── compute.tf       — instance(s) applicative(s)
├── database.tf      — base de données managée (si activée)
└── terraform.tfvars — valeurs à personnaliser
```
"""
    write(output_dir / "README.md", content)
