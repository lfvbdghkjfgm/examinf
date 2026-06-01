# Solved by Иван П.

a = [[int(d) for d in x.split()] for x in open("9.txt")]
c = 0
for e in a:
    s = sorted(e)
    if 3 * (s[0] + s[1] + s[2]) < 2 * (s[3] + s[4]):
        c5 = 0
        for x in e:
            if x % 10 == 5:
                c5 += 1
        if c5 >= 2:
            c += 1
print(c)
