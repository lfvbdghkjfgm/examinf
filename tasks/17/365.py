# Solved by Виктор Г.


t = [int(d) for d in open("17.txt")]
k = [d for d in t if d % 52 == 0]
r = min(k)
o = 0
n = []
for i in range(len(t) - 2):
    g = t[i]
    gg = t[i + 1]
    ggg = t[i + 2]
    v = [g, gg, ggg]
    z = [d % 113 for d in v]
    if sum(z) == r:
        o += 1
        n.append(sum(v))
print(o, max(n))
