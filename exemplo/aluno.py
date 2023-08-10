class Aluno:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = 0

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_curso(self):
        return self.curso

    def set_curso(self, curso):
        self.curso = curso

    def get_tempoSemDormir(self):
        return self.tempoSemDormir

    def estudar(self, qtd_horas):
        self.tempoSemDormir += qtd_horas

    def dormir(self, qtd_horas):
        self.tempoSemDormir -= qtd_horas