#parte 2 esercizio di ieri

import os
import numpy as np
folderpath = os.path.dirname(os.path.abspath(__file__))+"/"

def saveFile(testo):
    path = folderpath+"es_7pt2testo.txt"
    file = open(path, "w")
    file.write(testo)
        


listamatrici = []
testo = ""

while True:

    dosave = True
    print("Matrici: ", len(listamatrici))
    match input("Seleziona l'azione: [C] Crea  [E] Estrai sottomatrice  [T] Trasponi  [S] Somma\n  [M] Moltiplicazione  [N] Media  [R] Rimuovi  [P] Print  [X] Esci: ").lower():
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
            l = int(input("Inserisci quale matrice da sommare nella lista: "))
            m1 = listamatrici[l]

            somma = np.sum(m1)
            print(somma)
            listamatrici.append("Somma: "+str(somma))
        case 'm':
            l = int(input("Inserisci la matrice di primo prodotto: "))
            m1 = listamatrici[l]
            l = int(input("Inserisci la matrice di secondo prodotto: "))
            m2 = listamatrici[l]

            if(m1.shape==m2.shape):
                m3 = m1*m2
                print(m3)
                listamatrici.append(m3)
            else:
                print("Errore: le matrici sono di dimensioni diverse.")
                dosave = False

        case 'n':
            l = int(input("Inserisci la matrice di cui calcolare la media: "))
            m1 = listamatrici[l]

            med = np.mean(m1)
            print(med)
            listamatrici.append(med)

        case 'r':
            l = int(input("Inserisci l'elemento da rimuovere nella lista: "))
            listamatrici.remove(listamatrici[l])

        case 'p':
            print(listamatrici)
            dosave = False

        case 'x':
            break

        case _:
            print("Errore: azione sconosciuta.")
            dosave = False

    if dosave:
        testo = str(listamatrici)
        saveFile(testo)
    if input("Vuoi continuare? (s/n): ").lower() == 'n':
        break