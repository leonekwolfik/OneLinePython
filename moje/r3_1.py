import random

import numpy as np

a = np.array([1, 2, 3])


b = np.array([[1, 2],
              [3, 4]])


c = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])




a = np.array([[random.randint(0,3) for _ in range(3)] for _ in range(3)])
b = np.array([[random.randint(0,3) for _ in range(3)] for _ in range(3)])

print(a, b, sep='\n\n')

# print(a+b, a-b, a*b, a/b, sep='\n\n')

print(np.max(a))
print(np.min(a))
print(np.average(a))
