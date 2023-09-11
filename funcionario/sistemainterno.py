from autenticavel import Autenticavel
class SistemaInterno:
    def login(self, obj, senha):
        if(isinstance(obj, Autenticavel)):
            obj.autenticar(senha)
            return True
        else:
            print(obj.__class__.__name__,'não é autenticável')
            return False