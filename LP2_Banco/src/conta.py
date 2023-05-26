class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

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

