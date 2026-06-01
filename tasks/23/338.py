# Solved by Виктор Г.


def f(x, y):
    if x > y:
        return 0
    elif x == 20 or x == 25:
        return 0
    elif x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y) + f(x**2, y)


print(f(2, 15) * f(15, 35) * f(35, 50))
