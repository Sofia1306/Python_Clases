"""Algoritmo Selection sort"""

lis = [5, 3, 6, 7, 4, 2, 9, 1,8]
print(lis)

for i in range(len(lis)): 
    lis_c = i 
    for j in range(i+1, len(lis)): 
        if lis[lis_c] > lis[j]: 
            lis_c = j        
    lis[i], lis[lis_c] = lis[lis_c], lis[i]
    print(lis)
 
