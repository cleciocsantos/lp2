from personagem import Personagem
from random import randint

class Elfo(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 80, 9, 5, 6, 7, 4)

    def atacar(self):
        hp = randint(3,5) * self._forca
        print("O seu ataque vai tirar", hp, "de HP")
        return hp

    def desviarAtaque(self):
        return super().desviarAtaque() + 2