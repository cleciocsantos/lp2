import sqlite3
conexao = sqlite3.connect("brasil.db")
cursor = conexao.cursor()
cursor.execute(
    '''
    create table estados(
        id integer primary key autoincrement,
        nome text,
        populacao integer)
    '''
)
conexao.commit()
cursor.close()
conexao.close()
