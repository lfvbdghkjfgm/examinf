# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

nums = [int(i) for i in open("1.txt")]
nums = sorted(nums[1:])[::-1]
res = [nums[0]]

for i in nums:
    if res[-1] - i >= 9:
        res.append(i)
print(len(res), res[-1])
