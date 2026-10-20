import os
import numpy as np
folderpath = "Corso_Python/Sett3/20Mar/"

while True:
    arr = np.random.randint(10, 50, 16)
    arr = arr.reshape(4,4)
    arr2 = [] #indici specifici
    arr3 = [] #righe dispari
    arr4 = arr+10

    #righe e colonne si alternano nell'array:
    # a passo di due vengono indicizzate la riga della cella (i) e la colonna (i+1)
    idxs = np.array([0,1, 1,3, 2,2, 3,0])
    for i in range(0, idxs.shape[0], 2):
        arr2 = np.append(arr2, arr[idxs[i], idxs[i+1]])

    #righe dispari. arr.shape[0] indica lunghezza della riga, mentre shape[1] colonna
    idxsdisp = np.arange(1, arr.shape[0], 2)
    for i in range(idxsdisp.shape[0]):
        arr3 = np.append(arr3, arr[idxsdisp[i]])


    testo = "ARRAY 1\n"+str(arr)+"\nARRAY 2\n"+str(arr2)+"\nARRAY 3\n"+str(arr3)+"\nARRAY 4\n"+str(arr4)
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