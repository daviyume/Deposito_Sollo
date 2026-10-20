import os
import numpy as np
folderpath = "Corso_Python/Sett3/20Mar/"

while True:
    arr = np.arange(1, 25+1)
    arr = arr.reshape(5,5)
    arr2 = arr[:,0:1]
    arr3 = arr[2:3]
    sommadiag = np.sum(np.diag(arr))

    testo = "ARRAY 1\n"+str(arr)+"\nARRAY 2\n"+str(arr2)+"\nARRAY 3\n"+str(arr3)+"\nSomma diagonale: "+str(sommadiag)
    print(testo)
    
    path = folderpath + input("Inserire il nome del file (.txt): ") + ".txt"
    if os.path.isfile(path):
        if input("Vuoi sovrascrivere? (s/n): ").lower() == 's':
            file = open(path, "w")
            file.write(testo)
        else:
            print("Annullato.")
    else:
        file = open(path, "w")
        file.write(testo)

    if input("Vuoi continuare? (s/n): ").lower() == 'n':
        break