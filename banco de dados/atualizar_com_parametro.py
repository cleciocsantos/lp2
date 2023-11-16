import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
nome = input("Digite o nome do contato a ser atualizado:")
telefone = input(f"Digite o novo número de {nome}:")
cursor.execute("update agenda set telefone = ? where nome = ?",(telefone,nome))
print("Registros alterados:", cursor.rowcount)
if cursor.rowcount == 1:
    conexao.commit()
    print("Alterações gravadas")
else:
    conexao.rollback()
    print("Alterações abortadas")
cursor.close()
conexao.close()