# Solved by Анастасия


def f(st, fn):
    if st < fn or st == 67:
        return 0
    if st == fn:
        return 1
    return f(st - 2, fn) + f(st - 6, fn) + f(st // 7, fn)


print(f(100, 52) * f(52, 42))
