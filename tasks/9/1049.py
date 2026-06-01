# Solved by Данзан С.

l = [[int(d) for d in x.split()] for x in open("31.txt")]
k = 0
for x in l:
    k += 1
    povt3 = [d for d in x if x.count(d) == 3]
    nepovt = [d for d in x if x.count(d) == 1]
    if len(povt3) == 6 and len(nepovt) == 1:
        povt = [d for d in x if x.count(d) > 1]
        if sum(povt) / len(povt) > nepovt[0]:
            print(k, x)
