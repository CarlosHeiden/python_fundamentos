#4 - Classe Funcionário:
#Crie uma classe chamada Funcionario com os atributos nome (private), salario (private) 
#e cargo (public). Crie métodos para definir o nome(set_nome(novo_nome)), 
#obter o nome (get_nome()), 
#calcular aumento de salário (aumentar_salario(aumento)) 
#e exibir informações completas do funcionário (exibir_informacoes()). 
#Crie um construtor e trabalhe a manipulação da classe e dos dados via objetos.


class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.__nome = nome
        self.__salario = salario
        self.cargo = cargo

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, nome_novo):
        self.__nome = nome_novo

    def aumenta_salario(self, valor_acrescido):
        self.__salario = self.__salario = valor_acrescido

    def exibir_informacoes(self):
        print(f'Funcionario {self.__nome}, possui salario {self.__salario} e cargo {self.cargo}')

if __name__ == '__main__':
    funcionario_1 = Funcionario('carlos', 10000.00, 'Dev')
    funcionario_2 = Funcionario('aline', 5000.00, 'Analista')

    print(funcionario_1.nome)
    print(funcionario_1.nome)

    funcionario_1.exibir_informacoes()
    funcionario_2.exibir_informacoes()
    funcionario_1.aumenta_salario(7500.00)



        
