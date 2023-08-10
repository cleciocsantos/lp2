from equipe import Equipe

class GerenciadorEquipe:

    def __init__(self):
        self._equipes = []

    def criarEquipe(self, alunos, projeto):
        for aluno in alunos:
            for equipe in self._equipes:
                for integrante in equipe.get_alunos():
                    if aluno == integrante:
                        return False
        equipe_nova = Equipe(alunos, projeto)
        self._equipes.append(equipe_nova)
        return True
