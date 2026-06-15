# Solved by Владимир Д.


for n in range(18782, 18823):
    d = []
    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            d.append(i)
        if len(d) > 3:
            break
    if len(d) == 3:
        print(*sorted(d))
