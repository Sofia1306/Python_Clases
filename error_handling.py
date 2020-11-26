"""Error handling"""

"""
def division(int1, int2):
    try: 
        return int1/int2
    except: 
        raise Exception('No podemos dividir entre cero')
print(division(0,0))
"""

import sys


def linux_function():
    assert ('linux' in sys.platform), "OS Error: This code only run on Linux"
    print('Doing something')

try:
    linux_function()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as file_error:
        print(file_error)
finally:
    print('This is the finally clause')