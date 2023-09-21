from personagem import Personagem

class Batalha:

    @staticmethod
    def duelar(p1, p2):
        print("P1:", p1.getNome(), "- Tipo:", p1.__class__.__name__)
        valor_ataque = p1.atacar()
        print("Valor do ataque:", valor_ataque)
        print("-"*10)
        print("P2:", p2.getNome( ), "- Tipo:", p2.__class__.__name__)
        valor_desvio = p2.desviarAtaque()
        print("Valor do desvio:", valor_desvio)
        if valor_ataque > valor_desvio:
            print("Ataque efetuado com sucesso")
        else:
            print("Ops, o adversário desviou do seu ataque")
