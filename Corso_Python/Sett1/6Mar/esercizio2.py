#2 liste. Una di numeri una di parole.
#Chiedi quale lista usare, poi scegliere
# se aggiungere o rimuovere un elemento.
# Stampa lista.

numeri = [5, 6, 1, 21]
parole = ["elefante", "rosso", "scala", "giocare"]

print(numeri)
print(parole)

sel = int(input("Quale lista vuoi selezionare? (1/2)"))

#numero
if sel == 1:
    if input("Vuoi aggiungere o rimuovere un numero? (a/r)").lower == 'a':
        aggiunta = input("Che numero vuoi aggiungere? ")

        print("1 -", len(numeri), ")")
        pos = int(input("Dove lo vuoi aggiungere?"))-1
        numeri.insert(pos, aggiunta)
    else:
        print("1 -", len(numeri), ")")
        pos = int(input("Quale numero vuoi rimuovere?"))-1
        numeri.remove(numeri[pos])
#parola
else:
    if input("Vuoi aggiungere o rimuovere una parola? (a/r)").lower == 'a':
        aggiunta = input("Che parola vuoi aggiungere? ")

        print(" (1 -", len(parole), ")")
        pos = int(input("Dove la vuoi aggiungere?"))-1
        parole.insert(pos, aggiunta)
    else:
        print(" (1 -", len(parole), ")")
        pos = int(input("Quale parola vuoi rimuovere?"))-1
        parole.remove(parole[pos])

print(numeri)
print(parole)