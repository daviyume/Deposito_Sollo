import numpy as np

print("\nARRAY")
arr = np.concatenate((np.random.randint(0, 49, 50), np.random.randint(49, 101, 50)))
print(arr)
print(arr.dtype)
print(arr.shape)

print("\nTO FLOAT")
#arr.dtype = 'float64'
arr2 = arr.astype('float64')
print(arr2.dtype)
print(arr2.shape)

print("\nSLICING")
arr3 = np.concatenate((arr2[0:10], arr2[-7:], arr2[5:20], arr2[3::4]))
print(arr3)

print("\n 10-15 IN 999")
arr4 = arr3
arr4[10:15] = 999
print(arr4)

print("\n FANCY INDEXING")
idxs = [0, 3, 7, 12, 25, 22, 48]

arr5 = arr4[idxs]
for i in range(arr4.shape[0]-1):
    if arr4[i] %2 == 0:
        arr5 = np.append(arr5, arr4[i])
for i in range(arr4.shape[0]-1):
    if arr4[i] > np.mean(arr4):
        arr5 = np.append(arr5, arr4[i])
print(arr5)