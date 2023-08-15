# Exercício 18:
#Crie um programa que solicite ao usuário que insira a quantidade de notas do aluno a serem calculadas.
#Em seguida, peça para o usuário digitar as notas uma por uma. Armazene essas notas em uma lista.
#Calcule a média das notas utilizando um for loop para somar todos os elementos da lista 
#e dividir pela quantidade de notas.
#Verifique se a média é maior ou igual a 6.0.
#Se a média for maior ou igual a 6.0, exiba a mensagem "Aluno Aprovado!".
#Caso contrário, exiba a mensagem "Aluno Reprovado!".

import os


def ler_quantidade_notas():
    while True:
        try:
            quantidade_notas = int(input('Informe quantidade de notas: '))

            if quantidade_notas >0:
                return quantidade_notas
            else:
                raise ValueError('Informe numeros acima de zero! ')
            
        except Exception as e:
            print(f'Ocorreu um erro: str{e}')
            print('Informe uma quantidade valida!!')




def ler_notas(quantidade_notas):
    lista_notas = []
    while len(lista_notas) < quantidade_notas:
        try:
            nota = float(input(f'Informe a {len(lista_notas)+1 }॰ nota: '))
            if nota >=0 and nota <= 10:
                lista_notas.append(nota)


        except Exception as e:
            print(f'Ocorreu um erro: str{e}')
            print('Informe uma nota valida!!')



def calcula_media(lista_notas):
    for nota in lista_notas:
        soma  +=nota

    return soma / len(lista_notas)


def verificar_media(media):
    if media >= 6:
        print(f'O aluno foi aprovado com media: {media}')
    else:
        print(f'O aluno foi reprovado com media: {media}')
wwww


def main():
    #print(ler_quantidade_notas())
    quantidade_notas = ler_quantidade_notas()
    ler_notas(quantidade_notas)
    media = calcula_media
    verificar_media(media)


if __name__ =='__main__':
    os.system('clear')
    main()