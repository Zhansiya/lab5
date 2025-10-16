import re

text = input("Enter snake_case string: ")
camel = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), text)
print("Camel case:", camel)
