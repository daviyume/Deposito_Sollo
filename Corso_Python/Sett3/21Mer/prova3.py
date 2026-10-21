import pandas as pd
import os

import warnings
warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)

path = "Corso_Python/dati/products-10-simple.csv"

statistiche = {
    'Paese': ['Italia', 'Italia', 'Francia', 'Francia'],
    'Anno': [2023, 2023, 2023, 2024],
    'Vendite': [120, 135, 110, 118]
}

df = pd.DataFrame(statistiche)

#Multi Index
#index utilizza un attributo come indice vvv Index, Series
#se più serie hanno lo stesso indice, l'indice si raggruppa in uno
df = df.set_index(['Paese', 'Anno'])

print(df)

# # Seleziono tutte le righe per Italia
print("\nTutte le righe per Italia:")
print(df.loc['Italia'])

# # Seleziono il valore specifico per Francia nel 2024
print("\nValore Vendite per Francia, 2024:")
print(df.loc[('Francia', 2024), 'Vendite'])

#riorganizzazione tabella (spiegazione in prova)
print("PIVOT")
pivot_df = df.pivot_table(values='Vendite', index='Paese', columns='Anno', aggfunc='mean')
print(pivot_df)