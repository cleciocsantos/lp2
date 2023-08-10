class Equipe:

    def __init__(self, alunos, projeto):
        self._alunos = alunos
        self._projeto = projeto

    def get_alunos(self):
        return self._alunos

    def get_projeto(self):
        return self._projeto

    def set_projeto(self, projeto):
        self._projeto = projeto