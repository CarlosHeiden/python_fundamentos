class Calculator:
    operacoes_limite = 10
    input_mensagem = 'Informe um numero entre 1 e 5 para calcular: '
    input_mensagem += '\n1 = somar'
    input_mensagem += '\n2 = subtrair'
    input_mensagem += '\n3 = multiplicar'
    input_mensagem += '\n4 = dividir'
    input_mensagem += '\n5 = modulo'
    input_mensagem += '\ninforme a operacao: '

    def somar(numero_1, numero_2):
        print(f'\33[032m Soma - Resultado: {numero_1 + numero_2}\33[0m')

    def subtrair(numero_1, numero_2):
        print(f'Subtracao - Resultado: {numero_1 - numero_2}')

    def multiplicar(numero_1, numero_2):
        print(f'Multiplicacao - Resultado: {numero_1 * numero_2}')

    def dividir(numero_1, numero_2):
        print(f'Divisao - Resultado: {numero_1 / numero_2}')

    def modulo(numero_1, numero_2):
        print(f'Resto-Div - Resultado: {numero_1 % numero_2}')

    def controle_operacoes():
        contador = 0
        while contador <Calculator.operacoes_limite:
            contador+=1

            try:
                print(f'operacao: {contador}')
                numero_1 = int(input('Informe o primeiro numero: '))
                numero_2 = int(input('informe o segundo numero: '))

                if numero_1 >0 and numero_2 >0:
                    while True:
                        try:
                            opcao = int(input(Calculator.input_mensagem))

                            if opcao == 1:
                                Calculator.somar(numero_1, numero_2)
                                break
                            elif opcao == 2:
                                Calculator.subtrair(numero_1, numero_2)
                                break
                            elif opcao == 3:
                                Calculator.multiplicar(numero_1, numero_2)
                                break                                
                            elif opcao ==4:
                                Calculator.dividir(numero_1, numero_2)
                                break
                            elif opcao ==5:
                                Calculator.modulo(numero_1, numero_2)
                                break
                            else:
                                raise ValueError
                        except:
                            print('Informe uma opcao valida!!')
                else:
                    print('Informe numeros positivos!! ')
            except KeyboardInterrupt:
                print('\nPrograma encerrado manualmente!!!')
                quit()
            except:
                print('Informe numeros validos!!')


if __name__ == '__main__':
    Calculator.controle_operacoes()