import os
import numpy as np
folderpath = "Corso_Python/Sett3/20Mar/"

while True:
    arr = np.random.rand(15)*100

    testo = "ARRAY\n"+str(arr)+ "\nSomma: "+str(np.sum(arr))+ "\nMedia: "+str(np.mean(arr))
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