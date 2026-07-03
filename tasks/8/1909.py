# Solved by Аня


import itertools

k = 0
for x in itertools.product(sorted("КОТИА"), repeat=5):
    x = "".join(x)
    k += 1
    if k % 2 != 0:
        if x[0] != "К" and x[0] != "Т" and x.count("О") == 2:
            print(k, x)

# Solved by Владимир Д.


from itertools import product

ct = 0
for i in product(sorted("КОТИА"), repeat=5):
    ct += 1
    d = "".join(s for s in i)
    if ct % 2 != 0:
        if d[0] != "К" and d[0] != "Т":
            if d.count("О") == 2:
                print(ct, d)
