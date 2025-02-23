import re

pattern = r'[ ,.]'
test_string = "Hello, world. How are you today?"
result = re.sub(pattern, ":", test_string)
print("Result:", result)
