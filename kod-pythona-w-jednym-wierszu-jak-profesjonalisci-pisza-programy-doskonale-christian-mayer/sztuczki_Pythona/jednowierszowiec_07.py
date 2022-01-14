# Przypisywanie do wycinków w celu skorygowania uszkodzonych list


## Dane
visitors = ['Firefox', 'uszkodzone', 'Chrome', 'uszkodzone',
            'Safari', 'uszkodzone', 'Safari', 'uszkodzone',
            'Chrome', 'uszkodzone', 'Firefox', 'uszkodzone']

## Jednowierszowiec
visitors[1::2] = visitors[::2]

## Wynik
print(visitors)
'''
['Firefox', 'Firefox', 'Chrome', 'Chrome', 'Safari', 'Safari',
'Safari', 'Safari', 'Chrome', 'Chrome', 'Firefox', 'Firefox']
'''
