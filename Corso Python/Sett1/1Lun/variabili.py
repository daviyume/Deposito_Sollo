#Variabili e tipi di variabili

#Numeri: interi e float
x = 3
pi= 3.14

#Stringhe. Sono array di caratteri
nome = "Mario"
print(nome[1]) #carattere in cella 1 è il secondo, ovvero 'a'

cognome = "Super"
nominativo = cognome + " " + nome #concatenazione di string

print("Nominativo appello: ", nominativo)

#Rimpiazzare. Funzione che viene utilizzata con la stringa
nominativo = (nominativo.replace("Mario", "Luigi"))

print(nominativo)
#lunghezza della stringa. Funzione che ha come parametro la stringa
print("lunghezza nominativo: ", len(nominativo))

#booleani: true o false.
adulto = True
#Operatori di confronto
'''
== uguale
!= diverso
< minore
> maggiore
<= minore/uguale
>= maggiore uguale
'''

print(pi>x)
print(x==pi)

z = 3

print(not(pi>x and x!=z))
print(x==z or pi=="3.14")