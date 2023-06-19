from historico import Historico

class Conta:
    def __init__(self, numero, titular, saldo=0, limite=1000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def getNumero(self):
        return self.numero

    def setNumero(self, numero):
        self.numero = numero

    def getTitular(self):
        return self.titular

    def setTitular(self, titular):
        self.titular = titular

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("depósito de {}".format(valor))

    def sacar(self, valor):
        if valor > self.saldo:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))
            return True

    def extrato(self):
        print("Número: {}\nTitular: {}\nSaldo: {}".format(
            self.numero,self.titular.nome, self.saldo))
        print("-----------------------")
        self.historico.transacoes.append("Tirou extrato - Saldo de {}".format(self.saldo))

    def transfere(self, destino, valor):
        retirou = self.sacar(valor)
        if retirou:
            destino.depositar(valor)
            self.historico.transacoes.append("Tranferiu {} para a conta {}".
                                             format(valor, destino.numero))
            return True
        else:
            return False

