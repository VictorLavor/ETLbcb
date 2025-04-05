from src.extractTransform import etlBcB
from src.load import saveCsv

df = etlBcB('20191')
<<<<<<< HEAD
print(df)

# salvarCsv(dadosBcb, "src/datasets/meiosPagamentosTri.csv", ";",".")

# salvarSqlite(dadosBcb, "src/datasets/etlbcb.db", "meios_pagamentos_tri")

salvarMySql(dadosBcb, "root", "root", "localhost", "etlbcb", "meios_pagamento_tri")
=======

saveCsv(df, "meiosPagamentosTri", ";", ".")
>>>>>>> a83fbb7 (Segunda Aula)
