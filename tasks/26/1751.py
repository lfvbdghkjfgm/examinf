# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\1751_1.txt")
]

nums = nums[1:]

nums.sort(key=lambda d: -d[1])
bash = []
while nums:
    bs = [nums[0]]
    for i in nums[1:]:
        if bs[-1][1] - i[1] >= 2:
            bs.append(i)
    for i in bs:
        nums.remove(i)
    bash.append(bs)

print(sum([i[1] for i in bash[-1]]), sum([i[-1][0] for i in bash]))