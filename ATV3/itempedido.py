class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def getProduto(self):
        return self.produto

    def setProduto(self, produto):
        self.produto = produto

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

    def imprimir(self):
        print("Código do produto:", self.produto.codigo)
        print("Valor do produto:", self.produto.valor)
        print("Descrição do produto:", self.produto.descricao)
        print("Quantidade:", self.quantidade)
