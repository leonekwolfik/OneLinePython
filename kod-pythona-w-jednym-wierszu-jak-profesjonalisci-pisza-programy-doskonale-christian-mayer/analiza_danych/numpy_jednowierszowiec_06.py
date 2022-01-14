# Kiedy w NumPy używać funkcji sort(), a kiedy argsort()?


## Zależności
import numpy as np

## Dane: wyniki testu dla poszczególnych uczniów
sat_scores = np.array([1100, 1256, 1543,
                       1043, 989, 1412, 1343])
students = np.array(["Jan", "Robert", "Alicja",
                     "Józef", "Joanna", "Franciszek", "Karol"])

## Jednowierszowiec
top_3 = students[np.argsort(sat_scores)][:-4:-1]

## Wynik
print(top_3)
'''
['Alicja' 'Franciszek' 'Karol']
'''
