"""Algoritmo Burbuja"""

lis = [5, 3, 6, 7, 4, 2, 9, 1,8]

for i in range(1, len(lis)):
        for j in range(0, len(lis) - i):
            if(lis[j + 1] < lis[j]):
                lis[j],lis[j+1] = lis[j+1], lis[j]
                
            print(lis)
