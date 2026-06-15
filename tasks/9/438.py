# Solved by София


import math

l = [[int(d) for d in x.split()] for x in open("438_1.csv")]
k = 0
ans = []
for x in l:
    nepovt = [a for a in x if x.count(a) == 1]
    povt = [a for a in x if x.count(a) >= 2]
    k += 1
    if (
        x[0] % 2 == 0
        and x[1] % 2 != 0
        and x[2] % 2 == 0
        and x[3] % 2 != 0
        and x[4] % 2 == 0
        and x[5] % 2 != 0
        and x[6] % 2 == 0
    ) or (
        x[0] % 2 != 0
        and x[1] % 2 == 0
        and x[2] % 2 != 0
        and x[3] % 2 == 0
        and x[4] % 2 != 0
        and x[5] % 2 == 0
        and x[6] % 2 != 0
    ):
        if 3 * sum(nepovt) >= math.prod(povt):
            ans.append(k)
print(sum(ans))
