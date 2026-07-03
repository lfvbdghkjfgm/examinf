# Solved by Виктор Г.


t = [int(d) for d in open("17.txt")]
z = [d for d in t if str(d)[-3:] == "151"]
n = sum(z) // len(z)
o = 0
f = []
for i in range(len(t) - 2):
    g = t[i]
    gg = t[i + 1]
    ggg = t[i + 2]
    k = [g, gg, ggg]
    r = [q for q in k if len(str(abs(q))) == 4]
    u = [q for q in k if q % 13 == 0]
    p = [q for q in k if q % 7 == 0]
    c = [int(d) for d in k if d > n]
    if 0 < len(r) < 3:
        if len(u) > len(p):
            if len(c) == 3:
                o += 1
                f.append(sum(k))
print(o, min(f))
