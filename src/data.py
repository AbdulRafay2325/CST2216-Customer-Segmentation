import pandas as pd


FEATURES = [
    "Age",
    "Annual_Income",
    "Spending_Score",
]


def validate_data(frame: pd.DataFrame) -> pd.DataFrame:

    missing = sorted(
        set(FEATURES) - set(frame.columns)
    )

    if missing:
        raise ValueError(
            f"Missing required columns: {', '.join(missing)}"
        )

    result = frame.copy()

    result[FEATURES] = result[FEATURES].apply(
        pd.to_numeric,
        errors="coerce"
    )

    if result[FEATURES].isna().any().any():
        raise ValueError(
            "Age, income, and spending score "
            "must be numeric and non-empty."
        )

    if len(result) < 20:
        raise ValueError(
            "At least 20 customers are required."
        )

    if (result["Age"] <= 0).any():
        raise ValueError(
            "Age must be greater than 0."
        )

    if (result["Annual_Income"] < 0).any():
        raise ValueError(
            "Annual income cannot be negative."
        )

    if (
        (result["Spending_Score"] < 1) |
        (result["Spending_Score"] > 100)
    ).any():
        raise ValueError(
            "Spending score must be between 1 and 100."
        )

    return result