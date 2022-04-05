from datetime import datetime

data_string = '01/01/2019 12:20:22'
data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
print(data_convertida)

nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
print(nova_data)