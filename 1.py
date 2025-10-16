import re

pattern = r'ab*'
txt = input("Enter a string: ")

if re.fullmatch(pattern, txt):
    print("Match")
else:
    print("No match")
