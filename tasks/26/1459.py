# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\1459_1.txt")
]

places = [-2] * nums[0][0]
nums = nums[2:]

last_place = 0
res = 0

for start, end in sorted(nums):
    for pl in range(len(places)):
        if start - places[pl] >= 0:
            last_place = pl
            places[pl] = end + 1
            res += 1
            break

print(res, last_place + 1)