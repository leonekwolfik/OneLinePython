import re

text = 'zbyt czeste uzywanie slow pOwoduje zuzywanie sie slow'

style_problems = re.search('\s(?P<x>[a-zA-Z]*)\s+([a-zA-Z]+\s+){0,10}(?P=x)\s', ' ' + text + ' ')
print(style_problems)
