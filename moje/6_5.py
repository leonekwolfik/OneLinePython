from functools import reduce

s = [1, 2, 3]

ps = lambda s: reduce(lambda P, x: P + [subset | {x} for subset in P], s, [set()])

print(ps(s))

def reduce_f(P, x):
    result = []
    for subset in P:
        print(subset)
        result.append([subset | {x}])
    return P + result

ps2 = lambda s: reduce(reduce_f, s, [set()])

print(ps2(s))
