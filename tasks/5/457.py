# Solved by Влад


for n in range(100, 1000):
    t = str(n)
    p1 = int(t[0]) + int(t[1])
    p2 = int(t[2]) + int(t[1])
    if p1 > p2:
        res = str(p1) + str(p2)
    else:
        res = str(p2) + str(p1)
    if int(res) == 1715:
        print(n)

# Solved by Данзан С.


ct = 0
for x in range(100, 1000):
    a = int(str(x)[0]) + int(str(x)[1])
    b = int(str(x)[1]) + int(str(x)[2])
    if a > b:
        i = str(a) + str(b)
    else:
        i = str(b) + str(a)
    if i == "1715":
        ct += 1
        print(x, i)
print(ct)

# Solved by Виктор Г.


k = 0
for n in range(100, 1000):
    t = [int(d) for d in str(n)]
    p = t[0] + t[1]
    y = t[1] + t[2]
    u = [p, y]
    q = str(max(u)) + str(min(u))
    q = int(q)
    if q == 1715:
        k += 1
print(k)

# Solved by Анастасия


for x in range(100, 1000):
    t = int(str(x)[0]) + int(str(x)[1])
    d = int(str(x)[1]) + int(str(x)[2])
    m = int(str(max(t, d)) + str(min(t, d)))
    if m == 1715:
        print(x)
