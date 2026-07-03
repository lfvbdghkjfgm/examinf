# Solved by Аня


import itertools


def f(x, y, z, w):
    return (x and y and (not z)) or ((not w) and y and z)


for i in itertools.product([0, 1], repeat=5):
    l = [(0, i[0], 1, 0), (i[1], 1, 1, i[2]), (1, 1, i[3], 1), (0, 1, i[4], 1)]
    if len(set(l)) == len(l):
        for j in itertools.permutations("xyzw"):
            if [f(**dict(zip(j, r))) for r in l] == [1, 1, 1, 1]:
                print(j)

# Solved by Владимир Д.


import itertools


def f(x, y, z, w):
    return (x and y and (not z)) or ((not w) and y and z)


for t in itertools.product([0, 1], repeat=5):
    t = [[0, t[0], 1, 0], [t[1], 1, 1, t[2]], [1, 1, t[3], 1], [0, 1, t[4], 1]]
    for j in itertools.permutations("xyzw"):
        if [f(**dict(zip(j, p))) for p in t] == [1, 1, 1, 1]:
            print(*j)
