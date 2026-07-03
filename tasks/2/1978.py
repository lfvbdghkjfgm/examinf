# Solved by Анастасия


import itertools


def f(x, y, z, w):
    return (not z) or (not ((w <= x) == (x <= y)))


for i in itertools.product([0, 1], repeat=7):
    l = [(i[0], i[1], 0, 1), (0, i[2], i[3], i[4]), (1, i[5], i[6], 0)]
    if len(set(l)) == len(l):
        for j in itertools.permutations("xyzw"):
            if [f(**dict(zip(j, r))) for r in l] == [0, 0, 0]:
                print(j)
