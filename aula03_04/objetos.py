class Pessoa:
    nome = 'Carlos'
    idade = 54
    origem = 'Brasil'

    def dizer_ola(self):
        print(f'Ola, eu sou o {Pessoa.nome} ')

    def pensar(self):
        print(f'Eu estou pensando')

    def comprar(self):
        print(f'Compra realizada')

    def get_nome(self):
        return Pessoa.nome
    
    def get_idade(self):
        return Pessoa.idade
    
    # setter para setar (configurar) nome

    def set_nome(self, nome_novo):
        Pessoa.nome = nome_novo

    def set_idade(self, idade_nova):
        Pessoa.idade = idade_nova

pessoa_1 = Pessoa()
pessoa_2 = Pessoa()

pessoa_1.comprar()
pessoa_2.pensar()
print(pessoa_1.get_nome())
print(pessoa_2.get_idade())

#usando settins

nome_atual = 'HEIDEN'
pessoa_1.set_nome(nome_novo=nome_atual)
print(pessoa_1.set_nome(nome_atual))

idade = 55

pessoa_2.set_idade('55')
print(pessoa_2.set_idade(idade_nova=idade))
