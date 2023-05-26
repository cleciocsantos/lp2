class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcularPerimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        return perimetro

    def getMaiorLado(self):
        maiorLado = self.ladoA
        if self.ladoB > maiorLado:
            maiorLado = self.ladoB
        if self.ladoC > maiorLado:
            maiorLado = self.ladoC
        return maiorLado