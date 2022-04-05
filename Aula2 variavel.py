a = int(input('Entre com primeiro valor: '))
b = int(input('Entre com segundo valor: '))
print(type(a))

soma=a+b
subtracao=a-b
multiplicacao=a*b
divisao=a/b
print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
resto=a%b
print(resto)

print('soma: '+str(soma))

print('Soma: {soma}'
      '\nSubtração: {subtracao}'
      '\nMultiplicação: {multiplicacao}'
      '\nDivisão: {divisao}'
      '\nResto: {resto}'.format(soma=soma, subtracao=subtracao, multiplicacao=multiplicacao, divisao=divisao, resto=resto))

print(int(divisao))