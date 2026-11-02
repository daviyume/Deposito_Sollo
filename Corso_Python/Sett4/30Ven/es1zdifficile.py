#2.5
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

#weights must fit classes
X, y = make_classification(n_samples=1000, n_features=4, n_informative=4, 
                           n_redundant=0, n_classes=2, random_state=144,
                           weights=[0.03, 0.97])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=60, random_state=144, stratify=y)

scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_s = scaler.transform(X_train)
X_test_s = scaler.transform(X_test)

modelslist = [DummyClassifier(), KNeighborsClassifier(n_neighbors=5), DecisionTreeClassifier()]

for model in modelslist:
    model.fit(X_train_s, y_train)
    print("\n MODELLO ", str(model))

    y_pred = model.predict(X_test_s)
    y_proba = model.predict_proba(X_test_s)
    for treshold in [0.5, 0.3, 0.2, 0.1]:
        print("\nTreshold: ", treshold)
        #if probability passes treshold, bool is converted as 100% probability;
        # otherwise, it's 0% probability
        y_pred = (y_proba[:, 1] >= treshold).astype(int)
        
        print("Accuracy score: ", accuracy_score(y_test, y_pred))
        print("Precision score: ", precision_score(y_test, y_pred))
        print("Recall score: ", recall_score(y_test, y_pred))
        print("F1 score: ", f1_score(y_test, y_pred))

    #print("Predict proba: ", model.predict_proba(X_test))
    #display probablity of class 0 or class 1