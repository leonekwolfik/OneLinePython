## Zależności
import numpy as np

## Dane (wiersz = [tytuł, ocena])
books = np.array([['Coffee Break NumPy', 4.6],
                  ['Władca Pierścieni', 5.0],
                  ['Harry Potter', 4.3],
                  ['Kubuś Puchatek', 3.9],
                  ['The Clown of God', 2.2],
                  ['Coffee Break Python', 4.7]])

# print(books[:,1].astype(float) > 3.9)

predict_bestseller = lambda x, y : x[x[:,1].astype(float) > y][:,0]

print(predict_bestseller(books, 3.9))