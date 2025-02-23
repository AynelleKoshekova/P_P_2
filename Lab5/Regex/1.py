import re

pattern = r'ab*'
test_strings = ['a', 'ab', 'abbbb', 'ac']

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"'{s}' matches")
    else:
        print(f"'{s}' does not match")