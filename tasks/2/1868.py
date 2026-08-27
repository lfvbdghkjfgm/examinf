# Solved by Виктор Г.


import itertools


def f(x, y, z, w):
    return (w == z) or (not (y <= w)) or (not x)


for t in itertools.product([1, 0], repeat=5):
    t = [(0, 0, 1, t[0]), (t[1], 1, 1, t[2]), (0, t[3], t[4], 0)]
    if len(set(t)) == 3:
        for j in itertools.permutations("xyzw"):
            if [f(**dict(zip(j, r))) for r in t] == [0, 0, 0]:
                print(*j, sep="")
