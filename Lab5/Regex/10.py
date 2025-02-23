import re

def camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    snake = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    return snake

example = "camelCaseStringExample"
snake_case = camel_to_snake(example)
print("Snake case:", snake_case)
