# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\1752_2.txt")
]

n, k = nums[0]
nums = nums[1:]
boxes = nums[:n]
data = nums[n:]
data.sort()

boxes = [[num, cost, [[-1, -1]]] for num, cost in boxes]

for start, end in data:
    boxes.sort(key=lambda d: (-(d[2][-1][1] < start), d[1], d[0]))
    if boxes[0][2][-1][1] < start:
        boxes[0][2].append([start, end])

boxes = [
    [
        num,
        cost,
        len(queue) - 1,
        sum([end - start + 1 for start, end in queue[1:]]) * cost,
    ]
    for num, cost, queue in boxes
]
print(sorted(boxes, key=lambda d: (-d[-1], -d[0]))[0][0], max([x[2] for x in boxes]))