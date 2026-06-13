# Solved by Иван П.

a = [[int(d) for d in x.split()] for x in open("9.txt")]
c = 0
for e in a:
    s = sorted(set(e))
    if len(s) == len(e):
        if s[0] * s[1] <= s[2] + s[3] + s[4] + s[5] + s[6]:
            c += 1
print(c)

# Solved by Иса

l = [[int(d) for d in x.split()] for x in open("39")]
k = 0
for x in l:
    povt = [d for d in x if x.count(d) == 1]
    x = sorted(x)
    if len(povt) == 7 and (x[0] * x[1]) <= sum(x) - x[0] - x[1]:
        k += 1
print(k)

# Solved by Глеб Г.

ct = 0
l = [[int(d) for d in x.split()] for x in open("33.txt")]
for x in l:
    x = sorted(x)
    if len(set(x)) == len(x):
        if (x[0] * x[1]) <= (x[2] + x[3] + x[4] + x[5] + x[6]):
            ct += 1
print(ct)
