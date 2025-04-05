# 💳 ETLbcb – Estatísticas de Meios de Pagamento (Banco Central)

Este projeto tem como objetivo **extrair, transformar e carregar (ETL)** dados públicos fornecidos pelo **Banco Central do Brasil**, relacionados aos meios de pagamento utilizados no país.

Os dados contemplam instrumentos como **Pix, TED, boletos, DOC, cartões, cheques, convênios, saques**, entre outros – com diferentes frequências de atualização (mensal, trimestral e anual).

---

## 📊 Fontes dos dados

As informações são obtidas via **API do Banco Central** e documentos internos, incluindo:

- **Mensal:**
  - Pix (SPI, documento 1201)
  - TED (CIP-SITRAF, STR)
  - Boletos (CIP-SILOC)
  - DOC e TEC (CIP-SILOC)
  - Cheque (Compe)

- **Trimestral:**
  - Cartões de crédito, débito e pré-pagos (doc. 6308, 6334)
  - Pagamentos de convênio, transferências intrabancárias, débitos diretos (doc. 6209)
  - Volumetria por canal, ATMs, POS/PDV, recompensas e tarifas

- **Anual:**
  - Consolidação geral disponível via site do BC

---

## ⚙️ Tecnologias utilizadas

- `Python`
- `Pandas`
- `Requests`
- Organização modular com scripts em `src/`

---

## 🚀 Como executar

1. Clone este repositório:

```bash
git clone https://github.com/VictorLavor/ETLbcb.git
cd ETLbcb
```
2. Crie e ative um ambiente virtual:
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
3.Instale as dependências (caso exista um requirements.txt):
pip install -r requirements.txt
4.Execute o script principal:
python main.py

Estrutura do projeto
 ETLbcb/
├── main.py                # Script principal
├── src/
│   ├── __init__.py
│   ├── load.py            # Carga e transformação dos dados
│   └── datasets/
│       └── meiosPagamentosTri.csv
├── README.md              # Você está aqui :)
└── .gitignore

Status
 Requisição de dados da API

 Armazenamento local em .csv

 Análise exploratória

 Visualizações interativas

 Dashboard final (opcional)

 Contribuições
Sinta-se à vontade para abrir issues ou enviar pull requests.
Este projeto está em fase de aprendizado e evolução contínua. 

Licença
Este projeto está sob a licença MIT.
