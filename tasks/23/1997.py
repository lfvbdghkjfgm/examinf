# Solved by Анастасия


def f(st, fn, s):
    if st > fn:
        return 0
    if st == fn and s[0] == "B" and s[-1] == "B":
        return 1
    return f(st + 5, fn, s + "A") + f(st + 10, fn, s + "B") + f(st * 3, fn, s + "C")


print(f(5, 165, ""))
