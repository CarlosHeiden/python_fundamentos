# Exercício 16:
#Crie uma função que solicite ao usuário que insira
#uma lista de notas de alunos (números reais entre 0 e 10).
#A função deve calcular e exibir a média, a nota mais alta e a nota mais baixa.
#Utilize listas e for loops para
#processar as notas digitadas pelo usuário.
import os

lista_notas = []

def inserir_notas_lista():
    while True:
        try:
            notas = input('Digite as notas dos alunos ou "99" para sair: ')
            if notas == '99':
                break
            notas = float(notas)
            if notas >=0 and notas <=10:
                lista_notas.append(notas)
                #return lista_notas
        except ValueError:
            print('Valor inválido! Certifique-se de digitar apenas números.')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

def calculo_notas(lista_notas):
    
    maior_nota = max(lista_notas)
    menor_nota = min(lista_notas)
    media_notas = sum(lista_notas)/ len(lista_notas)
    return maior_nota, menor_nota, media_notas

def exibir_resultados(maior_nota, menor_nota, media_notas):
    print(
        f'-'*50+
        f'\nA media das notas: {media_notas:,.2f}\n'+
        f'-'*50+
        f'\nA maior nota: {maior_nota}\n'+
        f'-'*50+
        f'\nA menor nota: {menor_nota}\n'+
        f'='*50
    )
    

def main():
    inserir_notas_lista()
    maior_nota, menor_nota, media_notas = calculo_notas(lista_notas)
    exibir_resultados(maior_nota, menor_nota, media_notas)


if __name__ =='__main__':
    os.system('clear')
    main()