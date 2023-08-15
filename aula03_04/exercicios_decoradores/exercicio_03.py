#3- - Classe Conta Bancária:
#Crie uma classe chamada ContaBancaria, com os atributos 
#saldo (private), titular (public), numero_conta (private). 
#Crie métodos get_saldo() eset_saldo(novo_saldo) para acessar e modificar o saldo.

class ContaBancaria:
    def __init__(self, saldo, numero_conta, titular):
        self._saldo = saldo
        self._numero_conta = numero_conta
        self.titular = titular

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo_novo):
        self._saldo = saldo_novo



    
if __name__=='__main__':

    conta_1 = ContaBancaria( 100, 15, 'bruno')
    conta_2 = ContaBancaria(200, 15, 'ana')


    print(conta_1.titular)
    print(conta_1.saldo)

    print(conta_2.titular)
    print(conta_2.saldo)
    print('\n')
    conta_1.saldo = 500
    conta_2.saldo = 600
    print('\nnovos valores setados\n')
    print(conta_1.titular)
    print(conta_1.saldo)
    print(conta_2.titular)
    print(conta_2.saldo)


