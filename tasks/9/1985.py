# Solved by Аня


l = [[int(d) for d in x.split()] for x in open("9.txt")]
ct = 0
for x in l:
    p3 = [y for y in x if x.count(y) == 3]
    p1 = [y for y in x if x.count(y) == 1]
    if len(p3) == 3:
        if len(p1) >= 1:
            if sum(p3) / len(p3) <= sum(p1) / len(p1):
                ct += 1
print(ct)
