import logging
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from .data import FEATURES, validate_data

LOGGER = logging.getLogger(__name__)


def evaluate_k(frame: pd.DataFrame, candidates=range(3, 9)) -> pd.DataFrame:
    clean = validate_data(frame)
    scaled = StandardScaler().fit_transform(clean[FEATURES])
    rows = []
    for k in candidates:
        if k >= len(clean):
            continue
        model = KMeans(n_clusters=k, init="k-means++", n_init=20, random_state=2216)
        labels = model.fit_predict(scaled)
        rows.append({"k": k, "silhouette": silhouette_score(scaled, labels), "inertia": model.inertia_})
    if not rows:
        raise ValueError("No valid cluster counts for this dataset.")
    return pd.DataFrame(rows)


def train(frame: pd.DataFrame, k: int = 5):
    clean = validate_data(frame)
    if not 2 <= k < len(clean):
        raise ValueError("k must be at least 2 and smaller than the number of rows.")
    pipeline = Pipeline([("scale", StandardScaler()), ("model", KMeans(n_clusters=k, init="k-means++", n_init=20, random_state=2216))])
    labels = pipeline.fit_predict(clean[FEATURES])
    result = clean.copy(); result["Cluster"] = labels
    score = float(silhouette_score(pipeline["scale"].transform(clean[FEATURES]), labels))
    LOGGER.info("Trained KMeans k=%d; silhouette=%.3f", k, score)
    return pipeline, result, score


def assign(model: Pipeline, customer: dict) -> int:
    row = pd.DataFrame([customer])[FEATURES]
    return int(model.predict(row)[0])

