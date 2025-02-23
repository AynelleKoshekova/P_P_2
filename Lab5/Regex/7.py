def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

example = "this_is_snake_case"
camel_case = snake_to_camel(example)
print("CamelCase:", camel_case)
