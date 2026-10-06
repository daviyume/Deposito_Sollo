#menu con un if e vari elif ed else finale per un menu con
# aggiungi, modifica o elimina
#questo è il vecchio esercizio 2

lista = [3, 7, 1, 9]
#stampa lista
print(lista)
#stampa menu
sel = input("Seleziona l'opzione: \nAggiungi [a]\nModifica [m]\nElimina[e]\n")

#logica risposta menu
if(sel=='a' or sel=='m' or sel=='e'):
    if(sel=='a'):
        #AGGIUNGI
        aggiunta = input("Cosa vuoi aggiungere? ")
        lista.insert(int(input("In che posizione? ")), aggiunta)

    elif(sel=='m'):
        #MODIFICA
        pos = int(input("Quale vuoi modificare? "))
        if pos>=0 and pos<len(lista):
            lista[pos]= input("Inserisci valore modificato: ")
    
    elif(sel=='e'):
        #ELIMINA
        pos = int(input("Quale vuoi eliminare?"))
        
        if pos > 0 and pos < len(lista):
            lista.remove(lista[pos])
        else:
            print("Invalido.")
else:
    print("Annullato.")

print(lista)