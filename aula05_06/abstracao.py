from abc import ABC, abstractclassmethod


class PessoaAbstrata(ABC):

    @abstractclassmethod
    def gastar_dinherio(self):
        pass

    @abstractclassmethod
    def respirar(self):
        pass

    @abstractclassmethod
    def falar(self):
        pass


class Atleta(PessoaAbstrata):
    def gastar_dinheiro():
        print(f'Eu gasto pouco dinheiro')

    def falar():
        print('Queremos um aumento')



class Artista(PessoaAbstrata):
    def gastar_dinheiro():
        print(f'Eu gasto muito dinheiro porque eu posso')

    def falar():
        print('Eu sou rico e falo 5 idiomas')


        


Artista.gastar_dinheiro()
Atleta.gastar_dinheiro()        
Atleta.falar()
