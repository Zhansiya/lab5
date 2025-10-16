import re


pattern = r'ab*'


test_strings = ["a", "ab", "abb", "ac", "b", "aab", ""]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}'  Match")
    else:
        print(f"'{string}'  No match")
