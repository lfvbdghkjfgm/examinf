# Solved by Виктор Г.


for N in range(100000):
    R = bin(N)[2:]
    if N % 5 == 0:
        R = R[:3] + R
    else:
        R = R + bin((N % 5) * 5)[2:]
    R = int(R, 2)
    if R < 313 and N % 2 != 0:
        print(N, R)
