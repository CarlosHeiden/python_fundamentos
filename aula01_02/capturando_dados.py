import os


def captura_dados():

    #lendo dados do usuarios

    texto_usuario = input('Informe um numero: ')
    print('voce escreveu => ', texto_usuario)
    print( type(texto_usuario))


    inteiro_usuario = input('Informe um numero: ')
    print('Voce infomormou => ', inteiro_usuario)
    print(type(inteiro_usuario))


    #Convertendo strings para numeros inteiros

    inteiro_usuario = input('Informe um numero: ')
    

    # try para tentar executar e nao parar se der erro

    try:
        inteiro_usuario = int(inteiro_usuario)
    except:
        print('Erro ao tentar converter numero para float')

    
    # Convertendo strings para numeros quebrados

    float_usuario = input('Informe numero float: ')

    try:
        float_usuario = float(float_usuario)
    except:
        print('Erro ao tentar converter numero para float')


    print('Voce digitou => ', float_usuario)
    print(type(float_usuario))

if __name__ =='__main__':
    os.system('clear')

    captura_dados()
    











