from batalha import Batalha
from anao import Anao
from elfo import Elfo

#anao = Anao("Pequeno Gigante")
#elfo = Elfo("Guerreiro Voador")

#Batalha.duelar(anao, elfo)

personagens = []

condicao = True
while condicao:
    opcao1 = int(input('''Escolha sua opção: 
    [1] Cadastrar um personagem
    [2] Duelar
    [3] Encerrar o jogo.
    '''))
    if opcao1 == 1:
        tipo = int(input('''Escolha o tipo do personagem:
        [1] Anão 
        [2] Elfo
        '''))
        if tipo == 1:
            nome = str(input("Digite o nome do Anão:"))
            anao_novo = Anao(nome)
            personagens.append(anao_novo)
        elif tipo == 2:
            nome = str(input("Digite o nome do Elfo:"))
            elfo_novo = Elfo(nome)
            personagens.append(elfo_novo)
    elif opcao1 == 2:
        i = 0
        for p in personagens:
            print(i,'->',p.getNome(), "- Tipo:", p.__class__.__name__)
            i += 1
        indice1 = int(input("Digite o índice do primeiro personagem do duelo:"))
        indice2 = int(input("Digite o índice do segundo personagem do duelo:"))
        p1 = personagens[indice1]
        p2 = personagens[indice2]
        Batalha.duelar(p1, p2)
    else:
        condicao = False