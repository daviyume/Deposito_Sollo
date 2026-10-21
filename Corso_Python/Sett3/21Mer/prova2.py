import pandas as pd
import os
path = "Corso_Python/dati/products-10-simple.csv"

df = pd.read_csv(path)

df['Available'] = True
df['Expensive'] = df['Price'] > 100
df['Price'].fillna(df['Price'].mean(), inplace=True)

df = df.drop_duplicates()
df = df.dropna()

print(df)