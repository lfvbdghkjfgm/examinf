# Solved by Виктор Г.


import itertools


def f(x, y, z, w):
    return (
        ((not x) and y and z and (not w))
        or ((not x) and y and (not z) and (not w))
        or (x and y and z and (not w))
    )


for t in itertools.product([1, 0], repeat=7):
    t = [(1, t[0], t[1], t[2]), (0, t[3], 1, t[4]), (t[5], 0, 0, t[6])]
    if len(set(t)) == 3:
        for j in itertools.permutations("xyzw"):
            if [f(**dict(zip(j, r))) for r in t] == [1, 1, 1]:
                print(*j, sep="")
