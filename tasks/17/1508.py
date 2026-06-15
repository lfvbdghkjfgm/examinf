# Solved by Иван С.


m = []
l = [int(x) for x in open("1.txt")]
mx = max([x for x in l if len(str(abs(x))) == 4])
for i in range(len(l) - 1):
    p = [l[i], l[i + 1]]
    f = [x for x in p if x <= mx]
    if len(f) == 1 and (abs(l[i]) ** 2 + abs(l[i + 1]) ** 2) % 100 == 12:
        m.append(l[i] ** 2 + l[i + 1] ** 2)
print(len(m), min(m))
