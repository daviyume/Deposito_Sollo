import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

plt.rcParams['figure.figsize'] = [10, 6]  
# Imposta la dimensione predefinita delle figure

plt.rcParams['figure.dpi'] = 100          
# Imposta la risoluzione delle figure in DPI

plt.rcParams['figure.facecolor'] = '#AACCFF'  # Colore di sfondo della figura
#sns.set_theme(style="whitegrid")

df = pd.DataFrame(
    {
    'Temperature': [
        12, 13, 11, 10, 14, 15, 13, 12, 11, 14,
        16, 17, 15, 13, 12, 10, 11, 14, 15, 16,
        18, 17, 16, 14, 13, 12, 11, 13, 15, 16, 14
    ]
    },
    index = pd.date_range(start='2026-01-01', periods=31, freq='D')
)

print("Temperatura massima")
tmax = df['Temperature'].max()
print(tmax)

print("\nTemperatura minima")
tmin = df['Temperature'].min()
print(tmin)

print("\nTemperatura centrale")
tmid = df['Temperature'].median()
print(tmid)

print("\nTemperatura media")
tmean = df['Temperature'].mean()
print(tmean)