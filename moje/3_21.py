import random

import numpy as np

a = np.array([random.randint(1,10) for _ in range(10)])

print(a)
print(np.sort(a))
print(np.argsort(a))