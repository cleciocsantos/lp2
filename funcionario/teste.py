from gerente import Gerente
from funcionario import Funcionario
from controle_de_bonificacoes import ControleDeBonificacoes
from cliente import Cliente
from diretor import Diretor
gerente1 = Gerente('lucas', '91283203', 10000.0, '123', 10)
diretor1 = Diretor('João', '999999', 20000.0)
#funcionario1 = Funcionario('matheus', '12332124', 1250.0)
cliente1 = Cliente('noah', '19987603', '28/03/2007')
print(gerente1.getNome())
print(gerente1.getSenha())
#print(funcionario1.getNome())
#print(funcionario1.getSalario())
print("bonificação do gerente é de:", gerente1.getBonificacao())
#print("bonificação do funcionario é de:", funcionario1.getBonificacao())
controle = ControleDeBonificacoes()
#controle.registra(funcionario1)
controle.registra(gerente1)
controle.registra(cliente1)
print("total:", controle.getTotalDeBonificacoes())