from funcionario import Funcionario
from autenticavel import Autenticavel
class Diretor(Funcionario, Autenticavel):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def getBonificacao(self):
        return self._salario * 0.2

    def autenticar(self, senha):
        print("Diretor autenticado")