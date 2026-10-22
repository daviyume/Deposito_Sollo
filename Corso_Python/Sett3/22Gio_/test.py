#TEST: MultiIndexing, Pivot, loc, iloc.

import pandas as pd

data_multi = {
  'Paese': ['Italia', 'Italia', 'Francia', 'Francia'],
  'Anno': [2023, 2024, 2023, 2024],
  'Vendite': [120, 135, 110, 118]
}

df_multi = pd.DataFrame(data_multi)

#rearrange for later
#pivot table is +
#'Anno' is not a column, but its values are used to represent all columns.
df = df_multi.pivot_table(values='Vendite', index='Paese', columns='Anno', aggfunc='sum')

# # Creo un indice gerarchico con Paese e Anno
df_multi = df_multi.set_index(['Paese', 'Anno'])

print("\nDataFrame con MultiIndex:")
print(df_multi)

print("MultiIndex:")
print(df_multi.index)

#print by row
print("\nTEST\n")
print(df.loc['Italia'])

#print by row (multiindex)
print("\nTEST 2\n")
print(df_multi.loc['Italia'])

#print by row in hierarchy (multiindex)
print("\nTEST 3\n")
print(df_multi.loc[('Italia', 2024)])
#primary index, then secondary child index, inserted in a tuple.
#if the value is not a string, no quotes.

#print only by secondary row (multiindex)
print("\nTEST 4\n")
print(df_multi.xs(2024, level='Anno'))

#for
#len(df)        # Number of rows
#df.shape       # (number of rows, number of columns)
#df.size        # Total number of cells (rows × columns)

#access with for
#
print("\nTEST 4\n")
print(df.iloc[0].loc[2024])
df['Risultato Recente'] = '?'
print(df)
for i in range(0, len(df)):
    match df.iloc[i].loc[2024]:
        case n if n < 120:
            print("A")
            #iloc creates a copy
            #df.iloc[i].loc['Risultato Recente'] = 'Vendita mediocre'
            df.loc[df.index[i], 'Risultato Recente'] = 'Vendita mediocre'
        case n if n >= 120:
            print("B")
            #df.iloc[i].loc['Risultato Recente'] = 'Vendita eccellente'
            df.loc[df.index[i], 'Risultato Recente'] = 'Vendita eccellente'
print(df)