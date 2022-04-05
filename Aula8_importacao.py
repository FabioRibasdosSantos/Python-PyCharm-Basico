from Aula7_televisao import Televisao
from Aula7_Calculadora import Calculadora
from Aula8_contador_letras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra da lista: {}'.format(contador_letras(lista)))
    print(teste())