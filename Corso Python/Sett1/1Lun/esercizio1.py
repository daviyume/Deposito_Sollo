'''
Andare a creare una variabile per ogni tipo che prende in input ogni
 tipo basilare e stamparli tutti in unico print,
   dopodichè far inserire all'utente due numeri e
     comprovare gli operatori, logici e di confronto.
'''
x = int(input("Inserisci un numero intero: "))
y = float(input("Inserisci un numero decimale: "))
nome = input("Inserisci il tuo nome: ")
lettera = input("Inserisci una lettera: ")
bool_s = input("Sai scrivere o no? (s/n)")=='s'

print(x, y, nome, lettera, bool_s)