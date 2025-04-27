import requests
import pandas as pd


"""
def requestApiBcb(data):
   
    Funcão para extrair os dados dos meios de pagamentos trimestrais do Banco Central.

    parâmentros:
    data - string - aaaat (Exemplo: 20191)

    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json"
    
    req = requests.get(url)
    dados = req.json()
    
    df = pd.json_normalize(dados['value'])
    return print(df)
requestApiBcb('20241')
"""

def obter_dados(data: str) -> pd.DataFrame: 
    """
    Função que recebe um trimestre como parâmetro, faz uma requisição para a API do BCB e retorna os dados como um DataFrame do pandas.
    
    Parâmetros:
        data (str): Trimestre no formato 'YYYY-MM'.
        
    Retorna:
        pd.DataFrame: DataFrame com os dados obtidos.    
    """ 
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json"
    print(f"Requisitando dados de: {url}")  # Debug para verificar se a URL está certa
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        df = pd.DataFrame(dados.get('value', []))
        print(df)
        return df
    else:
        print("Erro ao obter os dados:", resposta.status_code)
        return pd.DataFrame()  # Retorna vazio em caso de erro


if __name__ == "__main__":
    obter_dados("20231")
