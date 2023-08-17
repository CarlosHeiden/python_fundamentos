#5 - Crie uma classe Alimento com atributos como nome e calorias. 
#Crie subclasses Fruta, Legumee Carne que herdam de Alimento e 
#implementam seus próprios atributos. 
#Crie uma função que aceita uma lista de alimentos e calcula o total de calorias 
#usando polimorfismo. Para mais precisão no exercício, 
#é ideal pesquisar as calorias dos alimentos e 
#criar objetos das subclasses com seus respectivos construtores e atributos.

from abc import ABC , abstractclassmethod

class Alimento(ABC):

    def __init__(self, calorias, nome):
        self.calorias = calorias
        self.nome = nome



class Fruta(Alimento):
    pass

class Carne(Alimento):
    pass

class Legume(Alimento):
    pass

def calcula_calorias(lista_calorias):
    soma_calorias = 0
    for caloria in lista_calorias:
        soma_calorias += caloria

    return soma_calorias




cenoura = Legume(5, 'cenoura')
vagem = Legume(10 , 'vagem')
beterraba = Legume(20, 'beterraba')

lista_legumas = [
    cenoura.calorias,
    vagem.calorias,
    beterraba.calorias
]

calorias_total_legumes = calcula_calorias(lista_legumas)

print(f'A soma de calorias de {cenoura.nome}, ', end=' ')
print(f'da {vagem.nome} e da {beterraba} eh igual {calcula_calorias}')


frango = Carne(100, 'file de frango')
bife = Carne(150, 'Patinho')
picanha = Carne(200, 'Picanha')

banana = Fruta(50, 'Banana')
melancia = Fruta(20, 'Melancia')
maracuja = Fruta(10, 'Maracuja')
