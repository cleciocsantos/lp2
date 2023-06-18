from ponto import Ponto
from retangulo import Retangulo

print("========== CADASTRO DE PONTOS ==========")
pontos = []
opcao = 's'
while opcao.lower() == 's':
    print('Digite a coordenada x:')
    x = float(input())
    print('Digite a coordenada y:')
    y = float(input())
    novo_ponto = Ponto(x, y)
    pontos.append(novo_ponto)
    print("Deseja cadastrar um novo ponto? [S/N]")
    opcao = input()

print("========== CADASTRO DE RETÂNGULOS ==========")
retangulos = []
opcao = 's'
while opcao.lower() == 's':
    print("Como deseja criar o retângulo:")
    print("1 - A partir de um vértice, largura e altura")
    print("2 - A partir de dois vértices")
    escolha = int(input())

    if escolha == 1:
        print("Pontos disponíveis:")
        indice = 1
        for ponto in pontos:
            print(indice, ':')
            ponto.imprimir()
            indice += 1
        ponto_escolhido = int(input("Digite o número do vértice escolhido: "))
        print("O vértice escolhido foi:")
        pontos[ponto_escolhido-1].imprimir()

        largura = float(input("Digite a largura do retangulo: "))
        altura = float(input("Digite a altura do retangulo: "))
        novo_retangulo = Retangulo(pontos[ponto_escolhido-1], largura, altura)
        retangulos.append(novo_retangulo)

    elif escolha == 2:
        print("Pontos disponíveis:")
        indice = 1
        for ponto in pontos:
            print(indice, ':')
            ponto.imprimir()
            indice += 1
        indice_vertice1 = int(input("Digite o número do 1º vértice: "))
        vertice1 = pontos[indice_vertice1 - 1]
        print("O 1º vértice escolhido foi:")
        vertice1.imprimir()

        indice_vertice2 = int(input("Digite o número do 2º vértice: "))
        vertice2 = pontos[indice_vertice2 - 1]
        print("O 2º vértice escolhido foi:")
        vertice2.imprimir()

        while vertice2.getX() == vertice1.getX() or vertice2.getY() == vertice1.getY():
            print("Você não pode escolher dois pontos com a mesma coordenada X ou a mesma coordenada Y!")
            indice_vertice2 = int(input("Digite um novo número para o 2º vértice: "))
            vertice2 = pontos[indice_vertice2 - 1]
            print("O 2º vértice escolhido foi:")
            vertice2.imprimir()


        largura = vertice2.getX() - vertice1.getX()
        altura = vertice2.getY() - vertice1.getY()
        novo_retangulo = Retangulo(vertice1, largura, altura)
        retangulos.append(novo_retangulo)

    print("Deseja cadastrar um novo retangulo? [S/N]")
    opcao = input()

print("\n========== CENTROS DOS RETÂNGULOS CADASTRADOS ==========")
contagem_retangulo = 1
for r in retangulos:
    print("\nRetângulo {}:".format(contagem_retangulo))
    print("Vértice:")
    r.getVertice().imprimir()
    print("Largura:", r.getLargura())
    print("Altura:", r.getAltura())
    centro = r.getCentro()
    print("Coordenadas do centro:")
    centro.imprimir()
    contagem_retangulo += 1