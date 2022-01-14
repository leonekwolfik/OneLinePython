# Połączenie listy składanej i wycinania

## Dane (dzienne kursy akcji (w dolarach))
price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
         [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
         [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
         [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]

## Jednowierszowiec
sample = [line[::2] for line in price]

## Wynik
print(sample)
'''
[[9.9, 9.8, 9.5],
 [9.5, 9.4, 9.2],
 [8.4, 7.9, 8.0],
 [7.1, 4.8, 4.7]]
'''
