# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from string import printable

text = open(r"C:\Users\111\Downloads\1862_1.txt").readline()

letters = dict.fromkeys(printable, 0)

start = 0
mn = 10**6
for end in range(len(text)):
    letters[text[end]] += 1
    while (
        all([letters[i] > 0 for i in "0123456789"])
        and sum([letters[i] for i in "ABCDEF"]) >= 3
    ):
        if (
            all([letters[i] > 0 for i in "0123456789"])
            and sum([letters[i] for i in "ABCDEF"]) == 3
        ):
            mn = min(mn, end - start + 1)
        letters[text[start]] -= 1
        start += 1

print(mn)
