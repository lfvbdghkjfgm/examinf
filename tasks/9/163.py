# Solved by Анастасия

l = [sorted([int(d) for d in x.split()]) for x in open("163.txt")]
ct = 0
for x in l:
    if len(set(x)) == 6:
        if (max(x) + min(x)) / 2 < (
            x[0] + x[1] + x[2] + x[3] + x[4] + x[5] - (max(x) + min(x))
        ) / 4:
            ct += 1
print(ct)
