class Conta:
    __Numero = 123

    def __init__(self,titular, cpf, saldo, limite):
        self.__Titular: str = titular
        self.__Cpf: str = cpf
        self. __Saldo: float = saldo
        self.__Limite: float = limite

        



    def __str__(self):
        return f'{self.Numero} {self.Titular} {self.Cpf} {self.Saldo} {self.Limite}'
    


        