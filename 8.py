import re

text = input("Enter camel case text: ")
parts = re.findall(r'[A-Z][^A-Z]*', text)
print("Split parts:", parts)
