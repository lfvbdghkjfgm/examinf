# Solved by lfvbdghkjfgm
# https://lfvb.ru


nums = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\1406_1.txt")
]

weight = nums[0][1]
data = [x[0] for x in nums[1:]]
sm = 0
ct = 0
for i in data:
    if 310 <= i <= 320:
        weight -= i
        sm += i
        ct += 1

data = [i for i in data if i > 320 or i < 310]
res = []
data.sort()
for i in data:
    if sum(res) + i <= weight:
        res.append(i)
    else:
        break

for i in data:
    for j in range(len(res)):
        if (
            i > res[j]
            and data.count(i) > res.count(i)
            and sum(res) - res[j] + i <= weight
        ):
            res[j] = i

print(ct + len(res), sm + sum(res))
