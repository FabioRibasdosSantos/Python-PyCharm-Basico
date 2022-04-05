from datetime import datetime

data_atual = datetime.now()
print(data_atual)
print(data_atual.strftime('%d/%m/%Y, %H:%M:%S'))
print(data_atual.strftime('%c'))
print(data_atual.weekday())
tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
print(tupla[data_atual.weekday()])
print(data_atual.today())
print(data_atual.hour)
print(data_atual.year)
data_criada = datetime(2018, 6, 20, 15, 30, 20)
print(data_criada)
print(data_criada.strftime('%c'))
data_string = '01/01/2019'
data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
print(data_convertida)
data_string = '01/01/2019 12:20:22'
data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
print(data_convertida)