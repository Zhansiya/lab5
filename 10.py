import re

text = input("Enter camelCase string: ")
snake = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', text).lower()
print("Snake case:", snake)
