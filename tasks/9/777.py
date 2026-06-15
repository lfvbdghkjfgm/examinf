# Solved by София


l = [[int(d) for d in x.split()] for x in open("1")]
ct = 0
for x in l:
    povt2 = [a for a in x if x.count(a) == 2]
    if len(povt2) == 2 and len(set(x)) == 5:
        otri = [a for a in x if a < 0]
        pol = [a for a in x if a > 0]
        if abs(sum(otri)) > sum(pol):
            ct += 1
print(ct)
