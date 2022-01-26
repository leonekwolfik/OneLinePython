abc = "abcdefghijklmnopqrstuvwxyz"
s = "xrosjaniexnadchodza"

rt13 = lambda x: "".join([abc[(abc.find(c) + 13) % len(abc)] for c in x])

print(rt13(s))
print(rt13(rt13(s)))