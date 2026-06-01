# Solved by Вадим С.


def dels(x, y):
    return x % y == 0


for a in range(1, 10000):
    flag = True
    for x in range(-1000, 10000):
        if not ((not (dels(x, 84)) or (not (dels(x, 90)))) <= (not (dels(x, a)))):
            flag = False
            break
    if flag:
        print(a)
