#5 operazioni. Con if, while e for, e ripetibile.


while True:
    #1: numero positivo in input
    x = -1
    while x <= 0:
        x = int(input("Inserisci un numero positivo: "))
        if x <=0:
            print("Non è positivo: riprova...")

    #2: stampa somma numeri pari da 1 a n con ciclo for e range
    print("Stampa numeri pari")
    sommap = 0
    for n in range(2, x+1, 2):
        sommap += n
    print(sommap)

    #3: stampa somma numeri dispari
    print("Stampa numeri dispari")
    sommad = 0
    for n in range(1, x+1, 2):
        sommad += n
    print(sommad)

    #4 if per primo
    primo = True
    for n in range(x-1, 1, -1):
        if(x%n==0):
            primo = False
            break

    if(primo):
        print("Il numero è primo")
    else:
        print("Il numero non è primo")

    print("Numero positivo: ", x)
    print("Somma numeri pari: ", sommap)
    print("Somma numeri dispari: ", sommap)
    print("Primo? ", primo)

    if bool(input("Vuoi continuare? Lascia vuoto per interrompere: ")) == False:
        break