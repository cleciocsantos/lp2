from gerente import Gerente
from funcionario import Funcionario
gerente1 = Gerente('lucas', '91283203', 10000.0, '123', 10)
funcionario1 = Funcionario('matheus', '12332124', 1250.0)
print(gerente1.getNome())
print(gerente1.getSenha())
print(funcionario1.getNome())
print(funcionario1.getSalario())
print("bonificação do gerente é de:", gerente1.getBonificacao())
print("bonificação do funcionario é de:", funcionario1.getBonificacao())