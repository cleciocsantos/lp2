from conta import Conta

contas = []
opcao = 's'

while opcao.lower() == 's':
    print('Digite o número:')
    numero = input()
    print('Digite o titular:')
    titular = input()
    print('Digite o saldo:')
    saldo = int(input())
    nova_conta = Conta(numero, titular, saldo)
    contas.append(nova_conta)
    print("Deseja cadastrar uma nova conta? [S/N]")
    opcao = input()

print('========== Cadastro de Contas ===========')
for conta in contas:
    conta.extrato()
    #print("Número:", conta.numero)
    #print("Titular:", conta.titular)
    #print("Saldo:", conta.saldo)
    #print("-----------------------")

print('========== Consulta de Conta ===========')
print('Digite seu nome:')
nome = input()
achou = False
for conta in contas:
    if nome == conta.getTitular():
        conta.extrato()
        achou = True
if not achou:
    print("Conta não cadastrada!")

