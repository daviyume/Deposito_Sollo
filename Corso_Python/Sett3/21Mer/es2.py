import pandas as pd


data = {
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Monitor', 'Tastiera', 'Monitor', 'Mouse', 'Monitor'],
    'Quantità': [10, 5, 15, 3, 8, 6, 20, 4],
    'Prezzo Unitario': [15, 30, 15, 150, 30, 150, 15, 150],
    'Città': ['Roma', 'Milano', 'Roma', 'Napoli', 'Milano', 'Roma', 'Napoli', 'Napoli']
}

df = pd.DataFrame(data)
print(df)

#tot
df['Totale Vendite'] = df['Quantità']*df['Prezzo Unitario']

#dfg raggruppa i prodotti e li utilizza come indici.
#dfg contiene come colonne solamente il totale vendite, con valori sommati per ogni
# sovrapposizione.
# reset_index per riaggiungere indice
print("DFG")

# single brackets: series
#dfg = df.groupby('Prodotto')['Totale Vendite'].sum().reset_index()

# double brackets = dataframe with real column

#4 Prodotto più venduto
dfgprod = df.groupby('Prodotto')[['Totale Vendite']].sum()
print(dfgprod)
#vendita massima
print("\nVendita massima: ", dfgprod['Totale Vendite'].max())

print("\nProdotto più venduto: ")
#print(dfg.index[dfg['Totale Vendite'] == dfg['Totale Vendite'].max()])
print(dfgprod['Totale Vendite'].idxmax())
#.idxmax() restituisce l'indice del valore massimo in una colonna

#5 Citta con più vendite
dfgcitta = df.groupby('Città')[['Totale Vendite']].sum()
print("\nCittà con più vendite: ")
print(dfgcitta['Totale Vendite'].idxmax())

#6 Vendite superiori a 600
dfgvenditegrandi = dfgprod[dfgprod['Totale Vendite'] > 600]
print("Vendite grandi")
print(dfgvenditegrandi)

#8 Vendite per ogni città
print("\nVendite per ogni città:\n")
print(dfgcitta)