from carro import Carro

Camaro = Carro(10)
print("A gasolina do carro está em:", Camaro.obterGasolina(), "Litros.")
Camaro.adicionarGasolina(25)
Camaro.adicionarGasolina(15)
print("A gasolina do carro está em:", Camaro.obterGasolina(), "Litros.")
Camaro.andar(50)
print("A gasolina do carro está em:", Camaro.obterGasolina(), "Litros.")
Camaro.andar(200)
print("A gasolina do carro está em:", Camaro.obterGasolina(), "Litros.")
Camaro.andar(300)
print("A gasolina do carro está em:", Camaro.obterGasolina(), "Litros.")
Camaro.tanque = -10
print("A gasolina do carro está em:", Camaro.obterGasolina(), "Litros.")

bmw = Carro(8)
ferrari = Carro(5)
print("total de carros:", Carro.get_total_carros())
