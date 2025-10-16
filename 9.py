import re

text = input("Enter text: ")
spaced = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
print("Result:", spaced)
