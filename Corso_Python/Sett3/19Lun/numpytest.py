import numpy as np

array1 = np.array([45, 57])

print(np.mean(array1))

#arraybidimensionali
arr2d = np.array([[60, 120, 144], [240, 288, 360]])

print(array1)
print("Lista bidimensionale: ", arr2d)

#dtype
arrint = np.array([1,2,3], dtype='int32')
print(arrint.dtype)

#shape indica le sue dimensioni
#tupla: lista non modificabile
arrnum = np.array([[1,2,3], [4,5,6]])
print(arrnum.shape)
#shape dà come output il numero di elementi e il numero di elementi in ogni array

#arange crea un range di numeri
arrfinoa10 = np.arange(10)
print(arrfinoa10)

#reshape cambia forma dell'array mantenendo i dati
arrfinoa10 = arrfinoa10.reshape(5, 2) #5 array da 2
print(arrfinoa10)