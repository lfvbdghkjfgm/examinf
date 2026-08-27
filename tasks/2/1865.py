# Solved by Виктор Г.


import itertools


def f(x, y, z, w):
    return not ((x <= w) <= (w == z)) and y


for t in itertools.product([1, 0], repeat=5):
    t = [(t[0], 0, 1, 0), (0, t[1], t[2], 0), (t[3], 1, 1, t[4])]
    if len(set(t)) == 3:
        for j in itertools.permutations("xyzw"):
            if [f(**dict(zip(j, r))) for r in t] == [1, 1, 1]:
                print(*j)
