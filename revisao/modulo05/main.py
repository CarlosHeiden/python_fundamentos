from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica


def menu():
    cond = 'sim'
    while cond == 'sim':
        borda = '*'*5
        print(f'{borda} MENU {borda}\n')
        var = int(input('1 - PESSOA_FISICA\n2 - PESSOA_JURIDICA\n3 - Sair\n>>'))
        match(var):
            case 1:
                pf = PessoaFisica(
                            input('Digite o nome do titular: ').capitalize(),
                            input('Digite o cpf do titular: '),
                            float(input('Digite o saldo inicial: '))
                        )
                print('='*30)
                print(pf)
                print('='*30)

                var = input('Voce deseja cadastrar um segundo titular?\nsim\nnao\n>> ')

                if var =='sim':
                    pf.segundo_titular = input('Digite o segundo titular: ').capitalize()
                    print('='*30)
                    print(pf)
                    print('='*30)
                        
            case 2:
                pj = PessoaJuridica(
                        input('Digite o nome do titular: ').capitalize(),
                        input('Digite o cnpj da empresa: '),
                        float(input('Digite o saldo inicial: '))
                    )
                print('='*30)
                print(pj)
                print('='*30)

                var = input('Voce deseja cadastrar um segundo titular?\nsim\nnao\n>> ')

                if var =='sim':
                    pj.segundo_titular = input('Digite o segundo titular: ').capitalize()
                    print('='*30)
                    print(pj)
                    print('='*30)

            case 3:
                print('Programa encerrado!')
                break

menu()


                                





