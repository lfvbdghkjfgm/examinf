# Solved by Виктор Г.


import itertools
import string

d = []
k = string.printable[10:15].upper()
for i in itertools.product(string.printable[:15].upper(), repeat=5):
    i = "".join(i)
    if i[0] != "0":
        if i.count("8") == 1:
            t = [str(d) for d in i if d in k]
            if len(t) >= 2:
                d.append(i)
print(len(set(d)))
