import numpy as np

arr = np.random.randint(1,100, 36).reshape(6,6)
#array con 36 numeri casuali da 1 a 100 formati in 6x6

print("\nARRAY 1")
print(arr)

print("\nARRAY 2 (sottomatrice 4x4)")
arr2 = arr[1:5, 1:5] #righe da 1 a 4, colonne da 1 a 4
print(arr2)

print("\nARRAY 3 (sottomatrice 4x4 invertita)")
arr3 = arr[4:0:-1, 1:5] #righe da 4 a 1, colonne da 4 a 1
print(arr3)

print("\nARRAY 4 (diagonale)")
diag = []
for n in range(0, len(arr)): #ciclo x&y
    diag.append(arr[n,n])
arr4 = np.array(diag)
print(arr4)

print("\nARRAY 5 (sottomatrice 4x4 invertita senza tripli)")
arr5 = arr3
for x in range(arr5.shape[0]): #ciclo x
    for y in range(arr5.shape[1]): #ciclo y
        if arr5[x, y] %3 == 0: #accesso alla cella
            arr5[x, y] = -1
print(arr5)

#in post
#diag = np.diag(matrix)
#mat2 = mat[::-1, :]