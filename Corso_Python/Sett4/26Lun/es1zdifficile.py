import pandas as pd
import numpy as np
from sklearn.datasets import load_wine, load_diabetes

#datasets are Bunch objects. The tables are listed in data section.
wine = load_wine()
diabetes = load_diabetes()

print("WINE, Campioni e feature:")
print(wine.data.shape)

print("DIABETES, Campioni e feature:")
print(diabetes.data.shape)

#controlla quanti valori unici
print("Problema WINE è di:")
if len(set(wine.target)) > 2:
    print("Regressione")
else:
    print("Classificazione")

print("Problema DIABETES è di:")
if len(set(diabetes.target)) > 2:
    print("Regressione")
else:
    print("Classificazione")