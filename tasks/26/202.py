# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\202_1.txt")
]
nums = nums[1:]
nums.sort()

res = [nums[0]]
for start, end in nums[1:]:
    if start <= res[-1][1] and end >= res[-1][1]:
        res[-1][1] = end
    if start > res[-1][1]:
        res.append([start, end])

res = [end - start for start, end in res]
print(sum(res), max(res))
