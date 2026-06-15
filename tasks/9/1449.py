# Solved by Владислав Ф.


l = [[int(d) for d in x.split()] for x in open("699.txt")]
k = 0
for x in l:

    povt = [d for d in x if x.count(d) == 2]
    nepovt = [d for d in x if x.count(d) == 1]
    if len(povt) == 4 and len(nepovt) == 3:
        x.sort()
        if (x[0] * x[1]) > (x[2] + x[3] + x[4] + x[5] + x[6]):
            k += 1
print(k)
