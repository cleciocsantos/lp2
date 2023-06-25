from produto import Produto
from pedido import Pedido

print("========== CADASTRO DE PRODUTOS ==========")
produtos = []
opcao = 's'
while opcao.lower() == 's':
    codigo = int(input('Digite o código do produto: '))
    valor = float(input('Digite o valor do produto: '))
    descricao = input('Digite a descrição do produto: ')
    novo_produto = Produto(codigo, valor, descricao)
    produtos.append(novo_produto)
    print("Deseja cadastrar um novo produto? [S/N]")
    opcao = input()

pedidos = []
opcao_pedido = 's'
while opcao_pedido.lower() == 's':
    print("========== CRIAR PEDIDO ==========")
    novo_pedido = Pedido()
    opcao_item = 's'
    while opcao_item.lower() == 's':
        print('Escolha um produto para incluir no pedido:')
        indice = 1
        for produto in produtos:
            print(indice, ':')
            produto.imprimir()
            indice += 1
        indice_produto = int(input("Digite o indice do produto escolhido: "))
        produto_escolhido = produtos[indice_produto - 1]
        print("O produto escolhido foi:")
        produto_escolhido.imprimir()

        quantidade = int(input("Digite a quantidade desejada: "))
        novo_pedido.adicionar_item(produto_escolhido, quantidade)

        print("Deseja incluir mais um item no pedido? [S/N]")
        opcao_item = input()
    print("========== EXTRATO DO PEDIDO ==========")
    pedidos.append(novo_pedido)
    print("O valor total do pedido é:", novo_pedido.obter_total())

    print("Deseja criar um novo pedido? [S/N]")
    opcao_pedido = input()