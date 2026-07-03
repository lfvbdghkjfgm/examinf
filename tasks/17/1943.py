# Solved by Анастасия


l = [int(x) for x in open("17.txt")]
mx = []
ok42 = (max([y for y in l if str(y)[-2:] == "42" and len(str(abs(y))) == 5])) ** 2
for x in range(len(l) - 1):
    k = 0
    if str(l[x])[-2:] == "42" and len(str(abs(l[x]))) == 5:
        k += 1
    if str(l[x + 1])[-2:] == "42" and len(str(abs(l[x + 1]))) == 5:
        k += 1
    if k == 1 and ((l[x]) ** 2 + (l[x + 1]) ** 2) >= ok42:
        mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))
