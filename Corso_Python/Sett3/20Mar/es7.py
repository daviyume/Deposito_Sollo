import os
import numpy as np
folderpath = os.path.dirname(os.path.abspath(__file__))+"/"

def saveFile(testo):
    path = folderpath+"es7testo.txt"
    file = open(path, "w")
    file.write(testo)
        


listamatrici = []
testo = ""

while True:
    
    print("Matrici: ", len(listamatrici))
    match input("Seleziona l'azione: [C] Crea  [E] Estrai sottomatrice  [T] Trasponi  [S] Somma  [X] Esci: ").lower():
        case 'c':
            r = int(input("Inserire il numero delle righe: "))
            c = int(input("Inserire il numero delle colonne: "))
            matrix = np.random.randint(0, 101, r*c)
            matrix = np.reshape(matrix, (r, c))
            print(matrix)

            listamatrici.append(matrix)

        case 'e':
            l = int(input("Inserisci quale matrice da dividere nella lista: "))
            m1 = listamatrici[l] #crea copia dalla lista

            #sottomatrice contenente il terzo centrale
            rowbeg = int(m1.shape[0]/3)
            rowend = int(m1.shape[0]-rowbeg)
            colbeg = int(m1.shape[1]/3)
            colend = int(m1.shape[1]-colbeg)
            matrix = m1[rowbeg:rowend, colbeg:colend]
            print(matrix)

            listamatrici.append(matrix)

        case 't':
            l = int(input("Inserisci quale matrice da trasporre nella lista: "))
            m1 = listamatrici[l]

            matrix = np.transpose(m1)

            print(matrix)
            listamatrici.append(matrix)

        case 's':
            l = int(input("Inserisci quale matrice da trasporre nella lista: "))
            m1 = listamatrici[l]

            somma = np.sum(m1)
            print(somma)
            listamatrici.append("Somma: "+str(somma))

    testo = str(listamatrici)
    saveFile(testo)
    if input("Vuoi continuare? (s/n): ").lower() == 'n':
        break