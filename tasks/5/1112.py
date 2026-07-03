# Solved by Константин Х.


for N in range(1, 1000):
    R = oct(N)[2:]
    if N % 2 == 0:
        R = str(R) + str(max(R))
    if N % 2 != 0:
        R = str(R) + str(2 * (min(R)))
    R = int(R, 8)
    if R < 313:
        print(N)
