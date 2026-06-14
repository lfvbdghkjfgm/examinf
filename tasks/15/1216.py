# Solved by lfvbdghkjfgm
# https://lfvb.ru


def B(x):
    return 170 <= x <= 220


res = 0
for a in range(5000, 0, -1):
    flag = True
    for x in range(1, 5000):
        if ((x % a == 0) or (B(x) <= (x % 24 != 0))) == 0:
            flag = False
            break
    if flag:
        res += 1
print(res)
