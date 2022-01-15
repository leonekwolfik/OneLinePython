import random

import numpy as np

basket = np.array([[random.randint(0,1) for _ in range(4)] for _ in range(13)])

print(basket)

ebooks = basket[:, 2::]
# print(ebooks)

two_books_clients_number = np.sum(np.all(ebooks, axis=1))
print(two_books_clients_number)

copurchases = two_books_clients_number / basket.shape[0]

print(copurchases)

print(basket.shape)