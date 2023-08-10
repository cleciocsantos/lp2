class Barbie:

    _total_barbie = 0

    def __init__(self, profissao, preco):
        self._profissao = profissao
        self._preco = preco
        Barbie._total_barbie += 1

    @staticmethod
    def get_total_barbies():
        return Barbie._total_barbie