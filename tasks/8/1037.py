# Solved by Константин Х.


import itertools

k = 0
for x in itertools.product(sorted("МИНУС"), repeat=4):
    x = "".join(x)
    k += 1
    x = x.replace("Н", "М")
    x = x.replace("С", "М")
    x = x.replace("У", "И")
    if x.count("М") >= x.count("И"):
        print(k, x)
