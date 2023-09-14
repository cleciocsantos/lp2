from personagem import Personagem

class Batalha:

    @staticmethod
    def duelar(p1, p2):
        print("P1:", p1.getNome())
        valor_ataque = p1.atacar()
        valor_destreza = p2.desviarAtaque()
        if valor_ataque > valor_destreza:
            print("Ataque efetuado com sucesso")
        else:
            print("Ops, o adversário desviou do seu ataque")
        print("P2:", p2.getNome())
        p2.atacar()
