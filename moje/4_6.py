from sklearn import tree
import numpy as np

## Dane: wyniki studentów (matematyka, język, kreatywność) --> kierunek studiów
X = np.array([[9, 5, 6, "informatyka"],
              [1, 8, 1, "lingwistyka"],
              [5, 7, 9, "sztuka"]])

Tree = tree.DecisionTreeClassifier().fit(X[:, :-1], X[:, -1])

student_0 = Tree.predict([[8, 6, 5]])
print(student_0)

student_1 = Tree.predict([[3, 7, 9]])
print(student_1)
