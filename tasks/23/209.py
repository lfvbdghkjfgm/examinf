# Solved by Тимур А.


def g(x, y):
    if x > y or x == 15 or x == 30:
        return 0
    if x == y:
        return 1
    if x < y:
        return g(x + 2, y) + g(x + 3, y) + g(x**2, y)


print(g(3, 10) * g(10, 20) * g(20, 38))
