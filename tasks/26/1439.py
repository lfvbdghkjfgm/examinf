# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\1439_1.txt")
]
sm = nums[0][1]
nums = nums[1:]
res = []
for i in range(4):
    nums = sorted([sorted(i) for i in nums])
    s = sm
    r = []
    new_nums = []
    for j in nums:
        if j[0] < s:
            s -= j[0]
            r.append(j[0])
            new_nums.append(j[1:])
        else:
            new_nums.append(j)

    res.append(r)
    nums = new_nums.copy()

print(len(res[-1]), sum([sum(i) for i in res]))
