import numpy as np

arr1 = np.arange(10, 49+1)
arr2 = np.arange(20)

print("Forma: ", arr1.shape)
print("Dimensioni: ", arr1.ndim)
print("Tipo: ", arr1.dtype)
print(arr1)

arr2.dtype = 'float64'
print(arr2.dtype)
print(arr2.shape)