"""Ejercicio Utopian Tree """

num_trees = int(input('Ingresa la cantidad de arboles: \n'))


for i in range(num_trees):

    num_cycles = int(input('Ingresa la cantidad de ciclos: \n'))
    h = 1
    for j in range(num_cycles):
        if (j % 2 == 0):
            h = h*2
        else:
            h = h+1        
    print(f'Para el arbol {i+1} su altura es: {h}') 
