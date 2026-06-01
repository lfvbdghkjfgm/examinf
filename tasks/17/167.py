# Solved by Влад

f = open("test.txt")
a = []
for s in f:
    a.append(int(s))
dv = [int(x) for x in a if abs(x) % 100 == 28]
sr = sum(dv) / len(dv)
tr = []
for i in range(len(a) - 2):
    if (
        int(len(str(abs(a[i]))) == 4)
        + int(len(str(abs(a[i + 1]))) == 4)
        + int(len(str(abs(a[i + 2]))) == 4)
        >= 1
    ):
        if (
            int(abs(a[i]) % 100 == 11)
            + int(abs(a[i + 1]) % 100 == 11)
            + int(abs(a[i + 2]) % 100 == 11)
            == 2
        ):
            if a[i] > sr and a[i + 1] > sr and a[i + 2] > sr:
                tr.append(a[i] + a[i + 1] + a[i + 2])
print(len(tr), min(tr))
