_initial_missing = object()

def reduce2(function, sequence, initial=_initial_missing):
    it = iter(sequence)

    if initial is _initial_missing:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError(
                "reduce() of empty iterable with no initial value") from None
    else:
        value = initial

    for element in it:
        value = function(value, element)

    return value

unsorted = [33, 2, 3, 45, 6, 54, 33]

q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []

print(q(unsorted))

r = reduce2(lambda l, x: [i for i in l if i < x], [33] * len(unsorted), unsorted)
print(r)

