# Warunkowe przeszukiwanie tablic, filtrowanie i rozgłaszanie w celu wykrywania elementów odstających


## Zależności
import numpy as np

## Dane: wartości wskaźnika jakości powietrza AQI (wiersz = miasto)
X = np.array(
    [[ 42, 40, 41, 43, 44, 43 ], # Hongkong
     [ 30, 31, 29, 29, 29, 30 ], # Nowy Jork
     [ 8, 13, 31, 11, 11, 9 ], # Berlin
     [ 11, 11, 12, 13, 11, 12 ]]) # Montreal
cities = np.array(["Hongkong", "Nowy York", "Berlin", "Montreal"])

## Jednowierszowiec
polluted = set(cities[np.nonzero(X > np.average(X))[0]])

## Wynik
print(polluted)
'''
{'Berlin', 'Hongkong', 'Nowy Jork'}
'''
