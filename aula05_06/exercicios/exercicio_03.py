#3 - Crie uma classe base Veiculo com atributos como marca, modelo
#e métodos como ligar()e desligar(), entre outros. 
#Crie as subclasses Carro e Moto que herdam de Veiculo e implementam 
#seus próprios métodos beaseando-se na abstratação de Veiculo. 
#Em seguida,crie uma classe Garagem que aceita veículos e 
#gerencia o estacionamento usando herança.
#Crie e trabalhe com os getters e setters para a classe Garagem.
from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self. marca = marca
        self.modelo = modelo

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
      pass

    @abstractmethod
    def acelerar(self):
        pass
    
    @abstractmethod
    def desacelerar(self):
        pass

    @abstractmethod
    def parar(self):
        pass
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor , ano):
        super().__init__(marca, modelo)

        self.cor = cor
        self.ano = ano

    def ligar(self):
        print(f'veiculo modelo: {self.modelo} e ano: {self.ano} esta ligado.')

    def desligar(self):
      print(f'veiculo modelo: {self.modelo} e ano: {self.ano} esta ligado.')

    def acelerar(self):
        print(
            f'o veiculo marca: {self.marca}, modelo : {self.modelo} esta acelerando.'
        )
    
    def desacelerar(self):
        print(f'o veiculo modelo: {self.modelo} na cor: {self.cor} esta diminuindo velociadade.')

    def parar(self):
        print(
            f'o veiculo marca: {self.marca}, modelo: {self.modelo}, cor: {self.cor}\n'+
            f'e ano: {self.ano} parou!!'
        )


class Moto(Carro):

    def empinando_moto(self):
        print(f'a moto marca {self.marca}, modelo {self.modelo} na cor {self.cor} esta empiando na rodovia')

class Garagem(Carro):

    def __init__(self, marca, modelo, cor, ano, numero_vaga):
        super().__init__(marca, modelo, cor, ano)
        self.numero_vaga = numero_vaga

    def estacionado(self):
        print(
            f'o veiculo marca: {self.marca}, modelo: {self.modelo}, cor: {self.cor}\n'+
            f'e ano: {self.ano} ESTACIONOU na vaga numero: {self.numero_vaga}.'
        )

    @property
    def numero_vaga(self):
        print('GET numero_vaga')
        return self.__numero_vaga

    @numero_vaga.setter
    def numero_vaga(self,valor):
        self.__numero_vaga = valor.replace('-', '/')
        print('SETTER vaga')



if __name__=='__main__':

    carro_1 = Carro('GM', 'Omega', 'preto', 1992)
    moto_1 = Moto('Honda', 'crf-450', 'vermelha', 2022)
    carro_2 = Garagem('BMW', 'X1', 'prata', 2022, '22-A')
    print(moto_1.acelerar())
    print(moto_1.desacelerar())
    print(moto_1.empinando_moto())
    print(moto_1.parar())
    print('-'*30)
    print(carro_2.ligar())
    print(carro_2.parar())
    carro_2.estacionado()
    print('-'*30)
    carro_2.estacionado()