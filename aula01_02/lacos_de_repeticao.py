import os
from operadores import verifica_idade, verificar_numeros


def script_idade():
    while True:
        verifica_idade()
        verificacao = input('Informe s para sair ou entre para continuar: ').lower()

        if verificacao == 's':
            break


def script_numero(limite_loop):

    contador = 0
    while contador < limite_loop:
        contador += 1
        verificar_numeros()

    print(f'O loop rodou {limite_loop} vezes!')

if __name__ =='__main__':
    os.system('clear')
    #script_idade()
    limite_loop = int(input('Informe quantas vezes o programa deve rodar: '))
    script_numero(limite_loop)