# Solved by Иван П.

a = [[int(d) for d in x.split()] for x in open("9.txt")]
c = 0
for e in a:
    s = sorted(set(e))
    if len(s) == len(e):
        if s[0] * s[1] <= s[2] + s[3] + s[4] + s[5] + s[6]:
            c += 1
print(c)
