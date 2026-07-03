# Solved by Константин Х.


import itertools

k = 0
for x in itertools.product(sorted("КОДИМ"), repeat=5):
    x = "".join(x)
    k += 1
    if x.count("М") == 2 and "ММ" not in x:
        print(k, x)

# Solved by Мария


import itertools

k = 0
for x in itertools.product(sorted("КОДИМ"), repeat=5):
    x = "".join(x)
    k += 1
    x = x.replace("М", "@")
    if x.count("@") == 2 and "@@" not in x:
        print(k, x)

# Solved by Иса


import itertools

k = 0
for x in itertools.product(sorted("КОДИМ"), repeat=5):
    x = "".join(x)
    k += 1
    if x.count("М") == 2 and "ММ" not in x:
        print(k)
