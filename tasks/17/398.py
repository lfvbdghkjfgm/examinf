# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [int(i) for i in open("1")]

g = max([i for i in nums if str(i)[-1] == "7"])
res = []
for ind in range(len(nums) - 2):
    l = nums[ind : ind + 3]
    nc = [i for i in l if i % 2]
    b = [i for i in l if i > g]
    if len(nc) == 2 and len(b) == 1:
        res += l

print(len(res) / 3, sum(set(res)) / len(set(res)))