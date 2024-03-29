#1 - Classe Produto:
#Crie uma classe chamada Produto que represente um produto em uma loja. 
#A classe deve ter os atributos: nome (private), precoe codigo (public). 
#Crie um construtor para inicializar esses atributos e 
#métodos get_nome(), get_preco() e set_preco(novo_preco) paraacessar e modificar o preço.


class Produto:

    def __init__(self, nome, preco, codigo):
        self.__nome = nome
        self.preco = preco
        self.codigo = codigo

    @property
    def nome(self):
        return self.nome
    
    def get_preco(self):
        return self.preco
    
    def set_preco(self, preco_novo):
        self.preco = preco_novo


if __name__ =='__main__':
    carro_objeto = Produto('Gol', 20000.00, 15978634)
    print( carro_objeto.nome)
    print(carro_objeto.get_preco())
    carro_objeto.set_preco(15000.00)
    print(carro_objeto.get_preco())
