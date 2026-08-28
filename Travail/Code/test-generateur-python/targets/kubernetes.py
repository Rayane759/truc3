"""
Cible : Kubernetes
Génère un Helm chart complet dans output_dir/chart/
"""

from pathlib import Path
from ._renderer import render, write

# Profils CPU/RAM
RESOURCE_PROFILES = {
    "xs": {"cpuReq": "50m",  "memReq": "64Mi",  "cpuLim": "100m", "memLim": "128Mi"},
    "s":  {"cpuReq": "100m", "memReq": "128Mi", "cpuLim": "250m", "memLim": "256Mi"},
    "m":  {"cpuReq": "250m", "memReq": "512Mi", "cpuLim": "500m", "memLim": "1Gi"},
    "l":  {"cpuReq": "500m", "memReq": "1Gi",   "cpuLim": "1",    "memLim": "2Gi"},
    "xl": {"cpuReq": "1",    "memReq": "2Gi",   "cpuLim": "2",    "memLim": "4Gi"},
}


def apply_defaults(v: dict) -> dict:
    v = v.copy()
    v.setdefault("imageTag",           "latest")
    v.setdefault("imageRepository",    f"registry.example.fr/{v['teamName']}/{v['appName']}")
    v.setdefault("namespace",          f"{v['environnement']}-{v['appName']}")
    v.setdefault("workloadType",       "Deployment")
    v.setdefault("replicaCount",       1)
    v.setdefault("servicePort",        8080)
    v.setdefault("exposureProfile",    "internal")
    v.setdefault("publicHost",         "")
    v.setdefault("enableHealthProbes", True)
    v.setdefault("healthPath",         "/actuator")
    v.setdefault("enableAutoscaling",  False)
    v.setdefault("resourceProfile",    "s")
    v.setdefault("configEnv",          {})

    profile = v["resourceProfile"]
    if profile not in RESOURCE_PROFILES:
        raise ValueError(f"resourceProfile inconnu : '{profile}'. Valeurs : {list(RESOURCE_PROFILES)}")
    v["resources"] = RESOURCE_PROFILES[profile]

    return v


def generate_kubernetes(values_raw: dict, output_dir: Path) -> None:
    v   = apply_defaults(values_raw)
    tpl = Path(__file__).parent.parent / "templates" / "kubernetes"

    files = [
        (tpl / "Chart.yaml.j2",                  output_dir / "chart" / "Chart.yaml"),
        (tpl / "values.yaml.j2",                  output_dir / "chart" / "values.yaml"),
        (tpl / "templates" / "deployment.yaml.j2",output_dir / "chart" / "templates" / "deployment.yaml"),
        (tpl / "templates" / "service.yaml.j2",   output_dir / "chart" / "templates" / "service.yaml"),
        (tpl / "templates" / "ingress.yaml.j2",   output_dir / "chart" / "templates" / "ingress.yaml"),
        (tpl / "templates" / "configmap.yaml.j2", output_dir / "chart" / "templates" / "configmap.yaml"),
    ]

    for src, dst in files:
        write(dst, render(src, v))

    _write_readme(v, output_dir)


def _write_readme(v: dict, output_dir: Path) -> None:
    content = f"""# {v['appName']} — Kubernetes

Généré par le **Golden Path** (cible : Kubernetes).

## Déploiement

```bash
helm upgrade --install {v['appName']} ./chart \\
  --namespace {v['namespace']} --create-namespace
```

## Informations

| Champ | Valeur |
|---|---|
| Namespace | `{v['namespace']}` |
| Image | `{v['imageRepository']}:{v['imageTag']}` |
| Profil ressources | `{v['resourceProfile']}` |
| Exposition | `{v['exposureProfile']}` |
"""
    write(output_dir / "README.md", content)