from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split

X, y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=144)

modelslist = [KNeighborsClassifier(n_neighbors=5), DecisionTreeClassifier(random_state=0)]
scalerslist = [StandardScaler(), MinMaxScaler(), RobustScaler()]

for model in modelslist:
    print()
    for scaler in scalerslist:
        #scale
        X_train_scaled = scaler.fit_transform(X_train) #train on X_train and transform
        X_test_scaled = scaler.transform(X_test) #transform X_test

        #model
        model.fit(X_train_scaled, y_train)
        print("Model: "+str(model)+"\tScaler: "+str(scaler))
        print("Score: ", model.score(X_test_scaled, y_test))
        print("X_test_scaled :"+str(X_test_scaled[0, 0:4]))
