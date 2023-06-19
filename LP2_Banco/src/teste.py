from pessoa import Pessoa
from conta import Conta

pessoa1 = Pessoa("João", "111.111.111-11", "25/07/2003")
pessoa2 = Pessoa("Maria", "222.222.222-22", "30/08/2007")

c1 = Conta("123",pessoa1, 15, 1500)
c2 = Conta("123",pessoa2)
#c2 = c1

c1.depositar(100)
c1.sacar(50)
c1.transfere(c2, 20)
c1.extrato()

c1.historico.imprimir()
c2.historico.imprimir()

"""
c1.titular.imprimir()
#print(c1.titular.nome)
#print(c1.titular.cpf)

print("O limite de c1 é", c1.limite)
print("O limite de c1 é", c2.limite)

c1.transfere(c2, 10)

print(c1.saldo)
print(c2.saldo)
"""