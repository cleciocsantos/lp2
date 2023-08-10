#consumo km/l
class Carro:

    _total_carros = 0

    def __init__(self,consumo):
        self.consumo = consumo
        self._tanque = 0
        Carro._total_carros += 1

    @staticmethod
    def get_total_carros():
        return Carro._total_carros

    def obterGasolina(self):
        return self._tanque

    def adicionarGasolina(self,qtdGasolina):
        self._tanque += qtdGasolina

    def andar(self, distanciaPercorrida):
        combustivelGasto = distanciaPercorrida/self.consumo
        if combustivelGasto <= self._tanque:
            self._tanque -= combustivelGasto
        else:
            print("Gasolina insuficiente para o percurso ")

