import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("delete from agenda where nome = 'André'")
print("Registros alterados:", cursor.rowcount)
if cursor.rowcount == 1:
    conexao.commit()
    print("Alterações gravadas")
else:
    conexao.rollback()
    print("Alterações abortadas")
cursor.close()
conexao.close()