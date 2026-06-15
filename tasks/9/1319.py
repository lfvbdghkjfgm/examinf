# Solved by Григорий Б.


l = [[int(d) for d in x.split()] for x in open("1319.txt")]
ct = 0
for x in l:
    c = sorted(x)
    if len(set(x)) == 6:
        if (c[5] + c[4]) * 2 >= (c[0] + c[1] + c[2] + c[3]) * 3:
            ct += 1
print(ct)

# Solved by степан с.


l = [[int(d) for d in x.split()] for x in open("13.txt")]
ct = 0
for x in l:
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt1) == 6:
        x = sorted(x)
        if (x[5] + x[4]) * 2 >= (x[0] + x[1] + x[2] + x[3]) * 3:
            ct += 1
print(ct)
