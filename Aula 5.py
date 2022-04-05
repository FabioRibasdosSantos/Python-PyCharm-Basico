# lista = [1, 3, 5, 7]
#         #lista sempre com colchetes
# lista_animal = ['cachorro', 'gato', 'elefante']
# #print(lista_animal[1])
#         #python sempre inicia contagem em 0
#
# for x in lista:
#         #sempre usar : em 'for', 'else' e 'if'
#     print(x)


# lista = [1, 3, 5, 7]
# lista_animal = ['cachorro', 'gato', 'elefante']
# #print(lista_animal[1])
#
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print (soma)


lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
print(lista_animal[1])
print(sum(lista))
print(max(lista))
print(min(lista))
print(max(lista_animal))
print(min(lista_animal))

if 'gato' in lista_animal:
    print('Existe um gato na lista')
else:
    print('Não existe um gato na lista')

if 'lobo' in lista_animal:
    print('Existe um lobo na lista')
else:
    print('Não existe um lobo na lista. Será incluida')
    lista_animal.append('lobo')
        #append inclui dado na lista
    print(lista_animal)

lista_animal.pop(0)
        #retira o nome 0 da lista
(print(lista_animal))

lista = [12, 10, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
lista.sort()
lista_animal.sort()
            #coloca em ordem númerica ou alfabética
print(lista)
print(lista_animal)

lista_animal.reverse()
print(lista_animal)