# Solved by Григорий Б.

l = [[int(d) for d in x.split()] for x in open("1009")]
k = 0
for x in l:
    k += 1
    povt = [y for y in x if x.count(y) > 1]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(set(povt)) == 2 and len(povt) == 6 and len(nepovt) == 1:
        if sum(povt) / len(povt) < nepovt[0]:
            print(k)
