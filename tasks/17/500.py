# Solved by Влад

f = open("test.txt")
a = []
for s in f:
    a.append(int(s))
mn = min([int(x) for x in a if x % 41 == 0 and x > 0])
pr = []
for i in range(len(a) - 1):
    if a[i] != a[i + 1] and abs(a[i] - a[i + 1]) % mn == 0:
        pr.append(a[i] + a[i + 1])
print(len(pr), max(pr))
