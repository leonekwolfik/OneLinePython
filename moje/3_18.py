import numpy as np

a = np.array([4] * 16)
print(a)

a[1::] = [42] * 15
print(a)

b = np.array(16 * [4])
print(b)

c = np.array([4])
c = c * 16

print(c)

a = np.array([4] * 16)
print(a)
a[1:8:2] = 16
print(a)

a = np.array([i for i in range(6)])
print(a)
print(a.reshape((2,3)))
print(a.reshape((2, -1)))
