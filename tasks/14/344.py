# Solved by lfvbdghkjfgm
# https://lfvb.ru


def from_ss(l, ss):
    res = 0
    for a, i in enumerate(l[::-1]):
        res += i * ss**a
    return res


d = set()
for y in range(9, 18):
    for x in range(y):
        a = from_ss([5, x, y, 10], 18)
        b = from_ss([1, 8, x, 7], y)
        d.add(a + b)
print(len(d))