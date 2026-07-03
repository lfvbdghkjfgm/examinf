# Solved by Аня


def f(s, k):
    if s > k or s == 8:
        return 0
    if s == k:
        return 1
    return f(s + 1, k) + f(s + 3, k) + f(s * 2, k)


print(f(2, 5) * f(5, 13))

# Solved by Владимир Д.


def f(start, end):
    if start > end or start == 8:
        return 0

    if start == end:
        return 1

    if start < end:
        return f(start + 1, end) + f(start + 3, end) + f(start * 2, end)


print(f(2, 5) * f(5, 13))
