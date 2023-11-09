import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("select * from agenda")
resultado = cursor.fetchone()
print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
cursor.close()
conexao.close()