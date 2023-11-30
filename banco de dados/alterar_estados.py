import sqlite3
conexao = sqlite3.connect("brasil.db")
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()
conexao.execute("alter table estados add sigla text")
conexao.execute("alter table estados add regiao text")
conexao.commit()
cursor.close()
conexao.close()
