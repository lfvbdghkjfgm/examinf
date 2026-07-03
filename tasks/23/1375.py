# Solved by Анастасия


def f(st, fn):
    if st < fn or st == 15:
        return 0
    if st == fn:
        return 1
    return f(st - 2, fn) + f(st - 3, fn) + f(st // 3, fn)


print(f(48, 25) * f(25, 17) * f(17, 4))
