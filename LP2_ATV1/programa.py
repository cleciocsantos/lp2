from triangulo import Triangulo

print("--- Digite as medidas do Triângulo ---- ")
ladoA = int(input("Lado A: "))
ladoB = int(input("Lado B: "))
ladoC = int(input("Lado C: "))
triangulo = Triangulo(ladoA, ladoB, ladoC)
print("O perímetro do triângulo é ", triangulo.calcularPerimetro())
print("O maior lado do triângulo é ", triangulo.getMaiorLado())