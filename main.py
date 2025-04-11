import pandas as pd
from src.extractTransform import requestsApiBcb
from src.load import salvarCSV, salvarSQLite, salvarMySQL

dadosBcb = requestsApiBcb("20191")
salvarCsv(dadosBcb, "src/datasets/meiosPagamentosTri.csv", ";", ".")

salvarSqlite(dadosBcb, "src/datasets/etlbcb.db", "meios_pagamentos_tri")

salvarMySQL(dadosBcb, "root", "root", "localhost", "etlbcb", "meiospagamentostri")
