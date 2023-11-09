import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
dados = [("João","98901-0109"),
         ("André", "98902-8900"),
         ("Maria", "97891-3321")]
cursor.executemany(
    '''
    insert into agenda (nome, telefone)
    values (?,?)
    ''', dados
)
conexao.commit()
cursor.close()
conexao.close()