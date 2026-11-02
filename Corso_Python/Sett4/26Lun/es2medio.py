from sklearn.datasets import load_digits
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#The target tells the model 
# which digit the pixels represent. The model learns to recognize 
# the digit from the pixel values.
#b = load_digits()
#print(b.DESCR)

#as frame per caricare dataframe e .frame per accedere solo al df
df = load_digits(as_frame=True).frame

print(df.columns)

print("\nshape 0:")
print(df.shape[0])
print("\nshape 1:")
print(df.shape[1]-1)

digits = load_digits(as_frame=True)
print(digits.images[0])

#creazione 10 grafici
for i in range(10):
    plt.figure()
    plt.imshow(digits.images[i], cmap="gray")
    plt.title("Cifra "+str(digits.target[i]))
plt.show()


#somma instanze per ogni cifra
cifre = np.arange(10)
n = []

for i in cifre:
    inst = np.sum(digits.target == i)
    n.append(inst)


plt.figure()
plt.bar(cifre, n)
plt.xticks(range(10))

plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.title('Campioni per ogni cifra')
plt.show()