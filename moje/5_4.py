import re

report = '''
Gdybyś zainwestował 1$ w roku 1801, miałbyś dziś 18087791,41$.
Jest to zwrot z inwestycji w wysokości 7,967%.
Jeśli jednak w roku 1801 zainwestowałbyś tylko 0,25$, to miałbyś 4521947,8525$.
'''

dollars = [x[0] for x in re.findall('([0-9]+(\,[0-9]*)?\$)', report)]

print(dollars)