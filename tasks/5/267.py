# Solved by Данзан С.


for x in range(1000, 10000):
    a = int((str(x)[0])) * int((str(x)[1]))
    b = int((str(x)[2])) * int((str(x)[3]))
    if a > b:
        y = str(b) + str(a)
    else:
        y = str(a) + str(b)
    if y == "1214":
        print(x)

# Solved by Анастасия


for x in range(1000, 10000):
    x = str(x)
    p1 = str(int(x[0]) * int(x[1]))
    p2 = str(int(x[2]) * int(x[3]))
    t = min(p1, p2) + max(p1, p2)
    if t == "1214":
        print(x, t)

# Solved by Илья М.


for i in range(1000, 10000):
    g = str(i)
    r = int(g[0]) * int(g[1])
    rr = int(g[2]) * int(g[3])
    R = str(min(r, rr)) + str(max(r, rr))
    if int(R) == 1214:
        print(g)
