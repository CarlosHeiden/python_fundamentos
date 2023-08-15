#6 - Classe Aluno:
#Crie uma classe chamada Aluno que represente um aluno.
#A classe deve ter os atributos nome, matricula e notas (uma lista de notas).
#Crie métodos para calcular a média (calcular_media()) 
# e exibir o status do aluno com base na média (exibir_status())

import os

class Aluno:

    nome = ''
    matricula = 0.0
    lista_notas = [5.5, 8.5, 9.5]

    def cacular_notas(lista_notas):
        soma_notas = 0
        for notas in lista_notas:
            soma_notas += notas
        media = soma_notas/ len(lista_notas)
        return media

    def exibir_status(nome, matricula, media):
        print(
            f'='*50 +
            f'\nSTATUS DO ALUNO\n'+
            f'-'*50+
            f'\nNome do aluno: {nome}\n'+
            f'Numero da matricula: {matricula}\n'+
            f'Media das notas: {media:.2f}\n'+
            f'='*50 
        )
        

    def script(): 
        nome = 'Carlos'
        matricula = 11468
        lista_notas = [5.5, 8.5, 9.5]  
         
        media = Aluno.cacular_notas(lista_notas)
        Aluno.exibir_status(nome, matricula, media)


if __name__=='__main__':
    os.system('clear')
    Aluno.script()
    
