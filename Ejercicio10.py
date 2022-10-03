print('Introduzca la cantidad de payasos')
payasos = int(input())
peso_paya = payasos*112
print('Introduzca la cantidad de munecas')
munecas = int(input())
peso_mune = munecas*75
peso_paquete = peso_paya + peso_mune
peso_kg = peso_paquete/100
print('Tu paquete pesa', peso_kg, 'Kg')