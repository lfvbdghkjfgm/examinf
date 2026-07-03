# Solved by Илья М.


b = []
for N in range(1000, 10000):
    r = oct(N)[2:]
    r = r.replace("0", "1")
    r = r.replace("2", "1")
    r = r.replace("4", "1")
    r = r.replace("6", "1")
    r = r + str(N % 8)
    r = int(r, 8)
    r = oct(r)[2:]
    r = r.replace("0", "1")
    r = r.replace("2", "1")
    r = r.replace("4", "1")
    r = r.replace("6", "1")
    r = r + str(N % 8)
    R = int(r, 8)
    if R % 234 == 0:
        b.append(R)
print(max(b), b)
