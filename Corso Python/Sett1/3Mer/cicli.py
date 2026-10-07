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