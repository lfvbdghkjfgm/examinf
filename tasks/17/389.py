# Solved by Влад

f = open("test.txt")
a = []
for s in f:
    a.append(int(s))
mn = min([int(x) for x in a if abs(x) % 100 == 25])
tr = []
res = []
for i in range(len(a) - 2):
    if (
        int(len(str(abs(a[i]))) == 4)
        + int(len(str(abs(a[i + 1]))) == 4)
        + int(len(str(abs(a[i + 2]))) == 4)
        >= 2
    ):
        if (a[i] * a[i + 1] * a[i + 2]) <= mn**2:
            res.append(a[i] * a[i + 1] * a[i + 2])
print(len(res), max(res))
