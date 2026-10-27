#*EX AVANZATO 1.7

import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = make_moons(n_samples=400, noise=0.35, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

valori_k = range(1, 252, 5)                         # da 1 fino a quasi tutto il training (280 punti)
acc_train, acc_test = [], []	#log accuracies with training and test for every k
for k in valori_k:
    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    acc_train.append(knn.score(X_train, y_train))
    acc_test.append(knn.score(X_test, y_test))

plt.plot(valori_k, acc_train, label="training")
plt.plot(valori_k, acc_test, label="test")
plt.xlabel("k (a sinistra modello complesso, a destra modello semplice)")
plt.ylabel("accuratezza")
plt.legend(); plt.title("Curva di complessità del KNN")
plt.show()
