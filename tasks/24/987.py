# Solved by Владимир Д.

import re

file = open(r"/home/student/Загрузки/987_1.txt").readline()


match = re.findall(r"A[^AD]*D", file)
match2 = re.findall(r"D[^AD]*A", file)
print(match)
print(max(match, key=len))
print(len(max(match, key=len)))


print(match2)
print(max(match2, key=len))
print(len(max(match2, key=len)))

# Solved by Влад

from re import *

s = open("987_1.txt").readline()
f = r"D([1234567890QWERTYUIOPSFGHJKLZXCVBNM])+A"
print(max([len(x.group()) for x in finditer(f, s)]))
