class Animal:

    #ATRIBUTOS
    #PRIVATE -> __nome (nome igual nome varaivel)
    #PROTECTED-> _nome
    #PUBLICO ->  nome


    #CONSTRUTOR

    def __init__(self, raca, cor, idade, nome):
        self._raca = raca
        self._cor = cor
        self._idade = idade
        self.__nome = nome
        print('Objeto instanciado com sucesso')

    # GETTERS
    @property
    def raca(self):
        return self._raca
    
    @property
    def cor(self):
        return self._cor
    
    @property
    def idade(self):
        return self._idade
    
    @property
    def nome(self):
        return self.__nome

    @raca.setter
    def raca(self, nova_raca):
        print(f'setou raca {self._raca} para {nova_raca}')
        self._raca = nova_raca

    @cor.setter
    def cor(self, nova_cor):
        print(f'setou cor {self._cor} para {nova_cor}')
        self._cor = nova_cor

    @idade.setter
    def idade(self,nova_idade):
        print(f'setou idade {self._idade} para {nova_idade}')
        self._idade = nova_idade

    @nome.setter
    def nome(self,novo_nome):
        print(f'setou idade {self.__nome} para {novo_nome}')
        self.__nome = novo_nome

# INSTANCIAS (CRACOES)DOS OBJETOS DA CLASSE ANIMAL

leao = Animal('leao da montanha', 'bege', 15, 'KING')
gato = Animal('ceames', 'preto', 11, 'CLEOPATA')
pantera = Animal('pantera cor de rosa', 'cor de rosa', 19, 'FANTASMA')

print(leao.raca)
print(leao.cor)
print(leao.idade)

print(gato.raca)
print(gato.cor)
print(gato.idade)

print(pantera.raca)
print(pantera.cor)
print(pantera.idade)

# UTILIZAZR SETTERS

print(f'='*30)
pantera.idade = 55
pantera.cor = 'BRANCA'
print(pantera.nome)
print(pantera.idade)
print(pantera.cor)