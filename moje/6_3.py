n = 5

factorial = lambda n: n * factorial(n - 1) if n > 1 else 1

print(factorial(n))


def fact(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(fact(5))


for i in range(10):
    assert factorial(i) == fact(i)
    