# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


from itertools import product

res = []
for d1 in "123456789":
    for l in range(10):
        for s in product("123456789", repeat=l):
            s = "".join(s)
            num = f"32{s}54{d1}123"
            if int(num) > 10**13:
                break
            if int(num) % 519 == 0:
                if len(num) % 2 == 0:
                    if sum(map(int, num[: len(num) // 2])) == sum(
                        map(int, num[len(num) // 2 :])
                    ):
                        res.append([int(num), int(num) // 519])

for i in sorted(res):
    print(*i)

# Solved by Владимир Д.


for mid_len in range(6):
    for mid in range(10**mid_len):
        star = str(mid).zfill(mid_len)

        for d in "0123456789":
            s = f"32{star}54{d}123"

            if len(s) % 2 != 0:
                continue

            if "0" in s:
                continue

            n = len(s) // 2

            if sum(map(int, s[:n])) != sum(map(int, s[n:])):
                continue

            num = int(s)

            if num % 519 == 0:
                print(num, num // 519)
