from conta_01 import Conta

class PessoaFisica(Conta):
    __Segundo_Titular = ' '

    def __init__(self, titular, cpf, saldo):
        super().__init__(1609, 'Pessoa Fisica')

        self.__Titular      = titular
        self.__Cpf          = cpf
        self.__Saldo        = saldo

    @property
    def Segundo_Titular(self):
        return self.__Segundo_Titular
    
    @property
    def 