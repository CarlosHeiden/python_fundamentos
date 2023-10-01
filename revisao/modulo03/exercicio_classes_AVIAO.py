class Aviao:
    __Modelo = 'Carga'
    def __init__(self, tipo, capacidade_carga, autonomia, tripulacao):
        self.__Tipo:   str = tipo
        self.__Capacidade_carga   :   float = capacidade_carga   # qtd em toneladas
        self.__Autonomia     :   float   = autonomia      # qtd km
        self.__Tripulacao     :   float   = tripulacao      #qtd pessoas

    @property
    def modelo(self):
        return self.modelo
    
    @property
    def tipo(self):
        return self.__Tipo
    @tipo.setter
    def tipo(self, tipo):
        self.__Tipo = tipo

    @property
    def capacidade_carga(self):
        return self.__Capacidade_carga
    @capacidade_carga.setter
    def capacidade_carga(self, capacidade_carga):
        self.__Capacidade_carga = capacidade_carga

    @property
    def autonomia(self):
        return self.__Autonomia
    @autonomia.setter
    def autonomia(self, autonomia):
        self.__Autonomia = autonomia

    @property
    def tripulacao(self):
        return self.__Tripulacao
    @tripulacao.setter
    def tripulacao(self, tripulacao):
        self.__Tripulacao = tripulacao


    def __str__(self):
        return f'{self.tipo} {self.capacidade_carga} {self.autonomia} {self.tripulacao}'
    