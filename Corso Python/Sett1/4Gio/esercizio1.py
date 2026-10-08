# genera un  numero casuale da far indovinare all'utente, con indizio maggiore/minore
# a ogni risposta. Gioco termina quando indovina o esce.

import random

finito = False
tesoro = random.randint(1, 100)
att = 1

def confronta(n: int):

    if guess == tesoro:
        print("Congratulazioni! Hai vinto in  ", att, " tentativi.")
        return True
    if guess == 0:
        print("Hai perso.")
        return True

    if guess > tesoro:
        print("Un po' di meno...")
    else:
        print("Un po' di più...")
    return False


print("Indovina il numero da 1 a 100! (inserisci 0 se vuoi arrenderti)")
while not finito:
    print("Attempt ", att, ":")
    guess = int(input())

    finito = confronta(guess)

    att+=1

print("Fine.")