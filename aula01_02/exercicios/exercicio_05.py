#Crie uma função que exiba uma mensagem perguntando a idade do usuário e, 
#com base na idade fornecida,
#exiba diferentes mensagens de acordo com as seguintes faixas etárias: 
#0-12 anos, 13-17 anos, 18 ou mais anos.
#(mais faixas etárias podem ser incluídas)

import os

def faixa_etaria():
    while True:
            try:
                idade = int(input('Digite sua idade ou s para sair: '))
                break
            except ValueError:
                print('Valor invalido, favor digitar numero inteiro!!')

    if idade > 0 and idade < 120:
        if idade < 13:
            print(f'Voce tem {idade} anos, pela sua idade voce eh considerado uma crianca')
        elif idade >= 13 and idade <= 17:
            print(f'Voce tem {idade} anos, pela sua idade voce eh considerado um adolescente')
        else:
            print(f'Voce tem {idade} anos, pela sua idade voce eh considerado um adulto')
    else:
        print(f'Digite uma idade valida, voce digitou: {idade}')
    

if __name__ =='__main__':
    os.system('clear')
    faixa_etaria()