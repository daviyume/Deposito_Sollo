#merge
import pandas as pd

df = pd.read_csv("Corso_Python/dati/products-10-simple.csv")
df2 = pd.read_csv("Corso_Python/dati/products-10-simple2.csv")

# square brackets for multiple columns
dfmerged = pd.merge(df, df2, on=['Name', 'Category', 'Price'], how='outer')

print(dfmerged)


'''
pd.merge(df1, df2, on='ID', how='inner')  # Only matching IDs (default)
pd.merge(df1, df2, on='ID', how='left')   # Keep all rows from df1
pd.merge(df1, df2, on='ID', how='right')  # Keep all rows from df2
pd.merge(df1, df2, on='ID', how='outer')  # Keep all IDs from both
    ('outer' sets sort to True by default if only 1 column chosen)
'''

dfcrisis = dfmerged
dfcrisis['Price'] = dfcrisis['Price'].apply(lambda x: x*2)

print()
print(dfcrisis)