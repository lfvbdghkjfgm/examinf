# Solved by Виктор Г.


import itertools

o = 0
for i in itertools.product(sorted("ОЛЬГА"), repeat=5):
    i = "".join(i)
    o += 1
    if i == "ОЛЬГА":
        print(o)
