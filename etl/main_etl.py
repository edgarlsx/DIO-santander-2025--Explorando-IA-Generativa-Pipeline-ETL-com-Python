"""
Script principal do ETL.

Como executar (a partir da raiz do projeto):

    python -m src.main_etl

Certifique-se de ter criado os CSVs em data/raw.
"""

from etl.extract import extract_all
from etl.transform import build_user_base
from etl.load import save_user_base


def run_etl():
    print("==> Iniciando ETL de usuários bancários...")
    dfs = extract_all()
    print(" - Extração concluída.")

    df_users_enriched = build_user_base(dfs)
    print(" - Transformação concluída.")
    print(df_users_enriched)

    output_path = save_user_base(df_users_enriched)
    print(f" - Load concluído. Arquivo salvo em: {output_path}")


if __name__ == "__main__":
    run_etl()
