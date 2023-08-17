#2 - Crie uma classe Banco com métodos abstratos depositar(), ver_saldo() e sacar() e 
#    implemente a lógica de cada método. Crie subclasses ContaCorrente e ContaPoupanca
#    que herdam da classe Banco e implementam os métodos de acordo com suas regras específicas.
#    Por exemplo, a subclasse ContaPoupanca pode nao deter o método sacar().
#    Crie atributos privados e publicos nas subclasses ContaCorrente e ContaPoupanca
#    como self.nome, self.saldo, e self.numero_conta por exemplo. Crie objetos dessas
#    classes com informações distintas, invoque os métodos e printe o resultado das operações. 

from abc import ABC, abstractmethod

class Banco(ABC):

    def __init__(self, nome, saldo, numero_conta):
        self.nome = nome
        self.__saldo = saldo
        self._numero_conta = numero_conta


    @abstractmethod
    def depositar(self):
        pass

    @abstractmethod    
    def saldo(self):
        pass

    @abstractmethod
    def sacar(self):
        pass


class ContaCorrente(Banco):

    
    def depositar(self, deposito):
        if deposito >0:
            self._Banco__saldo += deposito
            print('valor depositado na sua conta')
        else:
            print('Informe um deposito maoir que zero')

    @property
    def saldo(self):
        return self._Banco__saldo

    def sacar(self, valor_a_sacar):
        self._Banco__saldo -= valor_a_sacar
        print(f'saque de R$ {self.valor_a_sacar} foi realizado com sucesso')


    
class ContaPoupanca(Banco):
    
    def depositar(self, deposito):
        if deposito >0:
            self._Banco__saldo += deposito
            print('valor depositado na sua conta')
        else:
            print('Informe um deposito maoir que zero')

    @property
    def saldo(self):
        return self._Banco__saldo

    def sacar(self):
        print('\nPrezado cliente em conta poupanca nao eh possivel sacar\n')
 



titular_poupanca_01 = ContaPoupanca(
    nome='Carlos', 
    saldo=5000.00, 
    numero_conta='12345-8'
)
titular_poupanca_02 = ContaPoupanca(
    nome='Arthur', 
    saldo=2500.00, 
    numero_conta='14723-9'
)

titular_01 = ContaCorrente(
    nome='Joao', 
    saldo=5000.00, 
    numero_conta='12345-8'
)
titular_02 = ContaCorrente(
    nome='Ana', 
    saldo=2500.00, 
    numero_conta="14723-9"
)

print(titular_poupanca_01.saldo())
print(titular_poupanca_02.saldo())
#titular_poupanca_01.sacar()

print('-'*30)

#titular_01.saldo()
#titular_02.saldo()
#titular_01.sacar()




