"""Contar vocales"""

texto = input('Ingresa un texto')
texto.lower()
numero = 0

 for char in texto:
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        numero += 1
        print(f'Hay {numero} de vocales en tu texto')  