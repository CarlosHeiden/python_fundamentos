#2 - Classe Pessoa:
#Crie uma classe chamada Pessoa com o atributo nome (public). 
#Implemente métodos set_nome(novo_nome) e get_nome() para manipular esse atributo.


class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

if __name__ == '__main':

    pessoa1 = Pessoa('caue')
    pessoa2 = Pessoa('arthur')
    pessoa3 = Pessoa('joao')

    print(pessoa1.get_nome())
    print(pessoa2.get_nome())
    print(pessoa3.get_nome())

    pessoa1.set_nome('Carlos')
    pessoa2.set_nome('Aline'.upper())

    print(pessoa1.get_nome())
    print(pessoa2.get_nome())

    