l = [int(x) for x in open('AN')]
k = 0
m = -10**10
m6 = max([x for x in l if x % 6 == 0 and x < 0 and 99 < abs(x) < 1000])

for i in range(len(l) - 1):
    x1, x2 = l[i], l[i + 1]
    if int(x1 < 0) + int(x2 < 0) == 1 and x1 + x2 > m6:
        k += 1
        m = max(m, x1 ** 2 + x2 ** 2)
print(k, m)
