#3 - Classe Carro:
#Crie uma classe chamada Carro que simule um carro. 
#A classe deve ter os atributos marca, modelo e ano.
#Crie métodos para ligar (ligar()), desligar (desligar())
#e exibir as informações do carro (exibir_informacoes()).

class Carro:
    marca = 'GM'
    modelo = 'Vectra'
    ano = 2008

    def ligar_carro():
        print(f'\nO carro marca {Carro.marca}, modelo {Carro.modelo} esta ligado')

    def desligar_carro():
         print(f'\nO carro marca {Carro.marca}, modelo {Carro.modelo} foi desligado')

    def exibir_informacoes():
        print(
            f'='*50 +
            f'\nInformacoes do veiculo.\n'+
            f'-'*50 +
            f'\nMarca: {Carro.marca}\n'+
            f'-'*50 +
            f'\nModelo: {Carro.modelo}\n'+
            f'-'*50 +
            f'\nAno: {Carro.ano}\n'+
            f'='*50 
        )

if __name__=='__main__':
    Carro.ligar_carro()
    Carro.desligar_carro()
    Carro.exibir_informacoes()






