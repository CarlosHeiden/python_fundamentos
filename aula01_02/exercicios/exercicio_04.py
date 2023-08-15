#Desenvolva uma função que mostre na tela uma contagem regressiva de 5 a 1,
# com uma pausa de um segundo entre cada número.
import os
import time

def contagem_regressaiva():
    for i in range(5,0,-1):
        print(i)
        time.sleep(1)

def contagem_regressiva_manual():
    contador = 5
    while contador > 0:
        print(contador)
        time.sleep(1)
        contador -= 1




if __name__ =='__main__':
    os.system('clear')
    contagem_regressaiva()
    contagem_regressiva_manual()