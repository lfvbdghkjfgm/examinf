# Solved by Владимир Д.


P = list(range(10, 25 + 1))
Q = list(range(15, 30 + 1))
R = list(range(25, 40 + 1))
A = list(range(1, 10_000))

for x in range(1, 10_000):
    f = ((x in Q) <= (x not in R)) and (x in A) and (x not in P)

    if f:
        A.remove(x)

print(A[-1] - A[0])
