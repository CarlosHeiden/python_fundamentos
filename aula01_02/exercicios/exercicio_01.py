#Escreva uma função que solicite ao usuário que insira seu nome e, em seguida,
	#armazene esse valor em uma variável. Em seguida, exiba uma mensagem de boas-vindas
	#usando o nome digitado.

import os

def boas_vindas():

    nome = input('Informe seu nome: ')
    print(f'Seja bem vindo Sr(a). {nome}')
        

if __name__ =='__main__':
    os.system('clear')
    boas_vindas()



   
        
    

