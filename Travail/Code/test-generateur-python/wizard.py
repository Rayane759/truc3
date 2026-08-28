"""
Golden Path — Assistant interactif (wizard)
Lance : python wizard.py
"""

import os
import sys
from generate import generate

# ---------------------------------------------------------------------------
# Helpers d'affichage
# ---------------------------------------------------------------------------

BOLD  = "\033[1m"
CYAN  = "\033[96m"
GREEN = "\033[92m"
RED   = "\033[91m"
DIM   = "\033[2m"
RESET = "\033[0m"

def title(text: str)  -> None: print(f"\n{BOLD}{CYAN}{text}{RESET}")
def success(text: str)-> None: print(f"\n{GREEN}✔ {text}{RESET}")
def error(text: str)  -> None: print(f"{RED}✘ {text}{RESET}")
def hint(text: str)   -> None: print(f"{DIM}  {text}{RESET}")


def ask(prompt: str, default: str = "", required: bool = True) -> str:
    """Pose une question, affiche la valeur par défaut, valide si requis."""
    display = f"{BOLD}{prompt}{RESET}"
    if default:
        display += f" {DIM}[{default}]{RESET}"
    display += " : "

    while True:
        value = input(display).strip() or default
        if value or not required:
            return value
        error("Ce champ est obligatoire.")


def choose(prompt: str, options: list[tuple[str, str]], default: str = "") -> str:
    """Affiche une liste numérotée et retourne la clé choisie."""
    print(f"\n{BOLD}{prompt}{RESET}")
    for i, (key, label) in enumerate(options, 1):
        marker = f"{GREEN}▶{RESET}" if key == default else " "
        print(f"  {marker} {i}) {label}")

    keys    = [k for k, _ in options]
    default_idx = keys.index(default) + 1 if default in keys else ""

    while True:
        raw = input(f"\n{BOLD}Votre choix{RESET} {DIM}[{default_idx}]{RESET} : ").strip()
        if not raw and default:
            return default
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return keys[int(raw) - 1]
        error(f"Entrez un nombre entre 1 et {len(options)}.")


def confirm(prompt: str, default: bool = True) -> bool:
    """Demande oui/non."""
    suffix = f"{DIM}[{'O/n' if default else 'o/N'}]{RESET}"
    raw = input(f"{BOLD}{prompt}{RESET} {suffix} : ").strip().lower()
    if not raw:
        return default
    return raw in ("o", "oui", "y", "yes")


# ---------------------------------------------------------------------------
# Sections du formulaire
# ---------------------------------------------------------------------------

def section_identity() -> dict:
    title("── 1/4  Identité de l'application")
    return {
        "appName":      ask("Nom de l'application", required=True),
        "teamName":     ask("Équipe responsable",   required=True),
        "environnement": choose("Environnement cible", [
            ("dv", "dv — Développement"),
            ("qf", "qf — Qualification"),
            ("pp", "pp — Pré-production"),
            ("pd", "pd — Production"),
        ], default="dv"),
    }


def section_image(values: dict) -> dict:
    title("── 2/4  Image & déploiement")
    hint("Exemple : registry.example.fr/mon-equipe/mon-app")
    repo = ask(
        "Dépôt de l'image",
        default=f"registry.example.fr/{values['teamName']}/{values['appName']}",
    )
    tag  = ask("Tag de l'image", default="latest")
    return {"imageRepository": repo, "imageTag": tag}


def section_resources() -> dict:
    title("── 3/4  Ressources & exposition")

    profile = choose("Profil de ressources", [
        ("xs", "XS —  50m CPU /  64Mi RAM  (batch léger)"),
        ("s",  "S  — 100m CPU / 128Mi RAM  (microservice)"),
        ("m",  "M  — 250m CPU / 512Mi RAM  (application standard)"),
        ("l",  "L  — 500m CPU /   1Gi RAM  (traitement intensif)"),
        ("xl", "XL —   1 CPU  /   2Gi RAM  (application lourde)"),
    ], default="s")

    port = ask("Port applicatif", default="8080")

    exposure = choose("Mode d'exposition", [
        ("internal", "Interne uniquement (ClusterIP)"),
        ("external", "Exposée à l'extérieur (Ingress + TLS)"),
    ], default="internal")

    public_host = ""
    if exposure == "external":
        hint("Exemple : mon-app.dev.example.fr")
        public_host = ask("Nom de domaine public (FQDN)", required=True)

    return {
        "resourceProfile": profile,
        "servicePort":     int(port),
        "exposureProfile": exposure,
        "publicHost":      public_host,
    }


def section_vm() -> dict:
    title("── 3/4  Configuration VM on-premise")

    hypervisor = choose("Hyperviseur", [
        ("vsphere", "vSphere (VMware)"),
        ("libvirt", "libvirt (KVM/QEMU)"),
    ], default="vsphere")

    profile = choose("Profil de VM", [
        ("xs", "XS —  1 vCPU /  1 Go RAM /  20 Go disque"),
        ("s",  "S  —  2 vCPU /  2 Go RAM /  40 Go disque"),
        ("m",  "M  —  4 vCPU /  4 Go RAM /  80 Go disque"),
        ("l",  "L  —  8 vCPU /  8 Go RAM / 160 Go disque"),
        ("xl", "XL — 16 vCPU / 16 Go RAM / 320 Go disque"),
    ], default="s")

    network = ask("Réseau VM", default="VM Network")

    hint("Format de l'artefact applicatif stocké dans Nexus")
    artifact_format = choose("Format de l'artefact", [
        ("jar",    "JAR  — application Java (Spring Boot…)"),
        ("docker", "Docker — image conteneur"),
        ("rpm",    "RPM  — paquet Linux"),
    ], default="jar")

    nexus_url  = ask("URL Nexus",       default="https://nexus.example.fr")
    nexus_repo = ask("Repository Nexus", default="releases")

    rundeck_url     = ask("URL Rundeck",       default="https://rundeck.example.fr")
    rundeck_project = ask("Projet Rundeck",    default="")

    return {
        "hypervisor":       hypervisor,
        "vmProfile":        profile,
        "vmNetwork":        network,
        "artifactFormat":   artifact_format,
        "nexusUrl":         nexus_url,
        "nexusRepository":  nexus_repo,
        "rundeckUrl":       rundeck_url,
        "rundeckProject":   rundeck_project,
    }


def section_cloud() -> dict:
    title("── 3/4  Configuration Cloud")

    provider = choose("Provider cloud", [
        ("aws",   "AWS   — Amazon Web Services"),
        ("gcp",   "GCP   — Google Cloud Platform"),
        ("azure", "Azure — Microsoft Azure"),
    ], default="aws")

    default_regions = {"aws": "eu-west-1", "gcp": "europe-west1", "azure": "westeurope"}
    region = ask("Région", default=default_regions[provider])

    profile = choose("Profil d'instance", [
        ("xs", "XS — t3.micro / e2-micro / B1s       (test, outil interne)"),
        ("s",  "S  — t3.small / e2-small / B2s       (microservice)"),
        ("m",  "M  — t3.medium / e2-medium / B4ms    (application standard)"),
        ("l",  "L  — t3.large / e2-standard-2 / D4s  (traitement intensif)"),
        ("xl", "XL — t3.xlarge / e2-standard-4 / D8s (application lourde)"),
    ], default="s")

    port = ask("Port applicatif", default="8080")
    lb   = confirm("Activer un Load Balancer ?", default=True)
    tls  = confirm("Activer HTTPS ?",            default=True)

    db = confirm("Activer une base de données managée ?", default=False)
    db_engine, db_version = "", ""
    if db:
        db_engine = choose("Moteur de base de données", [
            ("postgres", "PostgreSQL"),
            ("mysql",    "MySQL"),
        ], default="postgres")
        db_version = ask("Version", default="15" if db_engine == "postgres" else "8.0")

    return {
        "cloudProvider":      provider,
        "cloudRegion":        region,
        "cloudProfile":       profile,
        "appPort":            int(port),
        "enableLoadBalancer": lb,
        "enableHttps":        tls,
        "enableDatabase":     db,
        "dbEngine":           db_engine,
        "dbVersion":          db_version,
    }


def section_advanced() -> dict:
    title("── 4/4  Options avancées")

    probes  = confirm("Activer les health checks (liveness / readiness) ?", default=True)
    health_path = ""
    if probes:
        health_path = ask("Chemin de base des sondes", default="/actuator")

    hpa     = confirm("Activer l'autoscaling horizontal (HPA) ?", default=False)
    replicas = int(ask("Nombre de réplicas", default="1"))

    workload = choose("Type de workload", [
        ("Deployment",  "Deployment  (sans état — recommandé)"),
        ("StatefulSet", "StatefulSet (avec stockage persistant)"),
    ], default="Deployment")

    # Variables d'environnement
    config_env = {}
    if confirm("Ajouter des variables d'environnement (ConfigMap) ?", default=False):
        hint("Entrez les variables une par une. Laissez le nom vide pour terminer.")
        while True:
            key = input(f"  {BOLD}Nom de la variable{RESET} (vide pour finir) : ").strip().upper()
            if not key:
                break
            val = input(f"  {BOLD}Valeur{RESET} : ").strip()
            config_env[key] = val

    return {
        "enableHealthProbes": probes,
        "healthPath":         health_path,
        "enableAutoscaling":  hpa,
        "replicaCount":       replicas,
        "workloadType":       workload,
        "configEnv":          config_env,
    }


# ---------------------------------------------------------------------------
# Résumé avant génération
# ---------------------------------------------------------------------------

def show_summary(values: dict) -> None:
    title("══ Récapitulatif ══════════════════════════════")
    rows = [
        ("Application",   values["appName"]),
        ("Équipe",        values["teamName"]),
        ("Environnement", values["environnement"]),
        ("Image",         f"{values['imageRepository']}:{values['imageTag']}"),
        ("Profil",        values["resourceProfile"]),
        ("Port",          str(values["servicePort"])),
        ("Exposition",    values["exposureProfile"] +
                          (f" → {values['publicHost']}" if values.get("publicHost") else "")),
        ("Health probes", "oui" if values["enableHealthProbes"] else "non"),
        ("Autoscaling",   "oui" if values["enableAutoscaling"] else "non"),
        ("Réplicas",      str(values["replicaCount"])),
        ("Workload",      values["workloadType"]),
        ("Env vars",      ", ".join(values["configEnv"].keys()) or "aucune"),
    ]
    width = max(len(k) for k, _ in rows)
    for k, v in rows:
        print(f"  {DIM}{k:<{width}}{RESET}  {v}")


# ---------------------------------------------------------------------------
# Point d'entrée
# ---------------------------------------------------------------------------

def main() -> None:
    # Effacement de l'écran pour plus de clarté
    os.system("cls" if os.name == "nt" else "clear")

    print(f"""
{BOLD}{CYAN}╔══════════════════════════════════════════╗
║       Golden Path — Générateur Helm      ║
╚══════════════════════════════════════════╝{RESET}
Répondez aux questions pour générer votre chart Helm.
Appuyez sur {BOLD}Entrée{RESET} pour accepter la valeur par défaut {DIM}[entre crochets]{RESET}.
""")

    target = choose("Cible de déploiement", [
        ("kubernetes", "Kubernetes — génère un Helm chart"),
        ("cloud",      "Cloud      — génère du Terraform (AWS / GCP / Azure)"),
        ("vm",         "VM         — génère Terraform + Ansible + Rundeck"),
    ], default="kubernetes")

    values: dict = {"target": target}

    try:
        values |= section_identity()
        if target == "kubernetes":
            values |= section_image(values)
            values |= section_resources()
        elif target == "cloud":
            values |= section_cloud()
        elif target == "vm":
            values |= section_vm()
        values |= section_advanced()
    except KeyboardInterrupt:
        print(f"\n\n{DIM}Génération annulée.{RESET}\n")
        sys.exit(0)

    show_summary(values)

    print()
    if not confirm("Générer le chart Helm avec ces paramètres ?", default=True):
        print(f"{DIM}Génération annulée.{RESET}\n")
        sys.exit(0)

    try:
        output_dir = generate(values)
        success(f"Chart généré dans : {BOLD}{output_dir}{RESET}")
        print(f"""
{DIM}Commandes suivantes :
  helm lint {output_dir}/chart
  helm template {values['appName']} {output_dir}/chart
  helm upgrade --install {values['appName']} {output_dir}/chart --namespace {values.get('namespace', values['appName'])} --create-namespace{RESET}
""")
    except Exception as e:
        error(f"Erreur lors de la génération : {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
