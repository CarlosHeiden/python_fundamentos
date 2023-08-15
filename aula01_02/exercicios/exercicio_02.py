#Escreva uma função que calcule a média de três notas fornecidas pelo usuário e
	#armazene o resultado em uma variável. Em seguida, exiba a média calculada no terminal.

import os

def calcula_nota():
    soma_nota = 0
    for i in range(3):
        nota= float(input('Informe a nota: '))
        if nota >0 and nota <=10:
            soma_nota += nota
    media = soma_nota/3
    print(f'A media da notas informadas eh: {media}')


def recebe_dados():
    lista_notas = []

    while len(lista_notas) <3 :
        try:
            nota = float(input('Digite uma nota: '))
            if nota > 0 and nota <= 10:
                lista_notas.append(nota)
                print('Adicionou nota com sucesso')

        except:
            print('Informe uma nota valida!')

    return lista_notas

def calcula_media(lista_notas):
    soma_notas = 0
    for nota in lista_notas:
        soma_notas +=nota
    media_notas = soma_notas/len(lista_notas)
    return media_notas

def mostrar_resultado(calcula_media):
    print(f'A media das notas eh: {calcula_media}')

    



if __name__ =='__main__':
    os.system('clear')
    
    #calcula_nota()
    recebe_dados()

