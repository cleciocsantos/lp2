import abc
class Autenticavel(abc.ABC):

    @abc.abstractmethod
    def autenticar(self, senha):
        pass