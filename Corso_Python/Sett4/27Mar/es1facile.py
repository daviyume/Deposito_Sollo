from sklearn.neighbors import KNeighborsClassifier

# Ogni riga: [peso in grammi, diametro in cm]
X = [[25, 55],[30, 60],[5, 20],[10, 35],[4.5, 23],[5, 25],[3.5, 20],[40, 60]]
y = ["cane", "cane", "gatto", "cane", "gatto", "gatto", "gatto", "cane"]

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X,y)

print(knn.predict([[65, 60], [3.7, 26]]))