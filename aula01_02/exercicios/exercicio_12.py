# Exercício 12:
#Crie uma função que solicite ao usuário que insira uma sequência de números inteiros
#separados por espaço e,em seguida, calcule e exiba a média desses números.
#Utilize listas para armazenar os números digitados pelo usuário
#e um for loop para calcular a soma dos elementos da lista.

import os

def obter_numero():
    lista = []
    lista_numeros_inteiros = []
    while True:
        try:
            numero =input('Digite um numero inteiro: ')
            lista = numero.split(' ')
            for val in lista:
                lista_numeros_inteiros.append(int(val))
            return lista_numeros_inteiros
        except Exception as e:
            print(f'Valor invalido!! {e}')

def calculos_lista(lista_numeros_inteiros):
    soma_itens = 0
    media = 0
    for item in lista_numeros_inteiros:
        soma_itens += item
    media = soma_itens / len(lista_numeros_inteiros)
    return soma_itens, media


def exibir_resultados(soma_itens, media):

    print(
        f'-' *50 +
        f'\nA SOMA dos valores inseridos na lista = {soma_itens}\n'+
        f'-' *50 +
        f'\nA MEDIA dos valores inseridos na lista = {media}\n'+
        f'-' *50
    )


def main():
    lista_numeros_inteiros = obter_numero()
    soma_itens, media = calculos_lista(lista_numeros_inteiros)
    exibir_resultados(soma_itens, media)
    #obter_numero()


if __name__ =='__main__':
    os.system('clear')
    main()