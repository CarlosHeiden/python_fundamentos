# Exercício 11:
#Dado um número inteiro positivo N, 
#crie uma função que exiba todos os números pares de 0 até N(inclusive).
#Utilize um for loop para iterar pelos números e um operador de módulo (%)
#para verificar se o número é par.

import os

def obter_numero():
    while True:
        try:
            numero =int(input('Digite um numero inteiro: '))
            return numero
            
        except Exception as e:
            print(f'Valor invalido!! {e}')


def listar_numeros_pares(numero):
    for n in range(0,numero,1):
        if n %2==0:
            print(f'\n{n}',end="")


def exibir_lista_numeros_pares(numero):
    lista_pares = []
    for n in range(0,numero,1):
        if n %2==0:
            lista_pares.append(n)
    print(f'\n\nOs numeros pares encontrados ate o numero digitado sao: {lista_pares}')


def main():
    numero = obter_numero()
    listar_numeros_pares(numero)
    exibir_lista_numeros_pares(numero)


if __name__ =='__main__':
    os.system('clear')
    main()