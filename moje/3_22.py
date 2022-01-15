import numpy as np

a = np.array([[1,6,2],
              [5,1,1],
              [8,0,1]])

print(np.sort(a, axis=0))
print(np.sort(a, axis=1))
print(np.sort(np.sort(a, axis=0), axis=1))
print(np.sort(np.sort(a, axis=1), axis=0))