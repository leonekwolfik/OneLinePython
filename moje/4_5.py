from sklearn.neural_network import MLPRegressor
import numpy as np

## Dane z ankiety (TYDZIEŃ, LATA, KSIĄŻKI, PROJEKTY, ZAROBKI, OCENA)
X = np.array(
    [[20, 11, 20, 30, 4000, 3000],
     [12, 4, 0, 0, 1000, 1500],
     [2, 0, 1, 10, 0, 1400],
     [35, 5, 10, 70, 6000, 3800],
     [30, 1, 4, 65, 0, 3900],
     [35, 1, 0, 0, 0, 100],
     [15, 1, 2, 25, 0, 3700],
     [40, 3, -1, 60, 1000, 2000],
     [40, 1, 2, 95, 0, 1000],
     [10, 0, 0, 0, 0, 1400],
     [30, 1, 0, 50, 0, 1700],
     [1, 0, 0, 45, 0, 1762],
     [10, 32, 10, 5, 0, 2400],
     [5, 35, 4, 0, 13000, 3900],
     [8, 9, 40, 30, 1000, 2625],
     [1, 0, 1, 0, 0, 1900],
     [1, 30, 10, 0, 1000, 1900],
     [7, 16, 5, 0, 0, 3000]])

neutral_net = MLPRegressor(max_iter=10000).fit(X[:, :-1], X[:, -1])

res = neutral_net.predict([[0, 0, 0, 0, 0]])
print(res)

res = neutral_net.predict([[20, 0, 0, 0, 0]])
print(res)