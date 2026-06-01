# Solved by Вадим С.

l = [[int(d) for d in x.split()] for x in open("1266_1.txt")]
ct = 0
for x in l:
    x = sorted(x)
    if len(set(x)) == 6:
        if min(x) / 2 + max(x) / 2 < (sum(x) - min(x) - max(x)) / 4:
            ct += 1
print(ct)

# Solved by Иван П.

a = [[int(d) for d in x.split()] for x in open("9.txt")]
c = 0
for e in a:
    s = sorted(set(e))
    if len(s) == len(e):
        if (s[0] + s[5]) / 2 < (s[1] + s[2] + s[3] + s[4]) / 4:
            c += 1
print(c)
