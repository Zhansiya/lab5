import re


pattern = r'ab*'


test_strings = ["a", "ab" ]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}'  Match")
    else:
        print(f"'{string}'  No match")
