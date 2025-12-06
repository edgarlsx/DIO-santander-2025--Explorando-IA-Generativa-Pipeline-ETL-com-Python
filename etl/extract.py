import os
import pandas as pd


DATA_RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "data", "raw")


def _build_path(filename: str) -> str:
    return os.path.abspath(os.path.join(DATA_RAW_DIR, filename))


def extract_users() -> pd.DataFrame:
    path = _build_path("users.csv")
    return pd.read_csv(path)


def extract_accounts() -> pd.DataFrame:
    path = _build_path("accounts.csv")
    return pd.read_csv(path)


def extract_cards() -> pd.DataFrame:
    path = _build_path("cards.csv")
    return pd.read_csv(path)


def extract_features() -> pd.DataFrame:
    path = _build_path("features.csv")
    return pd.read_csv(path)


def extract_news() -> pd.DataFrame:
    path = _build_path("news.csv")
    return pd.read_csv(path)


def extract_all() -> dict:
    """
    Função de conveniência para extrair tudo de uma vez.
    Retorna um dicionário com todos os DataFrames.
    """
    return {
        "users": extract_users(),
        "accounts": extract_accounts(),
        "cards": extract_cards(),
        "features": extract_features(),
        "news": extract_news(),
    }
