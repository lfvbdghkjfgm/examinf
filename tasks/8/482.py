# Solved by Виктор Г.


import itertools

k = [2, 6]
d = []
for i in itertools.product("01234567", repeat=5):
    i = "".join(i)
    if int(i[0]) % 2 == 0 and int(i[-1]) not in k and i.count("7") <= 2 and i[0] != "0":
        d.append(i)
print(len(set(d)))
