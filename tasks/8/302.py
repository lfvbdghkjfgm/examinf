# Solved by Арина


import itertools

k = 0
for x in itertools.product(sorted("ТИМОФЕЙ"), repeat=6):
    x = "".join(x)
    for i in x:
        if i in "ИОЕ":
            x = x.replace(i, "0")
        else:
            x = x.replace(i, "1")
    if x.count("1") == x.count("0"):
        k += 1
print(k)
