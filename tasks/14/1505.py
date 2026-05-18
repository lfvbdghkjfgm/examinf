# Solved by lfvbdghkjfgm
# https://lfvb.ru


def to_25(num):
    res = []
    while num:
        res.append(num % 25)
        num //= 25
    return res[::-1]


mn = [0, 0]
for i in range(1, 2501):
    t = to_25(25**150 + 25**100 - i)
    if t.count(0) > mn[0]:
        mn = [t.count(0), i]
print(mn)