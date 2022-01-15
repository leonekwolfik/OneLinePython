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

print(mean, stdev)

outliers = (
    (np.abs(a[:,0] - mean[0]) > stdev[0]) * (np.abs(a[:,1] - mean[1]) > stdev[1]) * (np.abs(a[:,2] - mean[2]) > stdev[2])
)

print(a[outliers])

outliers2 = np.prod((np.abs(a[:,i] - mean[i]) > stdev[i]) for i in range(3))
print(a[outliers2])