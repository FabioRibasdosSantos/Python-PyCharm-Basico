# for x in range (100):
#     print(x)


# for x in range (0, 101):
#     print(x)


# a = int(input('Entre com um número: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#        div = div+1
# if div == 2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))


# for num in range(101):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)

# a = int(input('Entre com um valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)


# a = 0
# while a <= 10:
#     print(a)
#     a += 1

a = int(input('Primeiro Bimestre: '))
while a > 10:
    a = int(input('Você digitou errado no Primeiro Bimestre'))
b = int(input('Segundo Bimestre: '))
while b > 10:
    b = int(input('Você digitou errado no Segundo Bimestre'))
c = int(input('Terceiro Bimestre: '))
while c > 10:
    c = int(input('Você digitou errado no Terceiro Bimestre'))
d = int(input('Quarto Bimestre: '))
while d > 10:
    d = int(input('Você digitou errado no Quarto Bimestre'))
media = (a + b + c + d)/4
print('Média: {}'.format(media))