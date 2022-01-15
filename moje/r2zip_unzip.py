lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]

# Połączenie dwóch list
zipped = list(zip(lst_1, lst_2))
print(zipped)

# Przywrócenie poprzednich list

lst_1_new, lst_2_new = zip(*zipped)

print(list(lst_1_new))
print(list(lst_2_new))

assert lst_1 == list(lst_1_new)
assert lst_2 == list(lst_2_new)