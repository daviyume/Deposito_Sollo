#2.1
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np
from sklearn.preprocessing import MinMaxScaler

bc = load_breast_cancer()

#bc.data contains features. bc.target contains targets.
print(bc.data)

cmin = 0
cmax = 0

#trova colonna con varianza maggiore e minore
for c in range(bc.data.shape[1]):
    if np.std(bc.data[:, c]) > np.std(bc.data[:, cmax]):
        cmax = c
    if np.std(bc.data[:, c]) < np.std(bc.data[:, cmin]):
        cmin = c

print("Feature con la scala più grande: ", bc.feature_names[cmax])
print("Feature con la scala più piccola: ", bc.feature_names[cmin])

#all values transformed to 0-1 scale
mms = MinMaxScaler(feature_range=(0, 1), copy=False).fit(bc.data)
mms.transform(bc.data)

print(bc.data)