# Solved by Виктор Г.


def f(n, y):
    if n < y:
        return 0
    elif n == y:
        return 1
    else:
        return f(n - int(str(n**2)[0]), y) + f(n - sum([int(d) for d in str(n)]), y)


print(f(32, 1))
