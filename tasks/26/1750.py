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

# Solved by Анастасия


l = [
    x.replace("G", "2").replace("R", "1").replace("B", "3").split()
    for x in open("29.txt")
]
for x in range(len(l)):
    l[x] = [int(l[x][0]), int(l[x][1]), int(l[x][2])]
l = sorted(l, key=lambda d: (-d[1], d[2]))
l1 = list(filter(lambda d: d[2] == 1, l))
l2 = list(filter(lambda d: d[2] == 2, l))
l3 = list(filter(lambda d: d[2] == 3, l))
# print(l1)
# print(l2)
# print(l3) # 4 9 2   8 10
bashni = []
indexes_j = []
indexes_k = []
for i in range(len(l1)):
    bashni.append([l1[i][0]])
    for j in range(len(l2)):
        if l1[i][1] - l2[j][1] >= 2 and j not in indexes_j:
            bashni[-1].append(l2[j][0])
            indexes_j.append(j)
            for k in range(len(l3)):
                if l2[j][1] - l3[k][1] >= 2 and k not in indexes_k:
                    bashni[-1].append(l3[k][0])
                    indexes_k.append(k)
                    break
            else:
                print(len(bashni) - 1, bashni[-2][1])
                exit()
            if len(bashni[-1]) == 3:
                break
