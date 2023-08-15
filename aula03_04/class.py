class ClasseCachorro:
    raca = 'Pastor de Shetlan'
    idade = 11

    def latir(latidas):
        for latida in range(latida):
            print('au au')

    def comer(comida, horario):
        print(f'au au, come {comida}, au au horario {horario}')

    def mostrar_info_dog():
        print(f'O cahorro eh da raca {ClasseCachorro.raca} e tem {ClasseCachorro.idade} anos')


class ClassePessoa:
    #  atributos = variaveis
    nome = 'Carlos'
    idade = 55
    altura = 1.74
    peso = 85.0
    pais_origem = 'Brasil'
    genero = 'Alien'

    #metodods = funcoes

    def dizer_ola():
        print(f'Ola, eu sou {ClassePessoa.nome}')

    def mostrar_dados():
        print(
            f'Eu tenho {ClassePessoa.idade} anos, minha altura eh {ClassePessoa.altura} '+
            f'meu peso eh {ClassePessoa.peso} e meu genero eh {ClassePessoa.genero}'
        )

    def mostrar_origem():
        print(f'Eu venho de/do/da {ClassePessoa.pais_origem}')

ClasseCachorro.latir(10)
ClasseCachorro.comer('racao', '10:00')
ClasseCachorro.info()
ClassePessoa.dizer_ola()
ClassePessoa.mostrar_dados()
ClassePessoa.mostrar_origem()



