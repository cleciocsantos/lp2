from funcionario import Funcionario
class Diretor(Funcionario):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def getBonificacao(self):
        return self._salario * 0.2