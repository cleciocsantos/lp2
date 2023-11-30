import sqlite3
conexao = sqlite3.connect("brasil.db")
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

regioes = [("SP", "SUDESTE", "São Paulo"),
             ("RJ", "SUDESTE", "Rio de Janeiro"),
             ("MG", "SUDESTE", "Minas Gerais"),
             ("ES", "SUDESTE", "Espírito Santo"),
             ("BA", "NORDESTE", "Bahia"),
             ("PE", "NORDESTE", "Pernambuco"),
             ("CE", "NORDESTE", "Ceará"),
             ("MA", "NORDESTE", "Maranhão"),
             ("PB", "NORDESTE", "Paraíba"),
             ("RN", "NORDESTE", "Rio Grande do Norte"),
             ("AL", "NORDESTE", "Alagoas"),
             ("PI", "NORDESTE", "Piauí"),
             ("SE", "NORDESTE", "Sergipe"),
             ("RS", "SUL", "Rio Grande do Sul"),
             ("PA", "SUL", "Paraná"),
             ("SC", "SUL", "Santa Catarina"),
             ("PR", "NORTE", "Pará"),
             ("AM", "NORTE", "Amazonas"),
             ("RO", "NORTE", "Rondônia"),
             ("TO", "NORTE", "Tocantins"),
             ("AC", "NORTE", "Acre"),
             ("AP", "NORTE", "Amapá"),
             ("RR", "NORTE", "Roraima"),
             ("GO", "CENTRO-OESTE", "Goiás"),
             ("MG", "CENTRO-OESTE", "Mato Grosso"),
             ("DF", "CENTRO-OESTE", "Distrito Federal"),
             ("MS", "CENTRO-OESTE", "Mato Grosso do Sul")
]

cursor.executemany("update estados set sigla = ?, regiao = ? where nome = ?", regioes)

conexao.commit()
cursor.close()
conexao.close()