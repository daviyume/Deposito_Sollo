#utente inserisce 2 numeri, e una delle 4 operazioni.
#se divisione per 0, mandare un errore e prevenire l'operazione.

x = int(input("Inserisci il primo numero: "))
y = int(input("Inserisci il secondo numero: "))

op = input("Inserisci l'operazione [+] [-] [*] [/] : ")

match op:
    case '+':
        print("La somma è ", x+y)
    case '-':
        print("La sottrazione è ", x-y)
    case '*':
        print("Il prodotto è ", x*y)
    case '/':
        if y!=0:
            print("Il risultato è ", x/y)
        else:
            print("L'operazione è impossibile.")
    case _:
        print("Operazione non valida.")

