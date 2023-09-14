from personagem import Personagem
from random import randint

class Anao(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 70, 7, 10, 8, 6, 2)

    def atacar(self):
        hp = randint(1,6) * self._forca
        print("O seu ataque vai tirar", hp, "de HP")
        return hp

    def defender(self):
        return super().defender() + 2