# Solved by Иван С.

m = []
l = [int(x) for x in open("df.txt")]
mn = min([x for x in l if x > 0 and len(str(x)) == 4 and x % 10 == 6])
for i in range(len(l) - 2):
    a, b, c = l[i], l[i + 1], l[i + 2]
    tr = [a, b, c]
    v1 = [x for x in tr if len(str(abs(x))) == 4 and abs(x) % 10 == 6]
    if len(v1) == 1 and sum(tr) <= mn:
        m.append(sum(tr))

print(len(m), max(m))

# Solved by Глеб Г.

l = [int(d) for d in open("36.txt")]
q = []
min6 = min([d for d in l if d > 0 and len(str(abs(d))) == 4 and str(d)[-1] == "6"])
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4 and str(l[x])[-1] == "6":
        k += 1
    if len(str(abs(l[x + 1]))) == 4 and str(l[x + 1])[-1] == "6":
        k += 1
    if len(str(abs(l[x + 2]))) == 4 and str(l[x + 2])[-1] == "6":
        k += 1
    if k == 1:
        if (l[x] + l[x + 1] + l[x + 2]) <= min6:
            q.append(l[x] + l[x + 1] + l[x + 2])
print(len(q), max(q))
