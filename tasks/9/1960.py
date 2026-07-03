# Solved by Анастасия


l = [[int(d) for d in x.split()] for x in open("9.txt")]
ct = 0
for x in l:
    povt = [y for y in x if x.count(y) > 1]
    nepovt = [y for y in x if x.count(y) == 1]
    print(povt)
    k = 0
    if len(povt) > 0 and len(nepovt) > 0:
        k += 1
    if len(povt) > 0 and (sum(povt) / len(povt)) > min(x):
        k += 1
    x = sorted(x)
    if (x[0] + x[-1]) != (x[1] + x[2]):
        k += 1
    if k >= 2:
        ct += 1
print(ct)

# Solved by Аня


l = [[int(d) for d in x.split()] for x in open("9.txt")]
ct = 0
for x in l:
    k = 0
    x = sorted(x)
    pv = [y for y in x if x.count(y) > 1]
    npv = [y for y in x if x.count(y) == 1]
    if len(pv) > 0 and len(npv) > 0:
        k += 1
    if len(pv) > 0 and (sum(pv) / len(pv)) > x[0]:
        k += 1
    if (
        x[0] + x[1] != x[2] + x[3]
        and x[0] + x[2] != x[1] + x[3]
        and x[0] + x[3] != x[2] + x[1]
    ):
        k += 1
    if k >= 2:
        ct += 1
print(ct)
