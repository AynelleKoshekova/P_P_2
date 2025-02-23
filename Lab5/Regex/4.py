import re

pattern = r'\b[A-Z][a-z]+\b'
test_string = "Hello World This Is Python and JAVA"
result = re.findall(pattern, test_string)
print("Matches:", result)
