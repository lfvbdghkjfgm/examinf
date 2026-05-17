# Solved by lfvbdghkfjgm
# https://lfvb.ru

nums = [int(i) for i in open(r"C:\Users\111\Downloads\1663_1.txt")]

res = 0
sm = 0

for i in range(len(nums) - 2):
    l = nums[i : i + 3]
    c1 = [i for i in l if i % 40 == 15]
    c2 = [i for i in l if i % 7 == 0]
    if len(c1) == 2 and len(c2) <= 2:
        res += 1
        sm += sum([i for i in l if i % 40 != 15])


print(res, sm)
