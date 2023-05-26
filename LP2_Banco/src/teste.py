from pessoa import Pessoa
from conta import Conta

conta1 = Conta("123","João", 15)

print(conta1.getTitular())
conta1.setTitular("Rodrigo")
print(conta1.getTitular())

consegui = conta1.sacar(30)
if consegui:
    print("Consegui sacar!")
else:
    print("Não consegui sacar!")