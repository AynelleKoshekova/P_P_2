import re

test_string = "HelloWorldThisIsPython"
parts = re.split(r'(?=[A-Z])', test_string)
parts = [part for part in parts if part]
print("Split parts:", parts)
