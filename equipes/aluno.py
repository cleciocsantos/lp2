class Aluno:

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf