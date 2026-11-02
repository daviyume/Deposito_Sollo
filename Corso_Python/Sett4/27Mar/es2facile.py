#1.6
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_wine

wines = load_wine()

knc = KNeighborsClassifier(n_neighbors=4)
#knc.fit(np.delete(wines.data, 100, axis=0), np.delete(wines.target, 100, axis=0))
#remove itself
knc.fit(wines.data, wines.target)

dist, idxs = knc.kneighbors(wines.data[[100]]) #must be 2d to select whole row. To select row, [[]]
dist = dist[:, 1:].round(2).ravel()
idxs = idxs[:, 1:].ravel()
#rimuovi 1o elemento
#ravel: turn to 1d array

print("Distanze: ", dist)
print("Indici: ", idxs)
print("Classi dei vicini: ", wines.target[idxs]) #label of target y (class)

predizioni = knc.predict(wines.data[idxs])
print("Predizione:", predizioni)