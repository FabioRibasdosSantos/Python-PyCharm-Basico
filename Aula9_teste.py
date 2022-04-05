
def escrever_arquivo(texto):
    diretorio = 'C:/Users/fabyo/PycharmProjects'
    arquivo = open('diretorio.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('diretorio.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo():
    arquivo = open('diretorio.txt', 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    escrever_arquivo('Primeira linha.\n')
    atualizar_arquivo('Segunda linha.\n')
    atualizar_arquivo('Terceira linha.\n')