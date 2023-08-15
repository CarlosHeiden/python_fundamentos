# Exercício 13:
#Crie um jogo em que o computador escolhe um número aleatório entre 1 e 100, 
#e o usuário deve adivinhar qual é esse número.
#O programa deve fornecer dicas se o número fornecido pelo usuário 
#é maior ou menor que o número escolhido pelo computador.
#Utilize um while loop para continuar o jogo até que o usuário acerte o número. Use


import os
import random


def jogo_adivinhar_numero():
    numero_aleatorio = random.randint(1,10)
    tentativas = 0
    numero_usuario = 0
    while numero_usuario  != numero_aleatorio:
        try:
                numero_usuario =int(input('Digite um numero inteiro: '))
                #for tentativas in range(1,numero_aleatorio):
                tentativas +=1

                if numero_usuario > numero_aleatorio:
                    print(f'Voce digitou um numero eh MAIOR que o numero secreto!!') 
                elif numero_usuario < numero_aleatorio:
                    print(f'Voce digitou um numero eh MENOR que o numero secreto!!')
                else:
                    print(
                        f'-' *50 +
                        f'\nParabens voce acertou o numero secreto!!' +
                        f'\nVoce tentou {tentativas} vezes ate acertar!!!\n'+
                        f'=' *50 +
                        f'\nFIM DO JOGO, OBRIGADO POR JOGAR!\n'+
                        F'='*50
                    )
                    break
        except Exception as e:
            print(f'Valor invalido!! {e}')


def main():
    jogo_adivinhar_numero()


if __name__ =='__main__':
    os.system('clear')
    main()
