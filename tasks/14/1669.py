# Solved by Анастасия


def v45(n):
    s = []
    while n > 0:
        s.append(n % 45)
        n //= 45
    return s[::-1]


for x in range(1, 1000):
    d = 6**2030 + 6**100 - x
    d = v45(d)
    if d.count(33) > 16:
        print(oct(d.count(33)))

# Solved by Владимир Д.


def to45(n):
    rs = []
    while n > 0:
        rs.append(n % 45)
        n //= 45

    return rs[::-1]


res = []
mx = 0
for x in range(1000):
    s = 6**2030 + 6**100 - x
    s = to45(s)
    ct = [d for d in s if d == 33]
    mx = max(mx, len(ct))
    if len(ct) == mx:
        print(x, mx)

print(oct(17)[2:])
