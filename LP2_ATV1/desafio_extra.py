from triangulo import Triangulo

lista_triangulos = []

opcao = 's'

print("-------- CADASTRO DE TRIÂNGULOS -------------")
while opcao.lower() == 's':
    print("--- Digite as medidas do Triângulo ---- ")
    ladoA = int(input("Lado A: "))
    ladoB = int(input("Lado B: "))
    ladoC = int(input("Lado C: "))
    triangulo = Triangulo(ladoA, ladoB, ladoC)
    lista_triangulos.append(triangulo)
    opcao = input("Deseja cadastrar novo triângulo? [S/N]")

print("------- SOMA DE TODOS OS PERÍMETROS ------")
soma_perimetros = 0
for triangulo in lista_triangulos:
    soma_perimetros += triangulo.calcularPerimetro()
print("A soma dos perímetros é ", soma_perimetros)

print("------ TRIÂNGULO DE MAIOR LADO ENTRE TODOS -------")
maiorLado = 0
trianguloMaior = None
for triangulo in lista_triangulos:
    if triangulo.getMaiorLado() > maiorLado:
        maiorLado = triangulo.getMaiorLado()
        trianguloMaior = triangulo
print("As medidas do triângulo de maior lado são:")
print("Lado A:", trianguloMaior.ladoA)
print("Lado B:", trianguloMaior.ladoB)
print("Lado C:", trianguloMaior.ladoC)