class Triangulo:
    def __init__(self,lado1, lado2, lado3):
        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3
        print('Obejto instanciado com sucesso')


def eh_valido(self):
    lado1_valido = self._lado3 + self._lado2 > self._lado1
    lado2_valido = self._lado1 + self._lado3 > self._lado2
    lado3_valido = self._lado1 + self._lado2 > self._lado3

    return lado1_valido is True and lado2_valido is True and lado3_valido is True

def calcula_perimetro(self):
    return self._lado1 + self._lado2 + self._lado3

def tipo_triangulo(self):
    if (self._lado)


triangulo_1 = Triangulo(lado1=3.5, lado2=5.5, lado3=8.5)
triangulo_2 = Triangulo(lado1=3, lado2=6, lado3=9)

print(f'Triangulo_1 eh valido: {triangulo_1.eh_valido()}')
print(f'Triangulo_2 eh valido: {triangulo_2.eh_valido()}')

print(f'Triangulo_1 perimetro: {triangulo_1.calcular_perimetro()}')
print(f'Triangulo_2 perimetro: {triangulo_2.calcular_perimetro()}')
        