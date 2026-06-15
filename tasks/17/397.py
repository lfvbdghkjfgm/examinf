# Solved by Влад


f = open("test.txt")
a = []
for s in f:
    a.append(int(s))
mn = min(a)
pr = []
for i in range(len(a) - 1):
    if ((a[i] % 77) * (a[i + 1] % 77)) == mn**2:
        pr.append(a[i] * a[i + 1])
print(len(pr), min(pr))
