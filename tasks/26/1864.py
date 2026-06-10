# Solved by lfvbdghkjfgm
# https://lfvb.ru

data = [[int(i) for i in x.split()] for x in open(r"C:\Users\111\Downloads\1864_1.txt")]

n = data[0][0]
data = data[1:]
res = []
for i in range(366):
    ct = 0
    for x in data:
        if x[0] <= i <= x[1]:
            ct += 1
    if ct == n:
        res.append(i)

int_ct = 0
mx_int = 0
cur_int = [res[0]]

for i in res[1:]:
    if i - cur_int[-1] == 1:
        cur_int.append(i)
    else:
        mx_int = max(mx_int, len(cur_int))
        int_ct += 1
        cur_int = [i]

mx_int = max(mx_int, len(cur_int))
int_ct += 1

print(int_ct, mx_int)
