# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\1729_2.txt")
]
nums = nums[1:]
data = []

for x in nums:
    id = x[0]
    sr = sum(x[1:]) / len(x[1:])
    two_count = x[1:].count(2)
    data.append([id, sr, two_count])

data.sort(key=lambda d: (d[2], -d[1], d[0]))
pov = len(data) // 4
pov = data[:pov]
first_id = 0
for x in data:
    if x[-1] > 2:
        first_id = x[0]
        break

print(pov[-1][0], first_id)
