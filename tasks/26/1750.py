# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [x.split() for x in open(r"C:\Users\aatop\Downloads\1750_1.txt")]
nums = nums[1:]
nums = [[int(x[0]), int(x[1]), x[2]] for x in nums]
red = sorted([i[:-1] for i in nums if i[-1] == "R"], key=lambda d: -d[1])
green = sorted([i[:-1] for i in nums if i[-1] == "G"], key=lambda d: -d[1])
blue = sorted([i[:-1] for i in nums if i[-1] == "B"], key=lambda d: -d[1])

bash = []
while True:
    first = red[0]
    red = red[1:]
    second = [i for i in green if first[1] - i[1] >= 2]
    if second:
        second = second[0]
    else:
        break
    green.remove(second)
    third = [i for i in blue if second[1] - i[1] >= 2]
    if third:
        third = third[0]
    else:
        break
    blue.remove(third)
    bash.append([first, second, third])
print(len(bash), bash[-1][1][0])