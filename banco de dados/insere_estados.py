import sqlite3
conexao = sqlite3.connect("brasil.db")
cursor = conexao.cursor()
estados_dados = [("São Paulo", 444441238),
                 ("Minas Gerais", 20538718),
                 ("Rio de Janeiro",16054524),
                 ("Bahia", 14141626),
                 ("Paraná", 1144380),
                 ("Rio Grande do Sul", 10882965),
                 ("Pernambuco", 9058931),
                 ("Ceará", 8794957),
                 ("Pará", 8121025),
                 ("Santa Catarina", 7610361),
                 ("Goiás", 7056495),
                 ("Maranhão", 6775805),
                 ("Paraíba", 3974687),
                 ("Amazonas", 3941613),
                 ("Espírito Santo", 3833712),
                 ("Mato Grosso", 3658649),
                 ("Rio Grande do Norte",3302729),
                 ("Piauí", 3272199),
                 ("Alagoas", 3127683),
                 ("Distrito Federal", 2817381),
                 ("Mato Grosso do Sul", 2757013),
                 ("Sergipe", 2209558),
                 ("Rondônia", 1581196),
                 ("Tocantins", 1511460),
                 ("Acre", 830018),
                 ("Amapá", 733759),
                 ("Roraima", 636707)]

cursor.executemany(
    '''
    insert into estados (nome, populacao)
    values (?,?)
    ''', estados_dados
)

conexao.commit()
cursor.close()
conexao.close()