# Klasyfikacja z maszynami wektorów nośnych


## Zależności
from sklearn import svm
import numpy as np

## Dane: wyniki studentów (matematyka, język, kreatywność) --> kierunek studiów
X = np.array([[9, 5, 6, "informatyka"],
              [10, 1, 2, "informatyka"],
              [1, 8, 1, "literatura"],
              [4, 9, 3, "literatura"],
              [0, 1, 10, "sztuka"],
              [5, 7, 9, "sztuka"]])

## Jednowierszowiec
svm = svm.SVC().fit(X[:,:-1], X[:,-1])

## Wynik
student_0 = svm.predict([[3, 3, 6]])
print(student_0)

student_1 = svm.predict([[8, 1, 1]])
print(student_1)

'''
['sztuka']
['informatyka']
'''
