import sqlite3
conexao = sqlite3.connect("agenda.db")
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()
cursor.execute("select * from agenda")
condicao = True
while condicao:
    resultado = cursor.fetchone()
    if resultado is None:
        condicao = False
    else:
        print(f"Nome: {resultado['nome']}\nTelefone: {resultado['telefone']}")
cursor.close()
conexao.close()