from ponto import Ponto
from retangulo import Retangulo

x = float(input("Digite a coordenada x do ponto: "))
y = float(input("Digite a coordenada y do ponto: "))

ponto = Ponto(x, y)

largura = float(input("Digite a largura do retangulo: "))
altura = float(input("Digite a altura do retangulo: "))

retangulo = Retangulo(ponto, largura, altura)

centro = retangulo.getCentro()

print("\nAs coordenadas do centro do retângulo são:")
centro.imprimir()
