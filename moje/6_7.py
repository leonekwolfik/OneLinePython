from functools import reduce

n = 100

s1 = set(range(1, n))
s2 = set(range(2, n + 1))

print(s1 - s2)
print(s2 - s1)

# p = reduce(lambda a, b: print(a, b), set(range(1, n)), set(range(1, n)))

print(set(range(3 ** 2, n, 3)))

print(22 in set(range(1, 10)))

primes = reduce(lambda r, x: r - set(range(x ** 2, n, x)) if x in r else r, range(2, int(n ** 0.5) + 1), set(range(2, n)))
primes2 = reduce(lambda r, x: r - set(range(x ** 2, n, x)), range(2, int(n ** 0.5) + 1), set(range(2, n)))

print(primes)
print(sorted(primes2))

assert sorted(primes2) == sorted(primes)

print(reduce(lambda a,b : a+b, range(1,5), 6))

it = iter(range(1,10))
next(it)
for i in it:
    print(i)
