import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    df.to_csv(f"src/datasets/{nome_arquivo}.csv", decimal=decimal, sep=separador)
    return


def salvarSQLite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):

    conn = sqlite3.connect(nome_banco)

    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)

    conn.close()
    return


def salvarMySQL(
    df: pd.DataFrame, usuario: str, senha: str, host: str, banco: str, nome_tabela: str
):
    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")
    df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)

    return


from pathlib import Path


def salvarCSV(df, nome_arquivo):
    """
    Salva um DataFrame como um arquivo CSV na pasta src/datasets.

    Parâmetros:
    df (pd.DataFrame): O DataFrame contendo os dados a serem salvos.
    nome_arquivo (str): O nome do arquivo CSV (ex: 'meiosPagamentosTri.csv').

    O arquivo será salvo no caminho 'src/datasets/<nome_arquivo>'.
    """
    caminho = Path("src/datasets")
    caminho.mkdir(parents=True, exist_ok=True)
    df.to_csv(caminho / nome_arquivo, index=False)
