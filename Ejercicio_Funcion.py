"""Ejercicio Funcion"""


def counting_bobs(string):
    """Function that return count of bob in a string.
    
    string: string,
    return: int,
    
    """
    string = string.lower()
    count = 0
    for char in range(len(text)):
    	if text[char: char+3] == 'bob':
    		count +=1
    return count
    
text = input('Ingresa un texto con bobs: \n')
bob_counter = counting_bobs(text)
print(f'Hay {bob_counter} bobs')