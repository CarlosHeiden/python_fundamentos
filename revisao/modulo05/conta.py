class Conta:
    def __init__(self, numero, tipo):
        self.Numero = numero
        self.Tipo = tipo

    def __str__(self) -> str:
        return f'{self.Numero} {self.Tipo}'
        