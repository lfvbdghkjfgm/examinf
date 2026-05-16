# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product

for l in range(3, 10):
    for i in product("01223456789", repeat=l):
        i = "".join(i)
        num = int(f"125{i[:3]}125{i[3:]}554")
        if num > 10**14:
            break
        if num % 27919 == 0:
            print(num, num // 27919)