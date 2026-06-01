# Solved by Влад

f = open("test.txt")
a = []
for s in f:
    a.append(int(s))
mn = min([int(x) for x in a if x % 10 == 4 and x > 0])
tr = []
for i in range(len(a) - 2):
    t1 = sum([int(x) for x in str(abs(a[i]))])
    t2 = sum([int(x) for x in str(abs(a[i + 1]))])
    t3 = sum([int(x) for x in str(abs(a[i + 2]))])
    if t1 + t2 + t3 == mn:
        tr.append(a[i] + a[i + 1] + a[i + 2])
print(len(tr), max(tr))
