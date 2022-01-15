from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[0, "Nie"],
              [10, "Nie"],
              [60, "Tak"],
              [90, "Tak"]])

model = LogisticRegression().fit(X[:, 0].reshape(-1, 1), X[:, 1])

print(model.predict([[2], [12], [40], [90]]))

for i in range(40):
    print(str(model.predict_proba([[i]])))
