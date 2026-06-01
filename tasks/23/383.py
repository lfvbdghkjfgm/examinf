# Solved by Тимур А.


def g(x, y):
    if x < y or x == 20:
        return 0
    if x == y:
        return 1
    if x > y:
        return g(x - 2, y) + g(x - 3, y) + g(x // 5, y)


print(g(41, 10) * g(10, 5))
