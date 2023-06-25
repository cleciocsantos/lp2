from itempedido import ItemPedido

class Pedido:

    def __init__(self):
        self.itens_pedido = []

    def adicionar_item(self, produto, quantidade):
        item = ItemPedido(produto, quantidade)
        self.itens_pedido.append(item)

    def obter_total(self):
        total = 0.0
        for item in self.itens_pedido:
            total += item.produto.valor * item.quantidade
            item.imprimir()  # linha incluída para o desafio extra
            print("-"*50)  # linha incluída para o desafio extra
        return total