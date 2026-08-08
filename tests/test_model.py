from pathlib import Path

import pandas as pd

from src.model import assign, evaluate_k, train


PROJECT_ROOT = (
    Path(__file__).resolve().parents[1]
)

DATA_PATH = (
    PROJECT_ROOT /
    "data" /
    "mall_customers.csv"
)


def test_clusters_and_assignment():

    data = pd.read_csv(DATA_PATH)

    comparison = evaluate_k(data)

    assert not comparison.empty

    best_k = int(
        comparison.loc[
            comparison["silhouette"].idxmax(),
            "k"
        ]
    )

    model, result, score = train(
        data,
        best_k
    )

    assert result["Cluster"].nunique() == best_k

    assert -1 <= score <= 1

    cluster = assign(
        model,
        {
            "Age": 30,
            "Annual_Income": 70,
            "Spending_Score": 80,
        }
    )

    assert 0 <= cluster < best_k
