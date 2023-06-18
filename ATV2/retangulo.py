from ponto import Ponto

class Retangulo:

    def __init__(self, vertice, largura, altura):
        self.vertice = vertice
        self.largura = largura
        self.altura = altura

    def getVertice(self):
        return self.vertice

    def setVertice(self, vertice):
        self.vertice = vertice

    def getLargura(self):
        return self.largura

    def setLargura(self, largura):
        self.largura = largura

    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        self.altura = altura

    def getCentro(self):
        x_do_centro = self.vertice.x + self.largura/2
        y_do_centro = self.vertice.y + self.altura/2
        centro = Ponto(x_do_centro, y_do_centro)
        return centro