import sqlite3
conexao = sqlite3.connect("brasil.db")
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()
cursor.execute("select regiao, count(*) as contagem, min(populacao) as min, max(populacao) as max, "
               "avg(populacao) as avg, sum(populacao) as sum from estados group by regiao")
print('REGIÃO       NÚMERO DE ESTADOS  POPULAÇÃO    MÍNIMA        MÁXIMA                MÉDIA              TOTAL')
print('============ ==================             =======      ========   ==================          =========')
condicao = True
while condicao:
    resultado = cursor.fetchone()
    if resultado is None:
        condicao = False
    else:
        print(f"{resultado['regiao']:12} {resultado['contagem']:17} "
              f"{resultado['min']:20} {resultado['max']:13} {resultado['avg']:20} {resultado['sum']:18}")
cursor.execute("select count(*) as contagem, min(populacao) as min, max(populacao) as max, "
               "avg(populacao) as avg, sum(populacao) as sum from estados")
resultado = cursor.fetchone()
print(f"Brasil       {resultado['contagem']:17} "
              f"{resultado['min']:20} {resultado['max']:13} {resultado['avg']:20} {resultado['sum']:18}")

print("\nAgora só as regiões com mais de 5 estados!\n")

cursor.execute("select regiao, count(*) as contagem, min(populacao) as min, max(populacao) as max, "
               "avg(populacao) as avg, sum(populacao) as sum from estados group by regiao "
               "having contagem >=5")
print('REGIÃO       NÚMERO DE ESTADOS  POPULAÇÃO    MÍNIMA        MÁXIMA                MÉDIA              TOTAL')
print('============ ==================             =======      ========   ==================          =========')
condicao = True
while condicao:
    resultado = cursor.fetchone()
    if resultado is None:
        condicao = False
    else:
        print(f"{resultado['regiao']:12} {resultado['contagem']:17} "
              f"{resultado['min']:20} {resultado['max']:13} {resultado['avg']:20} {resultado['sum']:18}")

cursor.close()
conexao.close()