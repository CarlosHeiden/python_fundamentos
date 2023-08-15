#
#Crie uma função que converta um valor em dólar para real.
#Peça ao usuário que insira a cotação do dólar e o valor em dólar a ser convertido.
#Em seguida, exiba o valor equivalente em reais.

import os

def obter_dados():

    verificacao = False
    while verificacao ==False:
        try:
            cotacao_dolar =float(input('Digite a cotacao do dolar ou 0 para sair: '))
            quantidade_dolar= float(input(
                f'Digite a quantidade de dolares que ' +
                f' deseja converter para real: ')
            )
            if cotacao_dolar == 0:
                 verificacao = True
        except ValueError:
                print(f'Valor invalido!! voce digitou {cotacao_dolar} / {quantidade_dolar}')
        return cotacao_dolar, quantidade_dolar

def converter_dolar_real(cotacao_dolar, quantidade_dolar):

    resultado = cotacao_dolar * quantidade_dolar

    return resultado


def exibir_resultado(resultado):
    print(f'O resultado da conversao para real dos valores inforados => R$ {resultado:.2f} reais')


def faz_tudo():
    verificacao = False
    while verificacao ==False:
        try:
            cotacao_dolar =float(input('Digite a cotacao do dolar ou 0 para sair: '))
            if cotacao_dolar == 0:
                 verificacao = True
            else:
                quantidade_dolar= float(input(
                    f'Digite a quantidade de dolares que ' +
                    f' deseja converter para real: ')
                )
                resultado = cotacao_dolar * quantidade_dolar
                print(
                     f'O resultado da conversao para real dos valores inforados => R$ {resultado:.2f} reais\n' + 
                     f'='*70
                )
                print('='*70)  


        except Exception as erro_ocorrido:
                print(f'Erro {erro_ocorrido}\Valor invalido!! voce digitou {cotacao_dolar} / {quantidade_dolar}')


def main():
    #cotacao_dolar, quantidade_dolar = obter_dados()
    #resultado = converter_dolar_real(cotacao_dolar, quantidade_dolar)
    #exibir_resultado(resultado)
    faz_tudo()



if __name__ == '__main__':
    os.system('clear')
    main()
