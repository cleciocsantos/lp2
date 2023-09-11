from gerente import Gerente
from cliente import Cliente
from diretor import Diretor
from sistemainterno import SistemaInterno
from autenticavel import Autenticavel

Autenticavel.register(Cliente)

gerente1 = Gerente('lucas', '91283203', 10000.0, '123', 10)
diretor1 = Diretor('João', '999999', 20000.0)
cliente1 = Cliente('noah', '19987603', '28/03/2007')

sistema = SistemaInterno()
sistema.login(diretor1, '123')
sistema.login(gerente1, '123')
sistema.login(cliente1, '123')