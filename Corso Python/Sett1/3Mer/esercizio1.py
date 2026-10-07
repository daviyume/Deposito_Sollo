#chiedi di inserire un numero, e fai countdown da lì.
#chiedi se ripetere.

continua = True

while continua:
    x = int(input("Inserisci il numero da cui iniziare il countdown: "))

    for i in range(x, -1, -1):
        print(i)

    continua= bool(input("Vuoi continuare? (lascia vuoto se no)"))
