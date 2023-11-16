import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("update agenda set telefone = '1234-5678' where nome = 'Nilo'")
print("Registros alterados:", cursor.rowcount)
if cursor.rowcount == 1:
    conexao.commit()
    print("Alterações gravadas")
else:
    conexao.rollback()
    print("Alterações abortadas")
cursor.close()
conexao.close()