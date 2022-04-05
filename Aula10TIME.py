from datetime import time

horario = time(hour=15, minute=18, second=30)
print(horario.strftime('%H:%M:%S'))
print(type(time))
horario_str = horario.strftime('%H:%M:%S')
print(horario_str)
print(type(horario_str))
