#inserisce un numero. Controlla se è primo, pari, o nessuno dei due.
#se primo salva e stampa che è primo, sennò dice che non è primo.
#si ferma quando ha 5 numeri primi

cont = 0
numeriprimi = []
contprimi = 0

while contprimi<5:
    x = int(input("Inserisci un numero: "))

    primo = True
    cont = x-1

    #escluso 0
    if x == 0:
        primo = False

    #check
    while primo == True and cont>1 and x >1:
        if(x%cont==0):
            print("Divisione trovata: ", x, "/", cont)
            primo = False
        cont -= 1

    #stampa
    if primo:
        print(x, "è primo")
        numeriprimi.append(x)
        contprimi += 1
    else:
        print(x, "non è primo")

print(numeriprimi)