#Crie uma função que solicite ao usuário que insira seu endereço completo
#(incluindo rua, número, bairro, cidade e CEP
#e armazene as informações em variáveis separadas. Depois mostre essas 	 
#informações usando concatenação com uma mensagem.

import os

def endereco_usuario():
    try:
        nome = input('Digite seu nome: ')
        rua = input('Digite rua em que reside: ')
        numero = input('Digite o numero da casa: ')
        bairro = input('Digite o bairro:')
        cidade = input('Digite a cidade: ')
        cep = input('Digite o cep: ')
        print(
            '\nPor favor confira seus dados:' +
            f'\nNome: {nome}\nRua: {rua}\nNumero:' + 
            f'{numero}\nBairro: {bairro}\nCidade: {cidade}\nCEP: {cep}'
        )
        
        print(f'')
    except:
        print('Valor invalido, digite novamente!!!')


def receba_dados_endereco():
    while True:
        try:
            numero = int(input('Informe o numero da casa: '))
            rua = input('Digite rua em que reside: ')
            bairro = input('Digite o bairro: ')
            cidade = input('Digite a cidade: ')
            cep = input('Digite o cep: ')
            return rua, numero, bairro, cidade, cep

        except Exception as e:
            print(f'Ocorreu um erro no input: {str(e)}')



def mostrar_dados_endreco(rua, numero, bairro, cidade, cep):
    print(
            '\nPor favor confira seus dados:' +
            f'\nRua: {rua}\nNumero: {numero}' + 
            f'\nBairro: {bairro}\nCidade: {cidade}\nCEP: {cep}'
        )

def main():
    rua, numero, bairro, cidade, cep = receba_dados_endereco()
    mostrar_dados_endreco(rua, numero, bairro, cidade, cep)

if __name__ =='__main__':
    os.system('clear')
    main()