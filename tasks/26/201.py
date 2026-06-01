# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\201_2.txt")
]
nums = [i for i in nums if i]
n, k = nums[0]
nums = nums[1:]
data = {}

for row, place in nums:
    if row not in data.keys():
        data[row] = set()
    data[row].add(place)

res = [0, 0]
for row, places in data.items():
    if row < res[0]:
        continue
    places = sorted(list(places))
    for i in range(len(places) - 1):
        if places[i + 1] - places[i] == k + 1:
            res = [row, places[i] + 1]
            break
print(*res)
