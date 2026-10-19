import numpy as np

arr = np.arange(10)

#indexing
print(arr[0])

#slicing
print(arr[7:9+1])

#boolean indexing
print(arr[arr>4])

arr2d = np.array([np.arange(0, 10), np.arange(20,30)])

#slicing sulle righe
print("SLICE RIGHE")
print(arr2d[1:3])

#slicing sulle colonne
print("SLICE COLONNE")
print(arr2d[:, 1:3])

#slicing misto
print("SLICE MISTO")
print(arr2d[1:3, 1:3])

#[riga, colonna]

#SLICING
# ':' da indice fino a indice

#da x a y con passo z
print(arr[5:10:2])

#funziona con numeri negativi
print("negative")
print(arr[-5:10])
print(arr[:-2])

#FANCY INDEXING
#lista di indici può essere utilizzata per accedere più elementi in un array
idxs = np.array([1, 4, 8])
print(arr[idxs+1])

