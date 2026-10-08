import random

'''
def sommanumeri(sommaognidue):
    def wrapper(*args, **kwargs):
        if(mod=="pari"):
            return sommaognidue(*args, **kwargs)
        else:
            return sommaognidue(*args, **kwargs)
    return wrapper
'''
#uso di decoratore eliminato perché non permette l'accesso di variabili specifiche

def sommanumeri(listag: list, mod: str):
    if(mod=="pari"):
        return sommaognidue(listag, 0)
    else:
        return sommaognidue(listag, 1)

#@sommanumeri
def sommaognidue(listag: list, n: int):
    somma = 0
    for val in listag:
        if val %2 == n:
            somma += val
    return somma



def isprime(n: int):
    primo = True
    for d in range(n-1, 1, -1):
        if(n%d==0):
            primo = False
            break
    return primo

def intreq():
    n = 0
    while n<=0:
        n = int(input("Inserisci un numero positivo: "))
        if n <=0:
            print("Riprova.")
    return n

def randomrefill(listag: list, n: int):
    lista.clear()
    for i in range(0, n, 1):
        listag.append(random.randint(0, n))

def checkprimi(listag: list):
    for n in listag:
        if isprime(n):
            yield n
        else:
            listag.remove(n)
            
lista = []
x=0

while True:
    scelta = int(input("Quale esercizio vuoi svolgere? (1-7): "))

    match scelta:
        case 1: #richiedi numero
            x = intreq()

        case 2: #genera lista
            x = intreq()
            randomrefill(lista, x)
            print(lista)

        case 3: #somma numeri pari
            somma = sommanumeri("pari")
            print(somma)

        case 4: #somma numeri dispari
            somma = sommanumeri("dispari")
            print(somma)
            
        case 5: #se primo
            x = intreq()
            print("Primo? ", isprime(x))

        case 6: #stampa tutti numeri primi
            for n in checkprimi(lista):
                print(n)

        case 7: #stampa se somma numeri è primo
            somma = 0
            for n in lista:
                somma += n

            if isprime(somma):
                print("La somma di tutti i numeri è un numero primo: ", somma)
            else:
                print("La somma di tutti i numeri NON è un numero primo: ", somma)


