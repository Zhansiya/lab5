import re


pattern = r'ab{2,3}$'


txt = input("Enter a string: ")


if re.fullmatch(pattern, txt):
    print(f"'{txt}' → Match ✅")
else:
    print(f"'{txt}' → No match ❌")
