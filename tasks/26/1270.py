# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\1270_3.txt")
]
seats_ct = nums[0][2]
rows_ct = nums[0][1]
data = {}
for row, seat in nums[1:]:
    if row not in data.keys():
        data[row] = set()
    data[row].add(seat)


busy = {}
for seat in range(1, seats_ct + 1):
    busy[seat] = rows_ct + 1
    for row, seats in data.items():
        if seat in seats and row < busy[seat]:
            busy[seat] = row
res = [0, 0]
for i in range(1, seats_ct):
    row = min(busy[i], busy[i + 1]) - 1
    if row > res[0]:
        res = [row, i]
print(*res)