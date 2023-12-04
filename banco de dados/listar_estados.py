import sqlite3
conexao = sqlite3.connect("brasil.db")
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()
cursor.execute("select * from estados order by regiao desc")
condicao = True
while condicao:
    resultado = cursor.fetchone()
    if resultado is None:
        condicao = False
    else:
        print(f"Id: {resultado['id']}\nNome: {resultado['nome']}\n"
              f"População: {resultado['populacao']}\n"
              f"Região: {resultado['regiao']}")
cursor.close()
conexao.close()