# Exercício 17:
#Crie uma função que receba uma lista de palavras
#e um determinado caractere. O programa deve exibir todas as
#palavras que contêm o caractere	fornecido pelo usuário. 
#Utilize listas, for loops e operadores para realizar a busca.

import os


def inserir_letra_comparacao():
    letra = input('Digite o caracter para comparacao: ')
    print(letra)
    return letra

def inserir_palavras_lista():
    lista_palavras = []
    while True:
        try:
            palavras = input('Digite as palavras para inserir na lista: ')
            lista_palavras.append(palavras)
            
            print(lista_palavras)
            encerrar = input('Deseja continuar digite "ENTER" ou digite "s" para sair!!  ')
            if encerrar.lower() == 's':
                break
        except ValueError:
            print('Valor inválido! Certifique-se de digitar apenas PALAVRAS!!!.')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')
    
    return lista_palavras

def procurando_letra(letra, lista_palavras):
    lista_com_letra = []
    for palavra in lista_palavras:
        if letra == palavra:
            lista_com_letra.append(palavra)
    print(lista_com_letra)


def buscar_palavras(letra, lista_palavras):
    palavras_encontradas = []
    for palavra in lista_palavras:
        for val in palavra:
            print(val, end=' ')
            if letra in palavra:
                palavras_encontradas.append(palavra)
    #return palavras_encontradas
    print(palavra)
    print(palavras_encontradas)


def printar_palavras_com_letra(lista_palavras, letra):
    for palavra in lista_palavras:
        if letra in palavra:
            print(f'Palavra {palavra} tem letra {letra}')
    
def main():
    letra = inserir_letra_comparacao()
    lista_palavras = inserir_palavras_lista()
    # procurando_letra(letra, lista_palavras)
    # buscar_palavras(letra, lista_palavras)
    printar_palavras_com_letra(lista_palavras, letra)

if __name__ =='__main__':
    os.system('clear')
    main()
