import pandas as pd
import os
path = "Corso_Python/dati/persone.csv"
newpath = os.path.dirname(os.path.abspath(__file__))+"/personenuovo.csv"

df = pd.read_csv(path)

print("stampa prime e ultime 5 righe")
print(df.head())
print(df.tail())

print("stampa tipi delle colonne")
print(df.dtypes)

print("Statistiche numeriche")
print(df.describe())

df = df.drop_duplicates()

#riempe celle vuote di salario in df con media del salario in df
#inplace indica che modifica il df esistente invece di crearne uno nuovo.

df['salario'].fillna(df['salario'].mean(), inplace=True)

df['maggiorenne'] = df['eta'] >= 18
#np.select(conditions, choices)

print(df)