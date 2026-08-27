# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


nums = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\1643_1.txt")
]

nums = nums[1:]
data = {}
for row, seat in nums:
    if row not in data.keys():
        data[row] = set()
    data[row].add(seat)
res = [0, 0]
for row, seats in data.items():
    seats = sorted(list(seats))
    cur_line = [seats[0]]
    mx_len = 0
    for cur_seat in seats[1:]:
        if cur_seat - cur_line[-1] == 1:
            cur_line.append(cur_seat)
        else:
            cur_line = [cur_seat]
        mx_len = max(mx_len, len(cur_line))
    if mx_len > res[1] or row > res[0] and mx_len == res[1]:
        res = [row, mx_len]
print(*res)
