# Solved by Константин Х.


for N in range(4, 1000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R + str(R[:3])
    if N % 2 != 0:
        R = "1" + R + "01"
    R = int(R, 2)
    if R > 600:
        print(R)
