from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

X, y = make_circles(n_samples=500, noise=0.25, factor=0.5, random_state=0)

#60/20/20
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2)

X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25)

bestscore= 0
bestk = 0
for k in range(1, 51):
    knr = KNeighborsRegressor(n_neighbors=k)
    knr.fit(X_train, y_train)
    score = knr.score(X_val, y_val)
    print("Punteggio per "+str(k)+" : "+str(score))
    if score > bestscore:
        bestscore = score
        bestk = k

print("k migliore è: ", bestk)

#testfinale
print("\nTEST")
knr = KNeighborsRegressor(n_neighbors=bestk)
knr.fit(X_train, y_train)
finalscore = knr.score(X_test, y_test)
print("Punteggio per "+str(bestk)+" : "+str(finalscore))