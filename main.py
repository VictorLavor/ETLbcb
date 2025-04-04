from src.extractTransform import etlBcB

df = etlBcB('20191')
print(df)

# salvarCsv(dadosBcb, "src/datasets/meiosPagamentosTri.csv", ";",".")

# salvarSqlite(dadosBcb, "src/datasets/etlbcb.db", "meios_pagamentos_tri")

salvarMySql(dadosBcb, "root", "root", "localhost", "etlbcb", "meios_pagamento_tri")