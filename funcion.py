"""Funcion class"""

def hello_world():
    """Function that return 'Hello World'.

    return: string
    """

    return 'Hello World!'

string = hello_world()
string = string.replace('Hello', 'Bye')
print(string)


def hello(name='persona', lastmane='exposito'):
    """Function that return 'name and last name'.
    name: strung,
    lastname:string,

    return: string,
    """
    if name != 'persona':
        return f'¿Como estas {name}?'
    return f'Hola {name} {lastname}'
    
print(hello(lastname=5))    