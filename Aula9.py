
arquivo = open('teste.txt', 'w')
arquivo.write('Minha primeira escrita')
arquivo.close()

arquivo = open('teste.txt', 'a')
arquivo.write('\nSegunda linha escrita')
arquivo.close()
#\n altera a linha "a" usa para atualizar o texto já existente

arquivo = open('teste.txt', 'a')
arquivo.write('\nTerceira linha escrita')
arquivo.close()


