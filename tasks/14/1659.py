# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


def to_7(num):
    res = []
    while num:
        res.append(num % 7)
        num //= 7
    return res[::-1]


a = 7**500 + 7**200 - 7**50 - 1

t = to_7(a)
print((len(t) - 1) * 6)
