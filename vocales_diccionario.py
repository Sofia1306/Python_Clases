"""Contar vocales con diccionarios"""

texto = input('Ingresa un texto').lower()

vocales ={
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0
}

for char in texto:
    if char == 'a':
        vocales['a'] += 1

    if char == 'e':
        vocales['e'] += 1    

    if char == 'i':
        vocales['i'] += 1

    if char == 'o':
        vocales['o'] += 1        

    if char == 'u':
        vocales['u'] += 1


print(f'Hay', vocales['a'], 'a ')
print(f'Hay', vocales['e'], 'e ')   
print(f'Hay', vocales['i'], 'i ')
print(f'Hay', vocales['o'], 'o ')
print(f'Hay', vocales['u'], 'u ')



         