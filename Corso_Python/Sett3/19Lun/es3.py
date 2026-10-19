#7 step da eseguire riguardo slicing e fancy indexing

import numpy as np

arr1d = np.random.randint(10,50, 20)
print("ARRAY")
print(arr1d)

print("PRIMI 10")
arr2 = arr1d[:10]
print(arr2)

print("ULTIMI 5")
arr3 = arr1d[-5:]
print(arr3)

print("5-15")
arr4 = arr1d[5:15]
print(arr4)

print("OGNI TERZO")
arr5 = arr1d[::3]
print(arr5)

print("NOVANTANOVE")
arr6 = arr1d
arr6[5:10]=99
print(arr6)

