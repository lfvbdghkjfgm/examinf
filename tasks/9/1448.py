# Solved by София


l = [[int(d) for d in x.split()] for x in open("1448_1.csv")]
k = 0
for x in l:
    k += 1
    povt2 = sorted([a for a in x if x.count(a) == 2])
    nepovt = sorted([a for a in x if x.count(a) == 1])
    if len(povt2) == 6 and len(set(x)) == 5:
        if (povt2[-1] - povt2[0]) ** 2 > 2 * (nepovt[0] ** 2 + nepovt[1] ** 2):
            print(k)

# Solved by Вадим С.


l = [[int(d) for d in x.split()] for x in open("1700_1.txt")]
c = 0
for x in l:
    c += 1
    w = [i for i in x if x.count(i) == 2]
    h = [i**2 for i in x if x.count(i) == 1]
    if len(set(w)) == 3 and sum(h) * 2 < (min(w) - max(w)) ** 2:
        print(c)

# Solved by Данзан С.


l = [[int(d) for d in x.split()] for x in open("32.txt")]
k = 0
for x in l:
    k += 1
    povt2 = [d for d in x if x.count(d) == 2]
    if len(set(povt2)) == 3:
        nepovt = [d for d in x if x.count(d) == 1]
        if (max(povt2) - min(povt2)) ** 2 > (nepovt[0] ** 2 + nepovt[1] ** 2) * 2:
            print(k, x)
