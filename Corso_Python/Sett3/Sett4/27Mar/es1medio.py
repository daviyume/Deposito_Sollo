from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)

knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train,y_train)

#predict on untrained data
y_pred = knn.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, y_pred))

print("Score: ", knn.score(X_test, y_test))