import pandas as pd
import os

# Creazione di dati per DataFrame
data = {
    'Nome': ['Alice', 'Bob', 'Carla'],
    'Età': [25, 30, 22],
    'Città': ['Roma', 'Milano', 'Napoli']
}

# aggiunta di una chiave al dizionario
data["Sesso"] = ["F","M","F"]

# Creazione di DataFrame
df = pd.DataFrame(data)

print("Prime 2 righe: ")
print(df.head(2)) #default: 5
print("Ultime 6 righe: ")
print(df.tail(6)) #default: 5

#statistiche per numeri.
# colonne miste non contano
print(df.describe())

#descrizione generale per tutte le colonne
print(df.info())






path = os.path.dirname(os.path.abspath(__file__))+"/"
nomefile = path+"studenti.csv"

testo = pd.read_csv(nomefile)

print("TESTO CSV:\n"+str(testo))

testo["Sesso"] = ["M", "M", "F", "F", "M", "F", "M", "F", "M", "F"]

#C'è questa colonna? No. Viene creata
#operazione di broadcasting
testo["promosso"] = testo["voto"] >= 6

#Viene estratta la lista dei voti per il calcolo
print("Media:", testo["voto"].mean())

#controlla se il valore testo["voto"] è maggiore di 7
#Viene estratto ogni elemento e tutte le sue proprietà.
print("Alunni con voti eccellenti: ", testo[testo["voto"] > 7])

testo = testo.drop_duplicates()
testo = testo.dropna()

print("TESTO CSV dopo modifica:\n"+str(testo))
nomenuovofile = path+"studentinuovo.csv"
testo.to_csv(nomenuovofile)

#persone
