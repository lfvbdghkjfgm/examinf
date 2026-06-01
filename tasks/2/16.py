# Solved by Вадим С.

import itertools


def f(x, y, w, z):
    return (x == (w or y)) or ((w <= z) and (y <= w))


for i in itertools.product([0, 1], repeat=7):
    table = [(1, i[0], i[1], 1), (i[2], i[3], i[4], 1), (1, i[5], 1, i[6])]
    if len(set(table)) == 3:
        for j in itertools.permutations("xywz"):
            if [f(**dict(zip(j, r))) for r in table] == [0, 0, 0]:
                print(j)

# Solved by Артем А.

print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ((x == (w or y)) or ((w <= z) and (y <= w))) == 0:
                    print(x, y, z, w)
