# 📊 ETLbcb – Estatísticas de Meios de Pagamento

Projeto de ETL (Extract, Transform, Load) que coleta, trata e organiza dados públicos disponibilizados pelo Banco Central do Brasil relacionados aos meios de pagamento utilizados no país.

## 🔍 Objetivo

Extrair informações atualizadas da API do Banco Central sobre diversas formas de pagamento, realizar a limpeza e transformação dos dados, e organizar em arquivos CSV prontos para análises futuras.

## 🧹 Fontes de Dados

As informações são provenientes da API de **Estatísticas de Meios de Pagamentos** do Banco Central, acessível na [documentação oficial](https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/documentacao), que inclui:

### Periodicidade Mensal:
- 📌 **Pix** – SPI e documento 1201
- 📌 **TED** – CIP-SITRAF e STR
- 📌 **Boletos** – CIP-SILOC
- 📌 **DOC e TEC** – CIP-SILOC
- 📌 **Cheque** – Compe

### Periodicidade Trimestral:
- 💳 Cartões de crédito, débito e pré-pagos (docs 6308 e 6334)
- 🔁 Transferências intrabancárias (doc 6209)
- 🏧 Quantidade de ATMs (doc 6209)
- 🦾 Estabelecimentos credenciados (doc 6334)
- 🧲 Tarifas (TIC, MDR), programas de recompensa, terminais POS/PDV
- 📈 Volumetria por canal e produto (doc 6209)

### Periodicidade Anual:
- 📅 Planilha consolidada com estatísticas gerais no [site oficial do BC](https://www.bcb.gov.br/)

## 🧐 Dicionário de Dados

| Campo              | Descrição                                      |
|--------------------|-----------------------------------------------|
| `Modalidade`       | Tipo de meio de pagamento                     |
| `Ano`              | Ano da transação                              |
| `Trimestre`        | Trimestre de referência (1 a 4)               |
| `Quantidade`       | Volume total de transações                    |
| `Valor`            | Valor financeiro total movimentado           |
| `Fonte`            | Origem do dado no sistema do Banco Central   |

## 🛠️ Tecnologias

- Python
- Pandas
- Requests
- Git / GitHub

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/VictorLavor/ETLbcb.git
   cd ETLbcb
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o pipeline:
   ```bash
   python main.py
   ```

## 📁 Estrutura do Projeto

```
ETLbcb/
│
├── main.py                 # Script principal do projeto
├── src/
│   ├── datasets/           # Arquivos CSV gerados
│   ├── load.py             # Funções auxiliares de carregamento
│   └── __init__.py
└── README.md
```

## 👨‍💻 Autor

Victor Matheus de Lavor  
[GitHub: @VictorLavor](https://github.com/VictorLavor)


