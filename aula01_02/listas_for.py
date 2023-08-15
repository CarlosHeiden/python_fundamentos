import os

def mostrar_lista():

    lista_dados= [
        1,
        2,
        3,
        'hello',
        'hi',
        False,
        True,
        1,5,
        20,
        'Texto!!!'
    ]
    for item in lista_dados:
        print(item)


def obter_mostrar_dados():
    lista_input= []
    for i in range(5):
        item = input(f'Informe o {i +1} item: ')
        lista_input.append(item)

    print('\nItens informados pelo usuario: ')
    for item in lista_input:
        print(item)

def script_lista():
    lista_dados= []
    contador = 0

    #receber 10 itens do ususario
    while contador <10:
        contador +=1
        item_informado = input('Informe o {contador} Item: ')
        lista_dados.append(item_informado)


    #mostrar itens recebidos
    #acessando tambem os indices / posicoes
    for indice, item in enumerate(lista_dados):
        print(f'Posicao {indice} - Valor {item}')



    # loop para o usuario acessar itens especificos da lista

    while True:
        try:
            posicao_item = int(input('Informe a posicao do item desejado: '))
            print(f'O item que esta na posicao {posicao_item} eh: {lista_dados[posicao_item]}')
            verificacao = input('Informe s para sair ou entre para continuar: ').lower()
            if verificacao == 's':
                break
        except:
            print('Informe apenas numeros interios para posicoes em listas!!!')
   

if __name__ =='__main__':
    os.system('clear')
    #mostrar_lista()
    #obter_mostrar_dados()
    script_lista()


    