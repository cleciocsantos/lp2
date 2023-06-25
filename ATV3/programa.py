from pedido import Pedido
from produto import Produto

motog = Produto(1234, 500.00, "Moto G")
galaxy = Produto(5234, 700.00, "Samsung Galaxy")
zenphone = Produto(4234, 400.00, "Zen Phone")
iphone = Produto(3213, 4000.00, "IPhone X")

p1 = Pedido()
p1.adicionar_item(motog, 3)
p1.adicionar_item(galaxy, 2)
p1.adicionar_item(zenphone, 2)
print("Valor total do pedido 1 = ", p1.obter_total())

p2 = Pedido()
p2.adicionar_item(iphone, 1)
print("Valor total do pedido 2 = ", p2.obter_total())
