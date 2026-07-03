# Solved by Анастасия


import sys

sys.setrecursionlimit(1000000)


def f(n):
    if n < 10:
        return 2026
    if n >= 10 and n % 2 == 0:
        return (n + 3) * f(n - 2)
    if n >= 10 and n % 2 != 0:
        return 2 * n + f(n - 2)


print((f(2026) * f(2025)) / f(2022) - 2029 * f(2023) * 2027)
