# Solved by lfvbdghkfjgm
# https://lfvb.ru

import re

text = open(r"C:\Users\aatop\Downloads\1487_1.txt").read()

first_word = r"[ABC][abc]*"
word = r"[ABCabc][abc]*"

m = re.findall(rf"{first_word}(?: {word})*\.", text)

print(len(max(m, key=len)))

# Solved by Анастасия

import re

m = open("1487.txt").readline()
s = re.findall(r"(?:[ABC][abc]+[ ][ABC]?[abc]+)*[.]", m)
print(max(s, key=len))
print(len(max(s, key=len)))
