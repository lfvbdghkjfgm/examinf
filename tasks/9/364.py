# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [[int(i) for i in j.split(";")] for j in open("364_1.csv")]
res = 0
for x in nums:
    d = [i for i in x if not i % 3]
    if len(d) == 3 and (max(x) - min(x)) <= sum(d):
        res += 1
print(res)