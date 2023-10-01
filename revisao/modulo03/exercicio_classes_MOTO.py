class Moto:
    __Modelo = 'Turismo'
    def __init__(self, potencia, cilincrada, cor, cambio):
        self.__Potencia   :   float = potencia
        self.__Cilindrada :   float = cilincrada
        self.__Cor        :   str   = cor
        self.__Cambio     :   str   = cambio

    @property
    def modelo(self):
        return self.__Modelo
    
    @property
    def potencia(self):
        return self.__Potencia
    @potencia.setter
    def potencia(self, potencia):
        self.__Potencia = potencia

    @property
    def cilindrada(self):
        return self.__Cilindrada
    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self.__Cilindrada = cilindrada

    @property
    def cor(self):
        return self.__Cor
    @cor.setter
    def cor(self, cor):
        self.__Cor = cor

    @property
    def cambio(self):
        return self.__Cambio
    @cambio.setter
    def cambio(self, cambio):
        self.__Cambio = cambio


    def __str__(self):
        return f'{self.potencia} {self.cilindrada} {self.cor} {self.cambio}'
        
