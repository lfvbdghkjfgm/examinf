# Solved by Илья М.

for N in range(1000):
    r = bin(N)[2:]
    r = r[::-1]
    r = r + r[-1]
    R = int(r, 2)
    if R > 99:
        print(N)
