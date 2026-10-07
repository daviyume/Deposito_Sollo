## 1. stampa pari o dispari
x = int(input("Inserisci un numero: "))
if(x%2==0):
    print("Pari")
else:
    print("Dispari")


## 2. count up
continua = True

while continua:
    y = int(input("Inserisci un numero per il count-up: "))

    for cont in range(0, y+1, 1):
        print(cont)

    continua = bool(input("Vuoi continuare? Lascia vuoto se no: "))


## 3. quadrato di lista **
numeri3 = []
continua3 = True

#fill
while continua3:
    print(numeri3)
    continua3 = bool(input("Vuoi aggiungere un nuovo numero nella lista? Lascia vuoto se no: "))

    if continua3:
        numeri3.append(int(input("Inserisci un nuovo numero nella lista: ")))

print("Ecco i quadrati:")
for val in numeri3:
    print(val**2)

print("")
## 4. sistema (contenuto ripetibile) per creare lista. Se piena stampa
## numero elementi con while e numero massimo
numeri4 = []
continua4 = True

#fill
while continua4:
    print(numeri4)
    continua4 = bool(input("Vuoi aggiungere un nuovo numero nella lista? Lascia vuoto se no: "))

    if continua4:
        numeri4.append(int(input("Inserisci un nuovo numero nella lista: ")))

if numeri4 != []:
    max = numeri4[0]
    for val in numeri4:
        if val > max:
            max = val

    cont4 = 0
    while cont4 < len(numeri4):
        print(numeri4[cont4], " è il #", cont4+1)
        cont4 += 1

    print("\nIl numero di elementi è ", cont4)
    print("Il maggiore è ", max)
else:
    print("La lista è vuota")


