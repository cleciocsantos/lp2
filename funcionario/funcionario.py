import abc
class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def getNome(self):
        return self._nome
    def setNome(self, nome):
        self._nome = nome

    def getCpf(self):
        return self._cpf
    def setCpf(self, cpf):
        self._cpf = cpf

    def getSalario(self):
        return self._salario
    def setSalario(self, salario):
        self._salario = salario

    @abc.abstractmethod
    def getBonificacao(self):
        return self._salario * 0.1