from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression

wine = load_wine()

X = wine.data
y = wine.target

model = LogisticRegression(max_iter=5000)
model.fit(X, y)

predictions = model.predict(X)
#print(predictions)

score = model.score(X, y)
#print(score)

prob = model.predict_proba(X)
#print(prob)

print("Data:", wine.data)
print("Target:", wine.target)
print("Feature names:", wine.feature_names)
print("Target names:", wine.target_names)
print("Description:", wine.DESCR)
print("Keys:", wine.keys())

print("HUE")
#it's a np array and not a pandas column
print(wine.data[:, 10])

winedf = load_wine(as_frame=True).frame
print("HUE")
#it's a pandas column
print(winedf["hue"])

print(winedf["target"].value_counts()) # quanti campioni per ogni classe target
print(winedf.groupby("target")[["alcohol", "color_intensity"]].mean())   # medie per classe