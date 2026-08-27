# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

# Для извращенцев

nums = [int(i) for i in open(r"C:\Users\111\Downloads\1447_1.txt")]

res = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if int((nums[i] + nums[j]) % 18 == 0) ^ int((nums[i] * nums[j]) % 18 == 0):
            res.append(nums[i] + nums[j])

print(len(res), max(res))

# Для нормальных людей

nums = [int(i) for i in open(r"C:\Users\111\Downloads\1447_1.txt")]

res = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        d = 0
        if (nums[i] + nums[j]) % 18 == 0:
            d += 1
        if (nums[i] * nums[j]) % 18 == 0:
            d += 1
        if d == 1:
            res.append(nums[i] + nums[j])

print(len(res), max(res))

# Solved by Владимир Д.


l = [int(x) for x in open("other/examinf/17/1447.txt")]
ct = 0
mxsm = 0
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        a, b = l[i], l[j]
        usl1 = (a + b) % 18 == 0
        usl2 = (a * b) % 18 == 0
        if (usl1 and not usl2) or (not usl1 and usl2):
            ct += 1
            mxsm = max(mxsm, (a + b))

print(ct, mxsm)
