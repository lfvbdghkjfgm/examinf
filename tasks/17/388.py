# Solved by Влад

a = [int(x) for x in open("test.txt")]
tr = []
mx = max([int(x) for x in a if int(x) % 100 == 17])
for i in range(len(a) - 2):
    if (
        int(len(str(abs(int(a[i])))) == 4)
        + int(len(str(abs(int(a[i + 1])))) == 4)
        + int(len(str(abs(int(a[i + 2])))) == 4)
    ) == 2:
        if (int(a[i] % 5 == 0) + int(a[i + 1] % 5 == 0) + int(a[i + 2] % 5 == 0)) >= 1:
            if a[i] + a[i + 1] + a[i + 2] > mx:
                tr.append(a[i] + a[i + 1] + a[i + 2])
print(len(tr), max(tr))

# Solved by Вадим С.

l = [int(d) for d in open("388_1.txt")]
c = []
p = max([x for x in l if x % 100 == 17])
for x in range(len(l) - 2):
    t = [l[x], l[x + 1], l[x + 2]]
    h = [i for i in t if i % 5 == 0]
    g = [i for i in t if len(str(i)) == 4]
    if len(h) >= 1 and len(g) == 2 and sum(t) > p:
        c.append(sum(t))
print(len(c), max(c))
