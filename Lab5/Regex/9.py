import re

test_string = "HelloWorldThisIsPython"
result = re.sub(r'(?<!^)(?=[A-Z])', ' ', test_string)
print("With spaces:", result)
