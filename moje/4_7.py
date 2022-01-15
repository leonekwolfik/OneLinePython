import numpy as np

## Dane (wiersze: akcje / kolumny: ceny akcji)
X = np.array([[25, 27, 29, 30],
              [1, 5, 3, 2],
              [12, 11, 8, 3],
              [1, 1, 2, 2],
              [2, 6, 2, 2]])

min_row = min([(i, np.var(X[i, :])) for i in range(len(X))], key=lambda x: x[1])

print(f"Wierssz z minimalną wariancją: {str(min_row[0])}, wariancja={min_row[1]}")

var = np.var(X, axis=1)
print(var)
min_row = (np.where(var==min(var)), min(var))
print(min_row)
