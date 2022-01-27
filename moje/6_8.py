from functools import reduce

n = 10

fibs = reduce(lambda x, _: x + [x[-2] + x[-1]], range(n - 2), [0, 1])

print(fibs)
