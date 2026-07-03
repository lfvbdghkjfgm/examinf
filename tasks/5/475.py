# Solved by Глеб Г.


l = []
for N in range(1, 1000):
    R = bin(N)[2:]
    if R.count("1") % 2 == 0:
        R = "10" + R[2:] + "0"
    else:
        R = "11" + R[2:] + "1"
    R = int(R, 2)
    if N > 27:
        l.append(R)
print(min(l))

# Solved by Виктор Г.


d = []
for n in range(28, 10000):
    r = bin(n)[2:]
    print(n, r)
    if r.count("1") % 2 == 0:
        r = "10" + r[2:] + "0"
    else:
        r = "11" + r[2:] + "1"
    r = int(r, 2)
    d.append(r)
print(min(d))
