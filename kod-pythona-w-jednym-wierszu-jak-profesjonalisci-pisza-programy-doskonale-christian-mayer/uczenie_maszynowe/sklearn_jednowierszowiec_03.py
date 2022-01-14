# Algorytm k-średnich


## Zależności
from sklearn.cluster import KMeans
import numpy as np

## Dane (Praca (h) / Wynagrodzenie (zł))
X = np.array([[35, 7000], [45, 6900], [70, 7100],
              [20, 2000], [25, 2200], [15, 1800]])

## Jednowierszowiec
kmeans = KMeans(n_clusters=2).fit(X)

## Wynik
cc = kmeans.cluster_centers_
print(cc)
'''
[[  20. 2000.]
 [  50. 7000.]]
'''
