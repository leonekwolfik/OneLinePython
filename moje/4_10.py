import numpy as np
from sklearn.ensemble import RandomForestClassifier

X = np.array([[9, 5, 6, "informatyka"],
              [5, 1, 5, "informatyka"],
              [8, 8, 8, "informatyka"],
              [1, 10, 7, "literatura"],
              [1, 8, 1, "literatura"],
              [5, 7, 9, "sztuka"],
              [1, 1, 6, "sztuka"]])

Forest = RandomForestClassifier(n_estimators=10).fit(X[:, :-1], X[:,-1])

students = Forest.predict([[8,6,5],
                           [3,7,9],
                           [2,2,1]])

print(students)
