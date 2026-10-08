# Stampa sequenza fibonacci fino a n inserito dall'utente.

def nextfib (n: int):
    print(lista)
    return (lista[n-1])+(lista[n-2])



x = int(input("Inserisci il numero a cui arrivare con la sequenza Fibonacci: "))
lista = [0, 1]

num = 1
cont = 2

while num <= x:
    num = nextfib(cont) #calcola somma dei 2 precedenti
    lista.append(num)
    cont+=1
