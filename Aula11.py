
lista = [1, 10]
try:
    divisao = 10 / 1
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except IndentationError:
    print('Erro ao acessar um indice invalido da lista')
except BaseException as ex:
    print('Erro desconhecido, Erro {}'.format(ex))
else:
    print('Arquivo sem erros')
finally:
    print('Fechando arquivo')