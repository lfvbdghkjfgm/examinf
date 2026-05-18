# Solved by lfvbdghkfjgm
# https://lfvb.ru


def from_40(l):
    res = 0
    for s, i in enumerate(l[::-1]):
        res += i * 40**s
    return res


for x in range(40):
    a = [8, 7, 1, x, 2, 9, 1]
    b = [3, 6, 6, x, 6, 3, 1]
    c = [9, 7, 3, x, 6, 1, 8]
    a = from_40(a)
    b = from_40(b)
    c = from_40(c)
    t = a + b * c
    if t % 39 == 0:
        print(hex(t // 13)[2:])