# Exercício 10:
#Crie uma função que converta um valor em horas para minutos e segundos.
#Solicite ao usuário que digite o valor em horas e, em seguida, 
#exiba as conversões para minutos e segundos.
#Fórmula para converter horas em minutos: Minutos = Horas * 60
#Fórmula para converter horas em segundos: Segundos = Horas * 3600

import os
import re


def validar_horario(horario):
    padrao = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
    if re.match(padrao, horario):
        return True
    else:
        return False
    

def obter_horas():
    while True:
        horario = input('Digite o horario (HH:mm) que deseja converter ou "s" para sair: ')
        if horario.lower() == 's':
            break
        if validar_horario(horario):
            return horario
            #print(horario)
        else:
            print(
                f'\nHorario invalido!! Digite horario no formado HH:mm. **voce digitou: "{horario}"\n'
            )


def converter_horario(horario):
    horas, minutos = horario.split(':')
    horas = float(horas)
    minutos = float(minutos)
    resultado_minutos = (horas * 60) + minutos
    resultado_segundos = (horas * 3600) + (minutos * 60)
    return resultado_minutos, resultado_segundos

def exibir_horarios_convertidos(horario, resultado_minutos, resultado_segundos):
    print(
        f'-' *70 +
        f'\nO horario digitado -> {horario}\n'+
        f'-' *70 +
        f'\nO resultado da conversao do horario informado para minutos -> {resultado_minutos:,.2f} minutos\n'+
        f'-' *85 +
        f'\nO resultado da conversao do horario informado para segundos -> {resultado_segundos:,.2f} segundos\n'+
        f'='*85
    )


def main():
    horario = obter_horas()
    resultado_minutos, resultado_segundos = converter_horario(horario)
    exibir_horarios_convertidos(horario, resultado_minutos, resultado_segundos)


if __name__ =='__main__':
    os.system('clear')
    main()