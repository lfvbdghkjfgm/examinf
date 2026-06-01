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
