
#class mae
class Animal:

    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def correr(self):
        print(f'{self.nome} esta correndo')

    def comer(self):
        print(f'{self.nome} esta comendo')


# subclass herdando class Animal
class Cachorro(Animal):
    
    def latir(self):
        print(f'au au , eu sou um cachorro!!')

class Gato(Animal):

    def destruir_sofa(self):
        print(f'\nSeu sofa foi destruido em protesto a sua viagem\n')

    def miar(self):
        print(f'miauuuu, miauuuu')


cao_1 = Cachorro('Gibs', 'black')
cao_1.comer()
cao_1.correr()
cao_1.latir()

gato_1 = Gato('Mini', 'white')
gato_1.comer()
gato_1.correr()
gato_1.miar()
