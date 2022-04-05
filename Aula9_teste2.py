
def escrever_arquivo(nome_arquivo):
    arquivo = open('diretorio', 'w')
    arquivo.write(nome_arquivo)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo():
    arquivo = open('nome_arquivo', 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    #escrever_arquivo('Primeira linha.\n')
    aluno = 'Felipe,7,5,3,8\n'
    atualizar_arquivo('Notas.txt', aluno)
    #ler_arquivo('teste.txt')