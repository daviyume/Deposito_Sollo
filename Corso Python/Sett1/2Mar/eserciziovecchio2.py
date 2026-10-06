#menu con un if e vari elif ed else finale per un menu con
# aggiungi, modifica o elimina

lista = [3, 7, 1, 9]
#stampa lista
print(lista)
#stampa menu
sel = input("Seleziona l'opzione: \nAggiungi [a]\nModifica [m]\nElimina[e]\n")

pos = "(0-",len(lista)-1,")"
#logica risposta menu
if(sel=='a' or sel=='m' or sel=='e'):
    if(sel=='a'):
        aggiunta = (input("Cosa vuoi aggiungere? "))
        lista.insert(input("In che posizione? ", pos, " :"), aggiunta)
    elif(sel=='m'):
        modifica = (input("Quale vuoi modificare? ", pos, " :"))
        if modifica>=0 and modifica<lista:
            lista[modifica]= input("Inserisci valore modificato: ")
    elif(sel=='e'):
        elimina = input("Quale vuoi eliminare?", pos, ": ")
        if(elimina > 0 and elimina < len(lista)):
            lista.remove(lista[elimina])
        else:
            print("Invalido.")
else:
    print("Annullato.")

print(lista)