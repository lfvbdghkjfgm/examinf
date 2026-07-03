# Solved by Влад


for n in range(100, 1000):
    t = str(n)
    p1 = int(t[0]) * int(t[1])
    p2 = int(t[2]) * int(t[1])
    if p1 > p2:
        res = str(p1) + str(p2)
    else:
        res = str(p2) + str(p1)
    if int(res) == 205:
        print(n)

# Solved by Виктор Г.


for n in range(100, 1000):
    q = [int(d) for d in str(n)]
    t = q[0] * q[1]
    r = q[1] * q[2]
    g = [t, r]
    d = int(str(max(g)) + str(min(g)))
    if d == 205:
        print(n)
