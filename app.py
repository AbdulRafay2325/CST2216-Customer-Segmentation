import logging
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from src.model import assign, evaluate_k, train


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

LOGGER = logging.getLogger(__name__)


st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="🛍️",
)

st.title("Mall Customer Segmentation")


PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_DATA = PROJECT_ROOT / "data" / "mall_customers.csv"


upload = st.file_uploader(
    "Optional: upload another compatible mall_customers.csv",
    type="csv",
)


try:

    if upload is not None:

        data = pd.read_csv(upload)

        st.info("Using uploaded dataset.")

    else:

        if not DEFAULT_DATA.exists():
            raise FileNotFoundError(
                "data/mall_customers.csv was not found."
            )

        data = pd.read_csv(DEFAULT_DATA)

        st.info(
            "Using the bundled Week 11 mall customer dataset."
        )


    comparison = evaluate_k(data)

    suggested = int(
        comparison.loc[
            comparison["silhouette"].idxmax(),
            "k"
        ]
    )


    k = st.slider(
        "Number of clusters",
        min_value=2,
        max_value=8,
        value=suggested,
    )


    model, clustered, score = train(
        data,
        k
    )


    col1, col2 = st.columns(2)

    col1.metric(
        "Silhouette Score",
        f"{score:.3f}"
    )

    col2.metric(
        "Suggested k",
        suggested
    )


    figure = px.scatter(
        clustered,
        x="Annual_Income",
        y="Spending_Score",
        color=clustered["Cluster"].astype(str),
        hover_data=["Age"],
        title="Income and Spending Segments",
    )

    st.plotly_chart(
        figure,
        use_container_width=True
    )


    st.subheader("Cluster Profiles")

    profiles = (
        clustered
        .groupby("Cluster")[
            [
                "Age",
                "Annual_Income",
                "Spending_Score",
            ]
        ]
        .mean()
        .round(1)
    )

    st.dataframe(profiles)


    st.subheader("Assign a Customer")


    with st.form("customer"):

        age = st.slider(
            "Age",
            18,
            90,
            35
        )

        income = st.slider(
            "Annual income (thousands)",
            1,
            200,
            60
        )

        spending = st.slider(
            "Spending score",
            1,
            100,
            50
        )

        submitted = st.form_submit_button(
            "Assign Segment"
        )


    if submitted:

        customer = {
            "Age": age,
            "Annual_Income": income,
            "Spending_Score": spending,
        }

        cluster = assign(
            model,
            customer
        )

        st.success(
            f"Assigned cluster: {cluster}"
        )


except Exception as exc:

    LOGGER.exception(
        "Customer segmentation application failed"
    )

    st.error(
        f"Could not process the data: {exc}"
    )