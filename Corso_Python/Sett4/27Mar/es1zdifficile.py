#es 1.5
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


X, y = load_digits(return_X_y=True)




df = pd.DataFrame({
        'Accuratezza': [0.0, 0.0, 0.0],
        'Random State': [0, 0, 0]
     },
    index=["KNN", "Tree", "Forest"])

#random state 20 default. Will change later for each model.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=20)

#dictionary
models = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Tree": DecisionTreeClassifier(random_state=144),
    "Forest": RandomForestClassifier(random_state=144),
    }


df1 = df
print("TEST RANDOM STATES 20")

for nm, model in models.items():
    model.fit(X_train,y_train)
    acc = model.score(X_test, y_test)
    df1.loc[nm, 'Accuratezza'] = acc
    df1.loc[nm, 'Random State'] = 20

df1 = df1.sort_values(by='Accuratezza')
print(df1)

df2 = df
rs = 0
print("\nTEST RANDOM STATE 0, 40, 80")
for nm2, model in models.items():
    X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y, test_size=0.4, random_state=rs)
    model.fit(X_train2,y_train2)
    acc = model.score(X_test, y_test)
    df2.loc[nm2, 'Accuratezza'] = acc
    df2.loc[nm2, 'Random State'] = rs
    rs+=40

df2 = df2.sort_values(by='Accuratezza')
print(df2)

#La classifica dei modelli cambia?
#Risposta: sì, ma non cambia la performance media di ogni algoritmo.