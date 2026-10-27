#1.6
from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.8, random_state=0)

klist = [1, 5, 20]
weightlist = ["uniform", "distance"]

bestk = 0
bestw = 0
bestscore = -1

for k in klist:
    for w in weightlist:
        print("\nk: ",k,"weights: ",w)
        knr = KNeighborsRegressor(n_neighbors=k, weights=w)
        knr.fit(X_train, y_train)
        score = knr.score(X_test, y_test)
        print("Score: ", score)

        if score > bestscore:
            bestk = k
            bestw = w
#test combinations

print("\nLa combinazione migliore è di ", bestk, " per k & ", bestw, " per weights!")