# para ler uma base de dados, preciso importar o módulo que lê
import csv

# agora eu vou dizer onde está o arquivo que vou ler
# digo o caminho (path) do arquivo

caminho_arquivo = "musicas.csv"

# sempre que eu quero criar uma função eu coloco a instrução "def" + "nome da função():"
def ler_musicas():
    print("----- LISTA DE MÚSICAS -----")
    try:
        # o comando "try" serve para o sistema tentar executar uma ou mais instruções. Se der certo, ok. Senão, ele exibe um erro
        with open (caminho_arquivo,"r",encoding='utf-8') as arquivo_musica:
            # o comando with open permite que eu abra algo, mas para isso devo informar 
            # 1 - onde está
            # 2 - o modo de abertura (ler  - r; adicionar - a, reescrever - w)
            # 3 - NÃO OBRIGATÓRIO - colocar como quer ler (codificação) e depois dar um apelido para essa instrução
            leitor = csv.reader(arquivo_musica)
            # chamei um leitor para o sistema que lê csv e adicionei o método reader para ler o arquivo 
            next(leitor)
            # o comando next é para pular a primeira linha do arquivo 

            # agora quero exibir linha por linha do que o leitor viu (sequenciar)
            for cada_linha in leitor: 
                if cada_linha:
                    titulo,artista,ano,genero,duracao_segundos = cada_linha
                    # tenho que falar todos os cabeçalhos do meu arquivo 
                    print('Título',titulo,'Artista',artista,'Ano',ano,'Gênero',genero, 'Duração em segundos', duracao_segundos)

    except FileNotFoundError:
        print('Erro: Arquivo não encontrado')







