# Solved by lfvbdghkjfgm
# https://lfvb.ru

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
