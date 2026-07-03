# Solved by степан с.


def v6(d):
    s = ""
    while d > 0:
        s = str(d % 6) + s
        d //= 6
    return s


for N in range(1, 10000):
    R = v6(N)
    if N % 4 == 0:
        R = "2" + R + "03"
    else:
        R = R + v6(N % 3 * 10)
    R = int(R, 6)
    if R > 680:
        print(R)
