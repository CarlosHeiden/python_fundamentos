#5 - Classe Triângulo:
#Crie uma classe chamada Triangulo que represente um triângulo. 
#A classe deve ter os atributos lado1, lado2 e lado3.
#Crie métodos para verificar se os lados formam um triângulo válido (eh_valido()),
#calcular o perímetro (calcular_perimetro())
#e exibir o tipo do triângulo com base nos lados (tipo_triangulo()).
import os
class Triangulo:

    
    def eh_valido():
        while True:
            try:
                lado1 = float(input('Informe o valor do lado1 do triangulo: '))
                lado2 = float(input('Informe o valor do lado2 do triangulo: '))
                lado3 = float(input('Informe o valor do lado3 do triangulo: '))
                break

            except Exception as e:
                print(f'Valor invalido, digite valores validos!!! {e}')
        return lado1, lado2, lado3
        

    def calcular_perimetro(lado1, lado2, lado3):
        perimetro = lado1 + lado2 + lado3
        return perimetro
        

    def tipo_triangulo(lado1, lado2, lado3):
        if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            tipo_triangulo = '"ESCALENO"'
            texto = 'TODOS os lados tem medidas DIFERENTES.'
        elif lado1 == lado2  and lado2 == lado3:
            tipo_triangulo = '"EQUILATERO" '
            texto = 'TODOS lados tem medidas IGUAIS.' 
        else:
            tipo_triangulo = '"ISOSCELES"'
            texto = '2 lados tem medidas iguais.'
        

        return tipo_triangulo, texto

    def exibir_resultados(perimetro, tipo_triangulo, texto):
        print(
                f'Pelas medidas informadas este eh um triangulo {tipo_triangulo},\n'+
                f'{texto},\n'+
                f'o perimetro deste triangulo eh: {perimetro}'
            )
    
    def script():
        lado1, lado2, lado3 = Triangulo.eh_valido()
        perimetro = Triangulo.calcular_perimetro(lado1, lado2, lado3)
        tipo_triangulo, texto = Triangulo.tipo_triangulo(lado1, lado2, lado3)
        Triangulo.exibir_resultados(perimetro, tipo_triangulo, texto)
    
if __name__=='__main__':
    os.system('clear')
    Triangulo.script()