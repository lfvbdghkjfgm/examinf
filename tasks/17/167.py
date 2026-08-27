# Solved by Влад


f = open("test.txt")
a = []
for s in f:
    a.append(int(s))
dv = [int(x) for x in a if abs(x) % 100 == 28]
sr = sum(dv) / len(dv)
tr = []
for i in range(len(a) - 2):
    if (
        int(len(str(abs(a[i]))) == 4)
        + int(len(str(abs(a[i + 1]))) == 4)
        + int(len(str(abs(a[i + 2]))) == 4)
        >= 1
    ):
        if (
            int(abs(a[i]) % 100 == 11)
            + int(abs(a[i + 1]) % 100 == 11)
            + int(abs(a[i + 2]) % 100 == 11)
            == 2
        ):
            if a[i] > sr and a[i + 1] > sr and a[i + 2] > sr:
                tr.append(a[i] + a[i + 1] + a[i + 2])
print(len(tr), min(tr))

# Solved by Виктор Г.


t = [int(d) for d in open("17.txt")]
o = 0
z = []
f = [d for d in t if str(d)[-2:] == "28"]
k = sum(f) / len(f)
for i in range(len(t) - 2):
    g = t[i]
    gg = t[i + 1]
    ggg = t[i + 2]
    q = [g, gg, ggg]
    p = [s for s in q if str(s)[-2:] == "11"]
    e = [s for s in q if len(str(abs(s))) == 4]
    r = [s for s in q if s > k]
    if len(r) == 3 and len(p) == 2 and len(e) >= 1:
        o += 1
        z.append(sum(q))
print(o, min(z))
