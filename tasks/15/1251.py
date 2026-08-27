# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


def B(x):
    return 60 <= x <= 80


for a in range(5000, 0, -1):
    flag = True
    for x in range(1, 5000):
        if ((x % a == 0) or (B(x) <= (x % 22 != 0))) == 0:
            flag = False
            break
    if flag:
        print(a)
        break
