# Solved by lfvbdghkjfgm
# https://lfvb.ru


def to_ss(num, ss):
    res = []
    while num > 0:
        res.append(num % ss)
        num //= ss
    return res[::-1]


a = 7**170 + 7**100
r = [0, 0]
for x in range(1, 2031):
    d = to_ss(a - x, 7)
    if d.count(0) >= r[0]:
        r = [d.count(0), x]

print(r)

# Solved by Анастасия


def v7(n):
    s = ""
    while n > 0:
        s += str(n % 7)
        n //= 7
    return s[::-1]


for x in range(1, 2031):
    d = 7**170 + 7**100 - x
    d = v7(d)
    if d.count("0") > 72:
        print(x, d.count("0"))
