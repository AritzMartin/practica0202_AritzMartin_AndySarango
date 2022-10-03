print('Introduzca su peso en Kg')
peso = float(input())
print('Introduzca su estatura en m')
altura = float(input())
resultado = peso/altura**2
redondeo = round(resultado, 2)
print('Tu indice de masa corparal es de', redondeo)