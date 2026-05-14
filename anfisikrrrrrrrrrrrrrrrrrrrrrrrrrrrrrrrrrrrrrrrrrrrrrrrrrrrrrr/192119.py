from math import ceil
def f(s, m):
    if s <= 505:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s - 3, m - 1), f(s // 5, m - 1)]
    return any(h) if m % 2 != 0 else any(h)

print([s for s in range(505, 1000000) if f(s, 2)])