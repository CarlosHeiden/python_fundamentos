# Exercício 14:
#Crie uma função que remova as duplicatas de uma lista de números. 
#Por exemplo, se a lista for [1, 2, 2, 3, 4, 4, 5],
#o programa deve retornar a lista sem duplicatas: [1, 2, 3, 4, 5]. 
#Utilize listas e um for loop para percorrer a lista 
#original e uma nova lista para armazenar os elementos únicos.

import os

lista = []
nova_lista = []

def inserir_valores_lista():
    while True:
        try:
            valores = int(input('Digite os números para inserir na lista: '))
            lista.append(valores)
            print(lista)
            encerrar = input('Deseja continuar digite "ENTER" ou digite "s" para sair!!')
            if encerrar.lower() == 's':
                break
            
            #return lista
            
        except ValueError:
            print('Valor inválido! Certifique-se de digitar apenas números.')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

def remover_duplicatas(lista):
    nova_lista = []
    for numero in lista:
        if numero not in nova_lista:
            nova_lista.append(numero)
    nova_lista.sort()   # Ordena lista em ordem crescente
    return nova_lista

def exibir_listas(lista, nova_lista):
    print(
        f'-'*50+
        f'\nlista com valores duplicados: {lista}\n'+
        f'-'*50+
        f'\nNova lista sem valores duplicados: {nova_lista}\n'+
        f'='*50
    )
    
def main():
    inserir_valores_lista()
    nova_lista = remover_duplicatas(lista)
    exibir_listas(lista, nova_lista)

if __name__ =='__main__':
    os.system('clear')
    main()