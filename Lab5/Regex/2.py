import re

pattern = r'ab{2,3}'
test_strings = ['abb', 'abbb', 'ab', 'abbbb']

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"'{s}' matches")
    else:
        print(f"'{s}' does not match")
