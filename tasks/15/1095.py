# Solved by Владимир Д.


def Del(x, A):
    return x % A == 0


for A in range(20000, 1, -1):
    t = True
    for x in range(1, 20000):
        f = (not (Del(x, 263) <= Del(x, A))) and Del(x, 71)

        if f:
            t = False
            break

    if t:
        print(A)
        break
