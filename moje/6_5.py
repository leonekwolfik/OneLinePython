from functools import reduce

s = [1, 2, 3]

ps = lambda s: reduce(lambda P, x: P + [subset | {x} for subset in P], s, [set()])

print(ps(s))


# print([subset | {5} for subset in [set([1,2,3,4])]])
# print([set()] + [{1} | {2}])
