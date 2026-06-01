# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [[int(i) for i in x.split()] for x in open("1.txt")]

tmp = [i[0] for i in nums]
sr = sum(tmp) / len(tmp)

nums = [i for i in nums if i[0] > sr * 1.5]
print(1)
mn = min(nums, key=lambda d: (d[0], -d[1]))
nums1 = [i[1] for i in nums if i[0] == mn[0]]
print(mn[0] * mn[1], sum(nums1))
