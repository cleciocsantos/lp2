class Cliente:
    def __init__(self, nome, cpf, datanasc):
        self.nome = nome
        self.cpf = cpf
        self.datanasc = datanasc

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getCPF(self):
        return self.cpf

    def setCPF(self, cpf):
        self.cpf = cpf

    def getDataNasc(self):
        return self.datanasc

    def setDataNasc(self, datanasc):
        self.datanasc = datanasc

    def imprimir(self):
        print("Nome: ", self.nome)
        print("CPF: ", self.cpf)
        print("Data de nascimento: ", self.datanasc)
