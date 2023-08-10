from aluno import Aluno
from gerenciador import GerenciadorEquipe

gerenciador = GerenciadorEquipe()

aluno1 = Aluno("fulano","111.111.111-11")
aluno2 = Aluno("sicrano","222.111.111-11")
aluno3 = Aluno("beltrano","333.111.111-11")
lista1 = [aluno1, aluno2]
lista2 = [aluno2, aluno3]
projeto1 = "X"
projeto2 = "Y"

criou = gerenciador.criarEquipe(lista1, projeto1)
if criou:
    print("Equipe 1 criada com sucesso!")
else:
    print ("Não foi possível criar a equipe 1")

criou = gerenciador.criarEquipe(lista2, projeto2)
if criou:
    print("Equipe 2 criada com sucesso!")
else:
    print ("Não foi possível criar a equipe 2")
