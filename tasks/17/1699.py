# Solved by lfvbdghkfjgm
# https://lfvb.ru

from math import prod

nums = [int(i) for i in open(r"C:\Users\111\Downloads\1699_1.txt")]

res = []
mx = max(nums)

for i in range(len(nums) - 2):
    l = nums[i : i + 3]
    minus = [i for i in l if i < 0] + [0]
    plus = [i for i in l if i > 0] + [0]
    if abs(sum(minus)) <= sum(plus) and str(prod(l))[-1] == str(mx)[-1]:
        res.append(abs(prod(l)))

print(len(res), max(res))
