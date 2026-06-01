# Solved by Тимур А.


def g(x, y):
    if x > y or x == 11 or x == 12:
        return 0
    if x == y:
        return 1
    if x < y:
        return g(x + 1, y) + g(x * 2, y) + g(x**2, y)


print(g(2, 10) * g(10, 40))
