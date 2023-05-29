class Conta:
    def __init__(self, numero, titular, saldo=0, limite=1000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

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

    def sacar(self, valor):
        if valor > self.saldo:
            return False
        else:
            self.saldo -= valor
            return True

    def extrato(self):
        print("Número: {}\nTitular: {}\nSaldo: {}".format(
            self.numero,self.titular, self.saldo))
        print("-----------------------")

    def transfere(self, destino, valor):
        retirou = self.sacar(valor)
        if retirou:
            destino.depositar(valor)
            return True
        else:
            return False

