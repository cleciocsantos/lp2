from funcionario import Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        #Funcionario.__init__(nome, cpf, salario)
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtdFuncionarios = qtd_funcionarios

    def getSenha(self):
        return self._senha
    def setSenha(self, senha):
        self._senha = senha

    def getQtdFuncionarios(self):
        return self._qtdFuncionarios
    def setQtdFuncionarios(self,qtd_funcionarios):
        self._qtdFuncionarios = qtd_funcionarios

    def autenticar(self, senha):
        if self._senha == senha:
            return True
        else:
            return False

    def getBonificacao(self):
        return super().getBonificacao() + 1000