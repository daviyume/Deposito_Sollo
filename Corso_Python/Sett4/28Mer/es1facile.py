from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

X, y = load_digits(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

knr = KNeighborsRegressor(n_neighbors=1)
knr.fit(X_train, y_train)

print("Score train: ", knr.score(X_train, y_train))
print("Score test: ", knr.score(X_test, y_test))

#Il modello non è in overfitting perché l'accuratezza nel test non è bassa.