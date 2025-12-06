from typing import Dict
import pandas as pd


def build_user_base(dfs: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    users = dfs["users"].copy()
    accounts = dfs["accounts"].copy()
    cards = dfs["cards"].copy()
    features = dfs["features"].copy()
    news = dfs["news"].copy()

    # ----- JOIN BÁSICO -----
    # Junta User + Account (1:1)
    base = users.merge(
        accounts,
        how="left",
        left_on="id",
        right_on="user_id",
        suffixes=("", "_account"),
    )

    base.drop(columns=["user_id"], inplace=True, errors="ignore")

    # Junta Card (1:1)
    base = base.merge(
        cards,
        how="left",
        left_on="id",
        right_on="user_id",
        suffixes=("", "_card"),
    )
    base.drop(columns=["user_id"], inplace=True, errors="ignore")

    # ----- AGREGAÇÕES -----
    # Qtd de features por usuário
    feat_agg = (
        features.groupby("user_id")
        .agg(
            features_count=("icon", "count"),
        )
        .reset_index()
    )

    # Qtd de notícias por usuário
    news_agg = (
        news.groupby("user_id")
        .agg(
            news_count=("icon", "count"),
        )
        .reset_index()
    )

    base = base.merge(feat_agg, how="left", left_on="id", right_on="user_id")
    base = base.merge(news_agg, how="left", left_on="id", right_on="user_id", suffixes=("_feat", "_news"))

    base.drop(columns=["user_id_feat", "user_id_news"], inplace=True, errors="ignore")

    base["features_count"].fillna(0, inplace=True)
    base["news_count"].fillna(0, inplace=True)

    # ----- FEATURES DERIVADAS -----
    # Taxa de utilização da conta
    base["account_utilization"] = base["balance"] / base["limit"]
    # Limita para evitar divisão por zero / NaN
    base["account_utilization"] = base["account_utilization"].fillna(0).clip(lower=-5, upper=5)

    # Classificação do limite do cartão
    def classify_card_limit(limit: float) -> str:
        if pd.isna(limit):
            return "sem_cartao"
        if limit < 3000:
            return "basic"
        if limit < 10000:
            return "gold"
        if limit < 20000:
            return "platinum"
        return "black"

    base["card_segment"] = base["limit_card"].apply(classify_card_limit)

    # Score de engajamento (regra simples, só para exemplo)
    # Peso: features(2) + news(1) + saldo positivo
    base["engagement_score"] = (
        2 * base["features_count"]
        + 1 * base["news_count"]
        + (base["balance"] > 0).astype(int) * 2
    )

    # Ordena colunas de forma amigável
    cols_order = [
        "id",
        "name",
        "number",          # conta
        "agency",
        "balance",
        "limit",
        "number_card",
        "limit_card",
        "card_segment",
        "features_count",
        "news_count",
        "account_utilization",
        "engagement_score",
    ]

    # Garante que só usa colunas que existem
    cols_order = [c for c in cols_order if c in base.columns]
    base = base[cols_order].sort_values("id").reset_index(drop=True)

    return base
