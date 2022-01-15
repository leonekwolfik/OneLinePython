import random

import numpy as np

a = np.array([random.randint(0,100) for _ in range(7)])
# print(a)
# print(a[:])
# print(a[2:])
# print(a[1:4])
# print(a[2:-2])
# print(a[::2])
# print(a[::-1])
# print(a[:1:-2])
# print(a[::-2])
# print(a[-1:1:-2])

a = np.array([[random.randint(0,20) for _ in range(4)] for _ in range(4)])
print(a)

print(a[:, 2])
print(a[1, :])
print(a[1, ::2])
print(a[:,:-1])
print(a[:-2])
print(a[:-2,:])