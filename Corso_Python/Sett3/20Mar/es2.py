import numpy as np

print("\nARRAY 1")
arr = np.linspace(0,1, 12)
arr = np.reshape(arr, (3, 4))
print(arr)

print("\nARRAY 2")
arr2 = np.random.rand(3, 4)
print(arr2)

print("\nSOMMA ARRAY")
arr3 = arr+arr2
print(arr3)
arr3 = arr3.astype("int")
print(arr3)