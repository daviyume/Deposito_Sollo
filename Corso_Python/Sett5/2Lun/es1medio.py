from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler

def getScale(feature):
    return feature.max() - feature.min()

#load bunch
fch = fetch_california_housing(as_frame=True)

X, y = fch.data, fch.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=20)

# * non scalato
linreg = LinearRegression()
linreg.fit(X_train, y_train)

#colonna, index
coefficienti = pd.Series(linreg.coef_, index=fch.feature_names)
coefficienti = coefficienti.sort_values()
print("Coefficienti w linreg (non scalato): V\n", coefficienti)

# * scalato
scaler = StandardScaler()
scaler.fit(X_train)
X_train_s = scaler.transform(X_train)

linreg = LinearRegression()
linreg.fit(X_train_s, y_train)

coefficienti = pd.Series(linreg.coef_, index=fch.feature_names)
coefficienti = coefficienti.sort_values()
print("Coefficienti w linreg (scalato): V\n", coefficienti)

#La risposta è AveBedrms per il modello non scalato e MedInc per il modello scalato.

print("\nScale AveBedrms: ", getScale(fch.frame['AveBedrms']))
print("Scale MedInc: ", getScale(fch.frame['MedInc']))

#Questo perché il primo ha una scala di circa 33, mentre il secondo di circa 14:
# i risultati vengono dunque lievemente incrementati proporzionalmente alla scala.