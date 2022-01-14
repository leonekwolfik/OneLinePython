# Użycie listy składanej do wyszukiwania osób o najwyższych dochodach


## Dane
employees = {'Alicja' : 100000,
             'Robert' : 99817,
             'Karolina' : 122908,
             'Franciszek' : 88123,
             'Ewa' : 93121}


## Jednowierszowiec
top_earners = [(k, v) for k, v in employees.items() if v >= 100000]


## Wynik
print(top_earners)
# [('Alicja', 100000), ('Karolina', 122908)]
