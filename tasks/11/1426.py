# Solved by Владимир Д.


from math import ceil, log2

for N in range(2, 100):
    bits = ceil(log2(N))
    total = 50000 * ceil(113 * bits / 8)

    if total < 3828 * 1024 and bits == 5:
        print(N)
        break
