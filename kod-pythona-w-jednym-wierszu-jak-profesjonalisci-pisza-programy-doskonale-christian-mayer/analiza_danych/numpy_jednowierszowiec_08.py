# Jak tworzyć zaawansowane filtry tablic z wykorzystaniem statystyki, matematyki i logiki?


## Zależności
import numpy as np

## Dane analityczne witryny:
## (wiersz = dzień), (kolumny = użytkownicy, odrzucenia, czas trwania sesji)
a = np.array([[815, 70, 115],
              [767, 80, 50],
              [912, 74, 77],
              [554, 88, 70],
              [1008, 65, 128]])
mean, stdev = np.mean(a, axis=0), np.std(a, axis=0)
# [811.2 75.4 88. ], [152.97764543 7.98999374 29.04479299]

## Jednowierszowiec
outliers = ((np.abs(a[:,0] - mean[0]) > stdev[0])
            * (np.abs(a[:,1] - mean[1]) > stdev[1])
            * (np.abs(a[:,2] - mean[2]) > stdev[2]))

## Wynik
print(a[outliers])
'''
[[1008   65  128]]
'''
