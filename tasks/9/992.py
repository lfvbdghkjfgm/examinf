# Solved by Данзан С.


import math

ct = 0
l = [[int(d) for d in x.split()] for x in open("28.txt")]
for x in l:
    povt = [d for d in x if x.count(d) > 1]
    if len(povt) > 0:
        print(povt)
        nepovt = [d for d in x if x.count(d) == 1]
        if sum(nepovt) * 3 <= math.prod(povt):
            ct += 1
print(ct)

# Solved by Владислав Ф.


import math

l = [[int(d) for d in x.split()] for x in open("699.txt")]
k = 0
for x in l:
    povt = [d for d in x if x.count(d) > 1]
    nepovt = [d for d in x if x.count(d) == 1]
    if len(povt) > 0:
        if (sum(nepovt)) * 3 <= math.prod(povt):
            k += 1
print(k)
