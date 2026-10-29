#2.1
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd

data = {
    'Età': [20, 30, 33, 45, 22, 64, 44, 70],
    'Reddito annuo': [15000, 44000, 36000, 80000, 120000, 60000, 22000, 16000],
    'Figli': [0, 2, 0, 3, 1, 3, 2, 1]
}

df = pd.DataFrame(data)

scaler = StandardScaler(copy=False).set_output(transform="pandas")

#scaler.fit(df)
#scaler.transform(df)

#overwrite esplicito per df
df = scaler.fit_transform(df)

df = df.round(2)

print(df)