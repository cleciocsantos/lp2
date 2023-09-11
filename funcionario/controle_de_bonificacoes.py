from funcionario import Funcionario
class ControleDeBonificacoes:
    def __init__(self, totalDeBonificacoes = 0):
        self._totalDeBonificacoes = totalDeBonificacoes

    def registra(self, funcionario):
        #if isinstance(funcionario, Funcionario):
        if hasattr(funcionario, 'getBonificacao'):
            self._totalDeBonificacoes += funcionario.getBonificacao()
        else:
            print('objeto da classe',funcionario.__class__.__name__,'não tem o metodo getBonificacao')

    def getTotalDeBonificacoes(self):
        return self._totalDeBonificacoes