# Exercício 15:
#Dado um número inteiro positivo N, 
#Crie uma função que calcule a soma de todos os números ímpares de 1 até N.
#Utilize um for loop para iterar pelos números e um operador de módulo (%)
#para verificar se o número é ímpar.

import os

def obter_numero():
    while True:
        try:
            numero =int(input('Digite um numero inteiro: '))
            return numero
            
        except Exception as e:
            print(
                f'='*50 +
                f'\nValor invalido!! {e}\n'+
                f'='*50
            )


def listar_numeros_impares(numero):
    for n in range(0,numero,1):
        if not n %2==0:
            print(f'\n{n}',end="")

def soma_numeros_impares(numero):
    soma_impares = 0
    for n in range(1,numero, 1):
        if not n %2==0:
            soma_impares += n
    return soma_impares


def exibir_lista_numeros_impares(numero, soma_impares):
    lista_numeros_impares = []
    for n in range(0,numero,1):
        if not n %2==0:
            lista_numeros_impares.append(n)
    print(
        f'-' *50 +
        f'\nOs numeros impares encontrados ate o numero digitado "({numero})" sao: {lista_numeros_impares}\n'+
        f'-' *50 +
        f'\nA soma dos numeros impares ->  {soma_impares}\n'+
        f'-' *50 
    )


def main():
    numero = obter_numero()
    #listar_numeros_impares(numero)
    soma_impares = soma_numeros_impares(numero)
    exibir_lista_numeros_impares(numero, soma_impares)


if __name__ =='__main__':
    os.system('clear')
    main()