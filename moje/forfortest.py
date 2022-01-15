n = 5

l = [(i,j, k) for i in range(n) for j in range(i+1, n) for k in range(j+1, n)]
print(l)


l2 = list()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            l2.append((i,j,k))

print(l2)

print(l == l2)


# Prosta analiza asocjacji: klienci, którzy kupili X, kupili również Y


## Zależności
import numpy as np

## Dane: wiersz to koszyk zakupów klienta
## wiersz = [kurs 1, kurs 2, e-book 1, e-book 2]
## wartość 1 oznacza, że dany produkt został zakupiony
basket = np.array([[0, 1, 1, 0],
                   [0, 0, 0, 1],
                   [1, 1, 0, 0],
                   [0, 1, 1, 1],
                   [1, 1, 1, 0],
                   [0, 1, 1, 0],
                   [1, 1, 0, 1],
                   [1, 1, 1, 1]])

print(basket[:,1] + basket[:,2] == 2)
copurchases = [(i,j,np.sum(basket[:,i] + basket[:,j] == 2)) for i in range(4) for j in range(i+1, 4)]
print(copurchases)

print(max(copurchases, key=lambda x:x[2]))