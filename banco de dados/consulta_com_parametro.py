import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
nome = input("Quem você quer pesquisar: ")
cursor.execute("select * from agenda where nome = ?",(nome,))
condicao = True
achou = False
while condicao:
    resultado = cursor.fetchone()
    if resultado is None:
        condicao = False
        if achou == False:
            print(f"Usuário {nome} não registrado")
    else:
        achou = True
        print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
cursor.close()
conexao.close()