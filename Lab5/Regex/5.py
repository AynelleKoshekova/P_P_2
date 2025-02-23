import re

pattern = r'^a.*b$'
test_strings = ['aXYZb', 'ab', 'a12345b', 'a_b_c', 'aXbY']
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"'{s}' matches")
    else:
        print(f"'{s}' does not match")
