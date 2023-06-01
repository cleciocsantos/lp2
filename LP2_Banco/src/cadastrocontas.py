from conta import Conta
from pessoa import Pessoa

print("========== CADASTRO DE PESSOAS ==========")
pessoas = []
opcao = 's'
while opcao.lower() == 's':
    print('Digite o nome:')
    nome = input()
    print('Digite o CPF:')
    cpf = input()
    print('Digite a data de nascimento:')
    datanasc = input()
    nova_pessoa = Pessoa(nome, cpf, datanasc)
    pessoas.append(nova_pessoa)
    print("Deseja cadastrar uma nova pessoa? [S/N]")
    opcao = input()

print("========== CADASTRO DE CONTAS ==========")
contas = []
opcao = 's'
while opcao.lower() == 's':
    print('Digite o número:')
    numero = input()
    #print('Digite o titular:')
    #titular = input()
    print("Digite o número correspondente ao titular:")
    indice = 1
    for pessoa in pessoas:
        print(indice, ' - ', pessoa.nome)
        indice += 1
    opcao_titular = int(input())
    titular = pessoas[opcao_titular-1]
    print("Titular selecionado:")
    titular.imprimir()
    print('Digite o saldo:')
    saldo = int(input())
    nova_conta = Conta(numero, titular, saldo)
    contas.append(nova_conta)
    print("Deseja cadastrar uma nova conta? [S/N]")
    opcao = input()

print('========== Contas Cadastradas ===========')
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
    if nome == conta.getTitular().getNome():
        conta.extrato()
        achou = True
if not achou:
    print("Conta não cadastrada!")

