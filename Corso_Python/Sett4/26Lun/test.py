from sklearn.linear_model import LogisticRegression

#Training data (features)
X = [[157], [122], [305], [144], [121], [102], [87], [21]]

#target/label
y = [1, 0, 1, 0, 0, 0, 1, 1]

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[99]]))

#attempt to make 100-150 False. AI does not know where the treshold begins,
# so it falsely assumes 99 isn't True.