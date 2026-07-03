# Solved by Аня


l = [[int(d) for d in x.split()] for x in open("bite1_9.txt")]
k = 0
for x in l:
    k += 1
    p2 = [y for y in x if x.count(y) == 2]
    p1 = [y for y in x if x.count(y) == 1]
    if len(p2) == 2 and len(p1) == 4:
        if sum(p1) % p2[0] == 0:
            print(k, sum(x))
