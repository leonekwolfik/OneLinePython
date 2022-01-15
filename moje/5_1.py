import re

text = 'król Karol kupił królowej Karolinie korale koloru koralowego'

result = re.findall('k.*?r.*?l', text)
print(result)

result = re.findall('k.*r.*l', text)
print(result)
