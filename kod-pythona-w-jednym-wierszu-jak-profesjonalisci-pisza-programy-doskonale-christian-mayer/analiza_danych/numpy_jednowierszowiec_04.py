# Filtrowanie dwuwymiarowych tablic z użyciem indeksowania logicznego


## Zależności
import numpy as np

## Dane: popularne konta na Instagramie (miliony obserwujących)
inst = np.array([[232, "@instagram"],
                 [133, "@selenagomez"],
                 [59, "@victoriassecret"],
                 [120, "@cristiano"],
                 [111, "@beyonce"],
                 [76, "@nike"]])

## Jednowierszowiec
superstars = inst[inst[:,0].astype(float) > 100, 1]

## Wynik
print(superstars)
'''
['@instagram' '@selenagomez' '@cristiano' '@beyonce']
'''
