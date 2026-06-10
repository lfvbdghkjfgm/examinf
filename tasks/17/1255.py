# Solved by Данзан С.

l = [int(x) for x in open("42.txt")]
ct32 = len([d for d in l if d % 32 == 0])
mx = []
for x in range(len(l) - 2):
    k = 0
    if l[x] < 0:
        k += 1
    if l[x + 1] < 0:
        k += 1
    if k >= 1:
        if (l[x] + l[x + 1]) < ct32:
            mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))

# Solved by Вадим С.

l = [int(x) for x in open("1255_1.txt")]
c = []
b = len([x for x in l if abs(x) % 32 == 0])
for x in range(len(l) - 1):
    t = [l[x], l[x + 1]]
    if len([i for i in t if i < 0]) >= 1:
        if sum(t) < b:
            c.append(sum(t))
print(len(c), max(c))
