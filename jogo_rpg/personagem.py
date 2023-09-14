from random import randint

class Personagem:
    def __init__(self, nome, hp, forca, constituicao, sabedoria, inteligencia, carisma = 10):
        self._nome = nome
        self._hp = hp
        self._forca = forca
        self._destreza = 10 - carisma
        self._constituicao = constituicao
        self._sabedoria = sabedoria
        self._inteligencia = inteligencia
        self._carisma = carisma

    def atacar(self):
        hp = randint(1, 20) * self._forca
        print("O seu ataque vai tirar", hp, "de HP")
        return hp

    def defender(self):
        return self._constituicao

    def desviarAtaque(self):
        desvio = randint(1, 5) * self._destreza
        print("O seu desvio é de", desvio)
        return desvio

    def getNome(self):
        return self._nome

    def getHP(self):
        return self._hp

    #Lista todos os atributos e seus valores
    def ficha(self):
        pass
