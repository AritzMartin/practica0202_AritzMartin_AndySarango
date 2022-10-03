print('Cuanto desea invertir?')
inversion = float(input())
print('Intoduzcas su interes anual')
interes = float(input())
interes_real = interes/100
print('Durante cuantos anos?')
anos = float(input())
resultado = inversion + (inversion*interes_real*anos)
print('Tu ganacia es de', resultado, '€')