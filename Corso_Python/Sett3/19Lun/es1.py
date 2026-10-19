#utente può creare file, modificare, leggere, svuotare, ripetibile
#extra: rinominabile

#from os import getcwd
#print(getcwd())

import os

path = "Corso_Python/Sett3/19Lun/"

#region filecontrol
def Crea():
    print("CREA")
    nome = input("Nome del file da creare: ")
    file = open(path+nome, "x")
    file.close()

def Modifica():
    nome = input("Nome del file da modificare: ")
    file = open(path+nome, "w")
    contenuto = input("Contenuto: ")
    file.write(contenuto)
    file.close()

def Leggi():
    nome = input("Nome del file da leggere: ")
    file = open(path+nome, "r")
    print(file.readline())
    file.close()

def Aggiungi():
    nome = input("Nome del file a cui aggiungere: ")
    contenuto = input("Contenuto da appendere: ")
    with open(path+nome, "a") as file:
        file.write(contenuto)

def Svuota():
    nome = input("Nome del file da svuotare: ")
    file = open(path+nome, "w")
    file.write("")
    file.close()

def Rinomina():
    nome = input("Nome del file da rinominare: ")
    nuovonome = input("Nuovo nome: ")
    os.rename(path+nome, path+nuovonome)
#endregion

while True:
    match(input("Inserisci l'azione: [C] Crea  [M] Modifica  [L] Leggi  [A] Aggiungi  [S] Svuota  [R] Rinomina: ").upper()):
        case 'C':
            Crea()
        case 'M':
            Modifica()
        case 'L':
            Leggi()
        case 'A':
            Aggiungi()
        case 'S':
            Svuota()
        case 'R':
            Rinomina()
        case 'X':
            break
        case _:
            print("Input invalido.")