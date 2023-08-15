#2 - Crie uma classe Banco com métodos abstratos depositar(), ver_saldo() e sacar() e 
#    implemente a lógica de cada método. Crie subclasses ContaCorrente e ContaPoupanca
#    que herdam da classe Banco e implementam os métodos de acordo com suas regras específicas.
#    Por exemplo, a subclasse ContaPoupanca pode nao deter o método sacar().
#    Crie atributos privados e publicos nas subclasses ContaCorrente e ContaPoupanca
#    como self.nome, self.saldo, e self.numero_conta por exemplo. Crie objetos dessas
#    classes com informações distintas, invoque os métodos e printe o resultado das operações. 

from abc import ABC, abstractmethod

class Banco(ABC):



    @abstractmethod
    def depositar(self):
        pass

    @abstractmethod    
    def ver_saldo(self):
        pass

    @abstractmethod
    def sacar(self):
        pass


class ContaCorrente(Banco):

    def __init__(self, nome, saldo, numero_conta):
        self.__nome = nome
        self.__saldo = saldo
        self.numero_conta = numero_conta

    def depositar(self):
        print('valor depositado na sua conta')

    def ver_saldo(self):
        print('seu saldo eh positivo')

    def sacar(self):
        print('um valor foi sacado da sua conta')


    
class ContaPoupanca(Banco):
    def __init__(self, nome, saldo, numero_conta):
        self.__nome = nome
        self.__saldo = saldo
        self.numero_conta = numero_conta

    def depositar(self):
        print('valor depositado na sua conta')

    def ver_saldo(self):
        print('seu saldo eh positivo')

    def sacar(self):
        print('em conta poupanca nao eh possivel sacar')
 


    