from sklearn.neighbors import KNeighborsRegressor
import numpy as np

## Dane (Powierzchnia mieszkania (metry kwadratowe) / Cena mieszkania (zł))
X = np.array([[35, 120000], [45, 180000], [40, 200000],
              [35, 140000], [25, 130000], [40, 160000]])

print(X[:,0])
KNN = KNeighborsRegressor(n_neighbors=3).fit(X[:,0].reshape(-1,1), X[:,1])

res = KNN.predict([[30]])
print(res)