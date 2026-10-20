import numpy as np
import os

folderpath = "Corso_Python/Sett3/20Mar/"

while True:
    arr = np.linspace(0,10, 50)
    arr2 = np.random.random(50)
    arr3 = arr+arr2

    somma = np.sum(arr3)
    somma5 = 0
    for i in range(arr3.shape[0]):
        if arr3[i] > 5:
            somma5+= arr3[i]

    '''print("\nARRAY 1\n", arr)
    print("\nARRAY 2\n", arr2)
    print("\nARRAY 3\n", arr3)
    print("\nSOMMA: ", somma)
    print("\nSOMMA5: ", somma5)
'''
    testo = "ARRAY 1\n"+str(arr)+"\n\nARRAY 2\n"+ str(arr2)+"\n\nARRAY 3\n"+ str(arr3)+"\n\nSOMMA: "+ str(somma)+"\nSOMMA5: "+ str(somma5)

    print(testo)

    nomefile = input("Inserisci il nome file (.txt): ")
    path = folderpath+nomefile+".txt"

    if os.path.isfile(path):
        if input("Vuoi sovrascrivere il file? (s/n): ").lower() == 's':
            file = open(path, "w")
            file.write(testo)
        else:
            print("Annulato.")
    else:
        file = open(path, "w")
        file.write(testo)

    if input("Vuoi continuare? (s/n): ").lower() == 'n':
        break