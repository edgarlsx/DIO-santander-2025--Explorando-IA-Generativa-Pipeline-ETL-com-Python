import os
import pandas as pd


DATA_PROCESSED_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "data", "processed")


def save_user_base(df: pd.DataFrame, filename: str = "users_enriched.csv") -> str:
    os.makedirs(DATA_PROCESSED_DIR, exist_ok=True)
    path = os.path.abspath(os.path.join(DATA_PROCESSED_DIR, filename))
    df.to_csv(path, index=False)
    return path
