#4 - Classe Agenda:
#Crie uma classe chamada Agenda que represente uma agenda de contatos. 
#A classe deve ter um atributo para armazenar uma lista de contatos.
#Crie métodos para adicionar (adicionar_contato(nome, telefone)), 
#remover (remover_contato(nome)), e exibir todos os contatos (exibir_contatos()).
import os

class Agenda:

    input_mensagem = '\nInforme um número entre 1 e 4: '
    input_mensagem += '\n1 = ADICIONAR CONTATOS'
    input_mensagem += '\n2 = EXCLUIR CONTATOS'
    input_mensagem += '\n3 = EXIBIR AGENDA CONTATOS '
    input_mensagem += '\n4 = SAIR\n'


    def controle_opracoes(dict_contatos):
            
            while True:
                try:
                    opcao = int(input(Agenda.input_mensagem))

                    if opcao == 1:
                        Agenda.adicionar_contatos(dict_contatos)
                        #break
                    elif opcao == 2:
                        Agenda.excluir_contatos(dict_contatos)
                        #break
                    elif opcao == 3:
                        Agenda.exibir_lista_contatos(dict_contatos )
                        #break
                    elif opcao == 4:
                        print('ENCERRANDO O PROGRAMA!!')
                        break
                    else:
                        raise ValueError()
               
                except KeyboardInterrupt:
                    print('\nPrograma encerrado manualmente.')
                    quit()
                except:
                    print('Informe uma opção válida!')
       
    def adicionar_contatos(dict_contatos):
        
        while True:
            try:
                nome = input('Informe o NOME do contato para INCLUIR NA AGENDA: ').upper()
                telefone = input('Informe o TELEFONE para INCLUIR NA AGENDA do contato: ')
                dict_contatos[nome] = telefone
                print(dict_contatos)
                break

                

            except Exception as e:
                print(f'Valor invalido, digite valores validos!!! {e}')
        return dict_contatos
    
    def excluir_contatos(dict_contatos):

        while True:
            try:
                nome = input('Informe o NOME do contato para EXCLUIR: ').upper()
                #for key in dict_contatos.items():
                if nome in dict_contatos:
                    del dict_contatos[nome]
                else:
                    print('Contato nao encontrado!!')
                print(dict_contatos)
                break
                

            except Exception as e:
                print(f'Valor invalido, digite valores validos!!! {e}')
        return dict_contatos
    
    def exibir_lista_contatos(dict_contatos):
        print(
            f'='*50+
                f'\nAGENDA CONTATOS\n'
        )
        for key, value in dict_contatos.items():
            print(
                f'-'*50 +
                f'\nNome: {key}\n'+
                f'Telefone: {value}\n'
                
            )
        print(f'='*50)

if __name__=='__main__':
    os.system('clear')
    dict_contatos = {}
    Agenda.controle_opracoes(dict_contatos)
    