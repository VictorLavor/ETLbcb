import pandas as pd

def saveCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal:str):
    df.to_csv(f'src/datasets/{nome_arquivo}.csv', decimal=decimal, sep=separador)

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