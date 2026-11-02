import pandas as pd

df = pd.DataFrame({
    "km": [45000, 120000, 80000, 150000, 30000, 95000],
    "anni": [3, 8, 5, 10, 2, 6],
    "cilindrata": [1200, 1600, 1400, 2000, 1000, 1800],
    "prezzo": [18000, 9500, 13000, 7000, 21000, 11500],
    "incidentata": ["no", "sì", "no", "sì", "no", "no"]
})

print(df)

#quanto costerà?
X = df.drop(columns=["prezzo"])
y = df["prezzo"]
#parametri X e target y

print(X.shape, y.shape)

#è stata incidentata?
X = df.drop(columns=["incidentata"])
y = df["incidentata"]
#parametri X e target y
print(X.shape, y.shape)