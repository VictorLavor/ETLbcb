import requests
import pandas as pd
import sqlite3

def etlBcB(date:str) -> pd.DataFrame:
    """
    Função para extrair os dados da API do Banco Central.

    Atributo:
    String - AAAAT - A ano e T trimestre (1-4)

    Saída:
    DataFrame com os dados econômicos dos meios de Pagamento.
    """ 
    url ="https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%2720051%27&$format=json"
    req = requests.get(url)
    print("Status Code:", req.status_code)
    data = req.json()

    df = pd.json_normalize(data["value"])

    df['datatrimestre'] = pd.to_datetime(df["datatrimestre"])
    return df

df = etlBcB("20191")
print(df)

def salvarSQLite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):
    conn = sqlite3.connect(nome_banco)

    df.to_sql(nome_tabela, conn ,if_exists='replace', index=False)

    conn.close()
    return

## 📌 Função principal criada

A função `salvarCSV()` foi criada para automatizar o processo de salvamento dos dados extraídos da API para arquivos `.csv`:



