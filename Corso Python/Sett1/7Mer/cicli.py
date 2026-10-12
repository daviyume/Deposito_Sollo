#I cicli ripetono una porzione di codice finché la condizione è vera

#ciclo while
cont = 0
while cont < 5:
    print(cont)
    cont+=1

#ciclo booleano
continua = True
while continua:
    print("ciao")

    if input("Scrivi x per uscire").lower()=='x':
        continua = False

#for, utilizzato per valori determinati o determinabili
numeri = [3, 7, 5, 2]

for val in numeri:
    print(val)

lim = "nave"
for x in lim:
    print(x)

#range([start]), stop, [step])

for i in range(12, 20, 2):
    print(i)

#3 clausole dei cicli: break, continue e pass
    while True:
        if lim == "nave":
            break #break esce
        else:
            pass #pass non fa nulla ed è per scopo organizzativo

for x in lim:
    if x == "a":
        continue #passa alla nuova iterazione
    print(x)

#operatore * splat. Prende un iterabile e
#  lo espande in elementi separati, che possono essere assegnati ad
# un altro iterabile come una lista.
numeri = [*range(1, 11)]
print(numeri)

listavuota = [*range(20)] #crea 20 celle facilmente
print(listavuota)