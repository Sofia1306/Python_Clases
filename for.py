""" Clase de For."""


names = ('Abraham', 'Cesar', 'Daniel', 'Daniela', 'Diego', 'Edgar' )


for name in names:
    print(f'Student {name}')
else:
    print('No more names')


string = 'Mauricio'

for char in string:
    if char != 'i':
        print(char)
    else:
        print('Out of the for')
    

    numbers = []

    for number in range(0,21,2):
        numbers.append(number)

        print(numbers)
