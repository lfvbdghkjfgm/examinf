
# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [[int(i) for i in j.split(';')] for j in open('413_1.csv')]
res =0
for x in nums:
    a = [max(x),min(x)]
    if not x[0] in a and not x[-1] in a and x[0] != x[-1]:
        if  not (a[0] - a[1]) % (x[0] - x[-1]):
            res+=1
print(res)