import re

inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99']

input_ok = lambda x: re.fullmatch('([01][0-9]|2[0-3]):[0-5][0-9]', x) is not None

for x in inputs:
    print(x, input_ok(x))
