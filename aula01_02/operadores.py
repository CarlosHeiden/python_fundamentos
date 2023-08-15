import os


def verificar_numeros():
    try:
        numero_um = int(input('Informe um numero: '))
        numero_dois = int(input('Informe um numero: '))

        if numero_um > 0 and numero_dois > 0:
            if numero_um > numero_dois:
                print('Primeiro numero eh maior que o segundo numero')
            elif numero_um < numero_dois:
                print('Primeiro numero eh menor que o segundo numero ')
            elif numero_um == numero_dois:
                print('NUmeros sao iguais')
        else:
            print('Numeros precisam ser positivos')

    except:
        print('Erro ao tentar converter numero para float')

def verifica_idade():

    try:
        idade_usuario = int(input('Informe sua idade: '))
        if idade_usuario >0 and idade_usuario <120:
            #Verificar se ewh adulto  maior de 18 anos
            if idade_usuario >= 18:
                print('Voce eh adulto')
            elif idade_usuario >= 12 and idade_usuario < 18:
                print('Voce eh um teen')
            elif idade_usuario < 12:
                print('Voce eh uma crianca')
        else:
            pass


    except:
        print('Erro ao ler os dados')



if __name__ =='__main__':
    os.system('clear')
    os.system('python --version')
    verifica_idade()


    