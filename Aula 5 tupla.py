lista = [12, 10, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(tupla)
print(tupla[2])
print(len(lista_animal))
            #len retorna o número de elementos
tupla_animal = tuple(lista_animal)
            #tuple transforma a lista em tupla
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)
