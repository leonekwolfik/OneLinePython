# Rozgłaszanie, przypisywanie do wycinków i przekształcanie w celu oczyszczenia co i-tego elementu tablicy


## Zależności
import numpy as np

## Dane czujnika (pon., wt., śr., czw., pt., sob., niedz.)
tmp = np.array([1, 2, 3, 4, 3, 4, 4,
                5, 3, 3, 4, 3, 4, 6,
                6, 5, 5, 5, 4, 5, 5])

## Jednowierszowiec
tmp[6::7] = np.average(tmp.reshape((-1,7)), axis=1)

## Wynik
print(tmp)
'''
[1 2 3 4 3 4 3 5 3 3 4 3 4 4 6 5 5 5 4 5 5]
'''
