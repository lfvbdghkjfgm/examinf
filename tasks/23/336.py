# Solved by Виктор Г.


def f(n, y, z):
    if n > y:
        return 0
    elif "ab" in z:
        return 0
    elif n == y:
        return 1
    else:
        return f(n + 3, y, z + "a") + f(n * 5, y, z + "b") + f(n * 7, y, z + "c")


print(f(1, 1000, ""))
