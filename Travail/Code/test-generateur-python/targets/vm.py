"""
Cible : VM on-premise
Génère :
  - Terraform  → provisioning de la VM (vSphere/libvirt selon hyperviseur)
  - Ansible    → configuration de la VM + déploiement applicatif
  - Rundeck    → job de déploiement / rollback
"""

from pathlib import Path
from ._renderer import render, write

# ---------------------------------------------------------------------------
# Profils de VM
# ---------------------------------------------------------------------------

VM_PROFILES = {
    "xs": {"cpu": 1,  "ram_mb": 1024,  "disk_gb": 20},
    "s":  {"cpu": 2,  "ram_mb": 2048,  "disk_gb": 40},
    "m":  {"cpu": 4,  "ram_mb": 4096,  "disk_gb": 80},
    "l":  {"cpu": 8,  "ram_mb": 8192,  "disk_gb": 160},
    "xl": {"cpu": 16, "ram_mb": 16384, "disk_gb": 320},
}

HYPERVISORS = ["vsphere", "libvirt"]


# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

def apply_defaults(v: dict) -> dict:
    v = v.copy()

    v.setdefault("vmProfile",        "s")
    v.setdefault("hypervisor",       "vsphere")
    v.setdefault("osImage",          "ubuntu-22.04")
    v.setdefault("vmNetwork",        "VM Network")
    v.setdefault("vmDatastore",      "datastore1")
    v.setdefault("vmFolder",         f"{v['teamName']}/{v['environnement']}")
    v.setdefault("appPort",          8080)
    v.setdefault("appUser",          "appuser")
    v.setdefault("configEnv",        {})
    v.setdefault("enableMonitoring", True)

    # Nexus
    v.setdefault("nexusUrl",         "https://nexus.example.fr")
    v.setdefault("nexusRepository",  "releases")
    v.setdefault("artifactFormat",   "jar")   # jar | docker | rpm

    # Rundeck
    v.setdefault("rundeckUrl",       "https://rundeck.example.fr")
    v.setdefault("rundeckProject",   v["teamName"])

    profile = v["vmProfile"]
    if profile not in VM_PROFILES:
        raise ValueError(f"vmProfile '{profile}' inconnu. Valeurs : {list(VM_PROFILES)}")
    v["vmSize"] = VM_PROFILES[profile]

    hypervisor = v["hypervisor"]
    if hypervisor not in HYPERVISORS:
        raise ValueError(f"hypervisor '{hypervisor}' inconnu. Valeurs : {HYPERVISORS}")

    return v


# ---------------------------------------------------------------------------
# Génération
# ---------------------------------------------------------------------------

TERRAFORM_FILES = {
    "vsphere": [
        ("main.tf.j2",       "terraform/main.tf"),
        ("variables.tf.j2",  "terraform/variables.tf"),
        ("outputs.tf.j2",    "terraform/outputs.tf"),
    ],
    "libvirt": [
        ("main.tf.j2",       "terraform/main.tf"),
        ("variables.tf.j2",  "terraform/variables.tf"),
        ("outputs.tf.j2",    "terraform/outputs.tf"),
    ],
}

ANSIBLE_FILES = [
    ("playbook.yml.j2",              "ansible/playbook.yml"),
    ("inventory.ini.j2",             "ansible/inventory.ini"),
    ("roles/app/tasks/main.yml.j2",  "ansible/roles/app/tasks/main.yml"),
    ("roles/app/vars/main.yml.j2",   "ansible/roles/app/vars/main.yml"),
    ("roles/app/templates/app.service.j2",
                                     "ansible/roles/app/templates/app.service.j2"),
]

RUNDECK_FILES = [
    ("job-deploy.yaml.j2",   "rundeck/job-deploy.yaml"),
    ("job-rollback.yaml.j2", "rundeck/job-rollback.yaml"),
]


def generate_vm(values_raw: dict, output_dir: Path) -> None:
    v          = apply_defaults(values_raw)
    tpl_base   = Path(__file__).parent.parent / "templates" / "vm"
    hypervisor = v["hypervisor"]

    # Terraform (dépend de l'hyperviseur)
    for tpl_name, out_path in TERRAFORM_FILES[hypervisor]:
        src = tpl_base / "terraform" / hypervisor / tpl_name
        write(output_dir / out_path, render(src, v))

    _write_tfvars(v, output_dir)

    # Ansible (commun)
    for tpl_name, out_path in ANSIBLE_FILES:
        src = tpl_base / "ansible" / tpl_name
        write(output_dir / out_path, render(src, v))

    # Rundeck
    for tpl_name, out_path in RUNDECK_FILES:
        src = tpl_base / "rundeck" / tpl_name
        write(output_dir / out_path, render(src, v))

    _write_readme(v, output_dir)


def _write_tfvars(v: dict, output_dir: Path) -> None:
    size = v["vmSize"]
    lines = [
        f'app_name    = "{v["appName"]}"',
        f'team_name   = "{v["teamName"]}"',
        f'environment = "{v["environnement"]}"',
        f'cpu_count   = {size["cpu"]}',
        f'ram_mb      = {size["ram_mb"]}',
        f'disk_gb     = {size["disk_gb"]}',
        f'vm_network  = "{v["vmNetwork"]}"',
    ]
    write(output_dir / "terraform" / "terraform.tfvars", "\n".join(lines) + "\n")


def _write_readme(v: dict, output_dir: Path) -> None:
    size = v["vmSize"]
    content = f"""# {v['appName']} — VM on-premise ({v['hypervisor']})

Généré par le **Golden Path** (cible : VM).

## 1. Provisionner la VM (Terraform)

```bash
cd terraform/
terraform init
terraform plan
terraform apply
```

## 2. Configurer et déployer l'application (Ansible)

```bash
cd ansible/
ansible-playbook -i inventory.ini playbook.yml
```

## 3. Opérations via Rundeck

Importez les jobs depuis `rundeck/` dans votre instance Rundeck :

```bash
rd jobs load -p {v['rundeckProject']} -f rundeck/job-deploy.yaml
rd jobs load -p {v['rundeckProject']} -f rundeck/job-rollback.yaml
```

Puis déclenchez depuis l'interface Rundeck ou via la CLI :

```bash
rd run -p {v['rundeckProject']} -j "Deploy {v['appName']}" \\
  -o artifact_version=1.2.3
```

## Informations

| Champ | Valeur |
|---|---|
| Hyperviseur | `{v['hypervisor']}` |
| Profil VM | `{v['vmProfile']}` ({size['cpu']} vCPU / {size['ram_mb']} Mo / {size['disk_gb']} Go) |
| OS | `{v['osImage']}` |
| Port applicatif | `{v['appPort']}` |
| Format artefact | `{v['artifactFormat']}` |
| Nexus | `{v['nexusUrl']}/{v['nexusRepository']}` |
| Rundeck projet | `{v['rundeckProject']}` |

## Structure générée

```
terraform/   ← provisioning VM ({v['hypervisor']})
ansible/     ← configuration OS + déploiement applicatif
rundeck/     ← jobs deploy et rollback
README.md    ← ce fichier
```
"""
    write(output_dir / "README.md", content)
