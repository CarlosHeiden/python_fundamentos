#2 - Classe Livro:
#Crie uma classe chamada Livro que represente um livro.
#A classe deve ter os atributos titulo, autor e ano. 
#Crie um método para exibir as informações do livro (exibir_informacoes()).

class ClassLivro:

    
    def exibir_informacoes_livro(titulo, author, ano):
        print(f'O livro {titulo} editado em {ano} foi escrito por {author}')

if __name__=='__main__':

    titulo = 'CODIGO LIMPO'
    author = 'Roberth C. Martin'
    ano = 2009

    ClassLivro.exibir_informacoes_livro(titulo, author, ano)
