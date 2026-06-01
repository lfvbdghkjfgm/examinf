# Solved by lfvbdghkjfgm
# https://lfvb.ru

with open("/home/student/Загрузки/1089_1.txt") as f:
    text = f.read()

text = text.split("Y")

max = 0

for i in text:
    ln = 0
    k = i.split(".")
    if len(k) < 6:
        ln = len(i)
    else:
        mx = 0
        for i in range(len(k) - 5):
            st = k[i] + k[i + 1] + k[i + 2] + k[i + 3] + k[i + 4] + k[i + 5]
            l = len(st)
            if l > mx:
                mx = l
        ln = mx + 5
    if ln > max:
        max = ln


print(max)
