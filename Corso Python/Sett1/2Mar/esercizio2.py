#menu con un if e vari elif ed else finale per un menu con
# aggiungi, modifica o elimina

lista = [3, 7, 1, 9]
#stampa lista
print(lista)
#stampa menu
sel = int(input("Seleziona l'opzione: \nAggiungi [1]\nModifica [2]\nElimina[3]\n"))

#logica risposta menu
if(sel>0):
    if(sel==1):
        aggiunta = (input("Cosa vuoi aggiungere? "))
        lista.insert(input("In che posizione? "), aggiunta)
    elif(sel==2):
        modifica = (input("Quale vuoi modificare? (0-", len(lista-1), "): "))
        if modifica>=0 and modifica<lista:
            lista[modifica]= input("Inserisci valore modificato: ")
    elif(sel==3):
        if input("Quale vuoi eliminare?  (0-", len(lista-1), "): ") > 0 and < len(lista)
    else:
        print("Errore.")
else:
    print("Annullato.")

print(lista)