# Solved by Влад


f = open("test.txt")
a = []
for s in f:
    a.append(int(s))
mx = max([int(x) for x in a if len(str(abs(x))) == 2])
ch = []
for i in range(len(a) - 3):
    if abs(a[i]) % 10 == abs(a[i + 1]) % 10 == abs(a[i + 2]) % 10 == abs(a[i + 3]) % 10:
        ch.append(a[i] + a[i + 1] + a[i + 2] + a[i + 3])
A = max(ch)
pt = []
for i in range(len(a) - 4):
    if (
        int(a[i] < A)
        + int(a[i + 1] < A)
        + int(a[i + 2] < A)
        + int(a[i + 3] < A)
        + int(a[i + 4] < A)
        == 1
    ):
        if (a[i] + a[i + 1] + a[i + 2] + a[i + 3] + a[i + 4]) % mx == 0:
            pt.append(a[i] + a[i + 1] + a[i + 2] + a[i + 3] + a[i + 4])
print(len(pt), min(pt))
