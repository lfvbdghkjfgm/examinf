# Solved by Виктор Г.


import itertools

o = 0
k = []
q = []
for i in range(1, 9, 2):
    q.append(str(i) + "0")
    q.append("0" + str(i))
    for d in range(len(k)):
        q.append(k[d] + str(i))
print(q)
for i in itertools.product("012345768", repeat=5):
    i = "".join(i)
    n = [d for d in q if d in i]
    if i.count("0") == 1 and i[0] != "0" and len(n) == 0:
        o += 1
print(o)
