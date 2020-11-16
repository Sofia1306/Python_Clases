"""Ejercicio Decimal a Binario """
import math

numero = int(input('Ingresa un número: \n'))


binario = ''
while (numero > 0):
    if (numero%2 == 0):
        binario = '0' + binario
    else:
        binario = '1' + binario
    numero = int(math.floor(numero/2))

print(f'El número en binario es {binario}')

