# Solved by Влад


for n in range(1000, 10000):
    t = str(n)
    p1 = int(t[0]) + int(t[1])
    p2 = int(t[2]) + int(t[3])
    if p1 > p2:
        res = str(p2) + str(p1)
    else:
        res = str(p1) + str(p2)
    if int(res) == 117:
        print(n)

# Solved by Анастасия


for x in range(1000, 10000):
    x = str(x)
    d = int(x[0]) + int(x[1])
    t = int(x[2]) + int(x[3])
    sm = str(min(d, t)) + str(max(d, t))
    print(x, sm, d, t)

# Solved by Вадим С.


for x in range(1000, 10000):
    x = str(x)
    t = [int(x[0]) + int(x[1]), int(x[2]) + int(x[3])]
    t = sorted(t)
    r = str(t[0]) + str(t[1])
    if int(r) == 117:
        print(int(x))

# Solved by Виктор Г.


for n in range(1000, 10000):
    q = ""
    t = [int(d) for d in str(n)]
    p = t[0] + t[1]
    l = t[2] + t[3]
    w = [p, l]
    q = str(min(w)) + str(max(w))
    q = int(q)
    if q == 117:
        print(n)
