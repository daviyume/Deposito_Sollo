from sklearn.datasets import load_breast_cancer
import pandas as pd

#as frame per caricare dataframe e .frame per accedere solo al df
df = load_breast_cancer(as_frame=True).frame

print("Numero campioni: ")
print(len(df))
print("Numero features: ")
print(len(df.columns)-1) #elimina features

print("Classi")
print(df["target"].unique())
print("Prime 5 feature")
print(df.columns[:5].tolist())
#print(df.iloc[:, :5])