from pathlib import Path

from gitlab import Gitlab
import pandas as pd
from bertopic import BERTopic


class Issue:

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description


def import_data(gitlab_project_id: str = "", project_name: str = "kubeapp"):
    try:
        print(
            f"Chargement du fichier ./tools/gitlab-board-analyzer/resources/{project_name}/data.csv"
        )
        data = pd.read_csv(
            f"./tools/gitlab-board-analyzer/resources/{project_name}/data.csv", sep=";"
        )
        return data
    except:
        print("Fichier non trouvé récupération des données sur Gitlab")
        gl = Gitlab(
            url="https://gitlab.insee.fr",
            private_token="",
            ssl_verify=False,
        )
        project = gl.projects.get(id=gitlab_project_id)
        issues = project.issues.list(get_all=True)
        rows = []
        for issue in issues:
            _issue = project.issues.get(id=issue.get_id())
            rows.append({"title": _issue.title, "description": _issue.description})
        df = pd.DataFrame(rows)
        Path(
            f"./tools/gitlab-board-analyzer/resources/{project_name}/data.csv"
        ).parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(
            f"./tools/gitlab-board-analyzer/resources/{project_name}/data.csv", sep=";"
        )
        return df


def analyze(data: pd.DataFrame, project_name: str = "kubeapp"):
    data["title"] = data["title"].fillna("")
    data["description"] = data["description"].fillna("")
    data["text"] = data["title"] + " " + data["description"]
    # Très important : forcer en string
    data["text"] = data["text"].astype(str)
    topic_model = BERTopic(language="multilingual")
    topics, probs = topic_model.fit_transform(data["text"].tolist())

    data["topic"] = topics
    topic_model.get_topic_info().to_csv(
        f"./tools/gitlab-board-analyzer/resources/{project_name}/topics.csv"
    )
    data.to_csv(f"./tools/gitlab-board-analyzer/resources/{project_name}/analyze.csv")
    topic_model.visualize_topics()


if __name__ == "__main__":
    # data = import_data(gitlab_project_id="10331", project_name="kubeapp")
    # analyze(data=data, project_name="kubeapp")
    data = import_data(gitlab_project_id="15962", project_name="iahs")
    analyze(data=data, project_name="iahs")
