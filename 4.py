import re

text = input("Enter text: ")
matches = re.findall(r'[A-Z][a-z]+', text)
print("Matches:", matches)
