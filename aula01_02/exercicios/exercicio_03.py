#Crie uma função que peça ao usuário que digite um número inteiro e, em seguida,
#armazene esse valor em uma variável. Crie mais funções para o usuário também informar 
#dados do tipo float e string, e armazene todos os dados em variáveis. Em seguida
#adicione todos esses items em uma lista e mostre os item através de um laço de repetição for. 


import os

def exibir_inteiro():

    while True:
        numero_inteiro = input('Digite numero inteiro ou s para sair: ').lower()
        if numero_inteiro == 's':
            break

        #if numero_inteiro.isdigit():
        #    print('Voce digitou um numero inteiro, obrigado')
        #    break
        try:
            numero_inteiro == int(numero_inteiro)
            lista.append(numero_inteiro)
        except:
            print('Numero invalido, favor digitar numero inteiro!!')


def exibir_float():

    while True:
        numero_float = (input('Digite um numero float ou s para sair: '))
        if numero_float.lower() == 's':
            break
        try:
            numero_float = float(numero_float)
            lista.append(numero_float)
        except:
            print('Numero invalido, favor digitar numero Float!!')


def exibir_string():
    while True:
        palavra = input('Digite uma palavra ou s para sair: ').lower()
        if palavra == 's':
            break

        #if palavra.isdigit():
        #   print('Voce digitou uma palavra, obrigado')
        #    break
        try:
            palavra == str(palavra)
            lista.append(palavra)
        except:
            print('Valor invalido, favor digitar uma palavra!!')

def exibir_lista():
    for item in lista:
        print(item)

    

if __name__ =='__main__':
    os.system('clear')
    lista = []
    exibir_inteiro()
    exibir_float()
    exibir_string()
    print(lista)
    exibir_lista()

    #fazer lista com as variaveis e depiois um for para imprimir 