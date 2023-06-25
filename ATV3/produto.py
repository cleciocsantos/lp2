class Produto:
    def __init__(self, codigo, valor, descricao):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getDescricao(self):
        return self.descricao

    def setDescricao(self, descricao):
        self.descricao = descricao

    def imprimir(self):
        print("Código:", self.codigo)
        print("Valor:", self.valor)
        print("Descrição:", self.descricao)
