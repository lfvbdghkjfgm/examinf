# Solved by Владимир Д.


def Del(x, A):
    return x % A == 0


A = []
B = list(range(10, 40 + 1))

for x in range(10**6):
    f = (x in A) or ((x in B) <= (not (Del(x, 6))))

    if not f:
        A.append(x)

print(A[-1] - A[0])
