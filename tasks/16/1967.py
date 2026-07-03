# Solved by Анастасия


import sys

sys.setrecursionlimit(1000000)


def f(n):
    if n < 6:
        return 2
    if n >= 6:
        return ((n % 4) + 2) * f(n - 2)


print((f(2026) - 3 * f(2024)) / f(2022))

# Solved by Аня


import sys

sys.setrecursionlimit(10**6)


def f(n):
    if n < 6:
        return 2
    else:
        return (n % 4 + 2) * f(n - 2)


print((f(2026) - 3 * f(2024)) / f(2022))
