# Solved by Влад


f = open("test.txt")
a = []
for s in f:
    a.append(int(s))
mx = max([int(x) for x in a if len(str(abs(x))) == 2])
ch = []
for i in range(len(a) - 3):
    if abs(a[i]) % 10 == abs(a[i + 1]) % 10 == abs(a[i + 2]) % 10 == abs(a[i + 3]) % 10:
        ch.append(a[i] + a[i + 1] + a[i + 2] + a[i + 3])
A = max(ch)
pt = []
for i in range(len(a) - 4):
    if (
        int(a[i] < A)
        + int(a[i + 1] < A)
        + int(a[i + 2] < A)
        + int(a[i + 3] < A)
        + int(a[i + 4] < A)
        == 1
    ):
        if (a[i] + a[i + 1] + a[i + 2] + a[i + 3] + a[i + 4]) % mx == 0:
            pt.append(a[i] + a[i + 1] + a[i + 2] + a[i + 3] + a[i + 4])
print(len(pt), min(pt))

# Solved by Виктор Г.


t = [int(d) for d in open("17.txt")]
q = []
o = 0
j = []
s = max([d for d in t if len(str(abs(d))) == 2])
for i in range(len(t) - 3):
    g = t[i]
    gg = t[i + 1]
    b = t[i + 2]
    bb = t[i + 3]
    f = [g, gg, b, bb]
    if str(g)[-1] == str(gg)[-1] == str(bb)[-1] == str(b)[-1]:
        q.append(sum(f))
a = max(q)
for i in range(len(t) - 4):
    g = t[i]
    gg = t[i + 1]
    b = t[i + 2]
    bb = t[i + 3]
    hh = t[i + 4]
    f = [g, gg, b, bb, hh]
    c = [d for d in f if d < a]
    if sum(f) % s == 0 and len(c) == 1:
        o += 1
        j.append(sum(f))
print(o, min(j))
