# Solved by Анастасия


import itertools


def f(x, y, z, w):
    return (not (x or (not z))) and (y <= w)


for i in itertools.product([0, 1], repeat=7):
    l = [(i[0], i[1], i[2], 1), (i[3], 1, i[4], 0), (i[5], i[6], 1, 1)]
    if len(set(l)) == len(l):
        for j in itertools.permutations("xyzw"):
            if [f(**dict(zip(j, r))) for r in l] == [1, 1, 1]:
                print(j)
