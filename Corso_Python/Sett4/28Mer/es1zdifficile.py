#1.7
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

plt.plot()
X, y = load_wine(return_X_y=True)

#accs = np.empty(5, 60)

for rs in range(100, 501, 100):

    accs = []
    ks = []
    for k in range(1, 61):
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, random_state=rs)
        knc = KNeighborsClassifier(n_neighbors=k)
        knc.fit(X_train, y_train)

        accs.append(knc.score(X_test, y_test))
        ks.append(k)

    #ogni linea rappresenta accs e ks con un random state diverso
    plt.plot(ks, accs, label=rs)

plt.xlabel("k")
plt.ylabel("accuratezza")
plt.title("Relazione k e accuratezza")
plt.legend()

plt.show()

#Nel grafico osserviamo stime piuttosto diverse tra loro, con picchi diversi per ogni colore.
#Possiamo concludere che il random state può variare il risultato in modo significativo,
#ed è necessario effettuare diverse stime.