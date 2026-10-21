import pandas as pd

# Dati di esempio
data = {
    'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Tastiera'],
    'Vendite': [100, 200, 150, 300, 250]
}


df = pd.DataFrame(data)
# Creazione della tabella pivot
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='sum')

print(df)
print(pivot_df)

#values: valore di incrocio
#index: indice
#columns: colonne
#aggfunc: sceglie come rappresentare valori che si sovrappongono (mean, sum)

#groupby raggruppa per prodotto e sceglie come sovrapporre i dati
grouped_df = df.groupby('Prodotto').sum()
print(grouped_df)