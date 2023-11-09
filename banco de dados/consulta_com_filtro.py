import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("select * from agenda where nome = 'Nilo'")
condicao = True
while condicao:
    resultado = cursor.fetchone()
    if resultado is None:
        condicao = False
    else:
        print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
cursor.close()
conexao.close()