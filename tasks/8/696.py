# Solved by Виктор Г.


import itertools

o = 0
for i in itertools.product(sorted("СВЕТА"), repeat=5):
    i = "".join(i)
    o += 1
    if i == "СВЕТА":
        print(o)
