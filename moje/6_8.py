from functools import reduce

n = 10

fibs = reduce(lambda x, _: x + [x[-2] + x[-1]], range(n - 2), [0, 1])
print(fibs)

x = [0, 1]
fibs2 = x[0:2] + [x.append(x[-1] + x[-2]) or x[-1] for i in range(n-2)]
print(fibs2)
