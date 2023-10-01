from conta import Conta

class PessoaJuridica(Conta):
    __Segundo_Titular = ' '
    def __init__(self, titular, cnpj, saldo):
        super().__init__(1610, 'Pessoa Juridica')
        self.__Titular = titular
        self.__Cnpj = cnpj
        self.__Saldo = saldo

    @property
    def Segundo_Titular(self):
        return self.__Segundo_Titular
    @Segundo_Titular.setter
    def Segundo_Titular(self, segundo_titular):
        self.__Segundo_Titular = segundo_titular
        
    @property
    def titular(self):
        return self.__Titular
    @titular.setter
    def titular(self, titular):
        self.__Titular = titular

    @property
    def cnpj(self):
        return self.__Cnpj
    @cnpj.setter
    def cpf(self, cnpj):
        self.__Cnpj = cnpj

    @property
    def saldo(self):
        return self.__Saldo
    @saldo.setter
    def saldo(self, saldo):
        if saldo > 0:
            self.__Saldo = saldo
        else:
            print('Saldo inexistente')

    def __str__(self):
        return f'\nConta: {super().__str__()}\nNome Titular: {self.titular}\nCnpj empresa: {self.cnpj}\nSaldo conta: R$ {self.saldo}\nSegundo Titular: {self.Segundo_Titular}'