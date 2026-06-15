# Solved by Глеб Г.


l = [[int(d) for d in x.split()] for x in open("3.txt")]
ct = 0
for x in l:
    a = min(x)
    if len(set(x)) == 5:
        if (max(x) + min(x)) < 2 * ((sum(x) - max(x) - min(x)) // 4):
            x.sort()
            if x[1] != a:
                ct += 1
                print(x, a)
print(ct)

# Solved by Анастасия


l = [sorted([int(d) for d in x.split()]) for x in open("165.txt")]
ct = 0
for x in l:
    if x.count(x[0]) == 1:
        if len(set(x)) < 6:
            if x[0] + x[-1] < (x[1] + x[2] + x[3] + x[4]) / 2:
                ct += 1
print(ct)
