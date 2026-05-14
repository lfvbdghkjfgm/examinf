import itertools
from itertools import product

c = 0
for i in product('0123456789abcde', repeat=4):
    if i[0] != '0':
        if i[0] != i[1] and i[1] != i[2] and i[2] != i[3]:
            if i.count('8') == 1:
                c += 1

print(c)