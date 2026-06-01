# Solved by Глеб Г.


l = [[int(d) for d in x.split()] for x in open("6.txt")]
ct = 0
for x in l:
    if x[0] <= x[1] <= x[2] <= x[3] <= x[4]:
        povt = [d for d in x if (sum(map(int, str(d))) % 2 == 0)]
        if len(povt) != len(set(povt)):
            ct += 1
            print(ct, x, povt)
