# Formatowanie baz danych za pomocą funkcji zip()


## Dane
column_names = ['imię', 'wynagrodzenie', 'stanowisko']
db_rows = [('Alicja', 180000, 'analityk danych'),
           ('Robert', 99000, 'menedżer średniego szczebla'),
           ('Franciszek', 87000, 'dyrektor generalny')]

## Jednowierszowiec
db = [dict(zip(column_names, row)) for row in db_rows]

## Wynik
print(db)
