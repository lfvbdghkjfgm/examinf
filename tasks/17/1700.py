# Solved by lfvbdghkfjgm
# https://lfvb.ru

nums = [int(i) for i in open(r"C:\Users\111\Downloads\1700_1.txt")]

res = []

for i in range(len(nums) - 2):
    l = nums[i : i + 3]
    c1 = [i for i in l if str(i)[0] == str(i)[-1]]
    c2 = [i for i in l if len(str(i)) == 4 and str(i)[1] == "2"]
    if len(c1) == 1 and len(c2) == 2:
        res.append(max(l))

print(len(res), sum(res))

# Solved by Вадим С.

l = [int(x) for x in open("1700_1.txt")]
c = []
for x in range(len(l) - 2):
    t = [l[x], l[x + 1], l[x + 2]]
    h = [i for i in t if str(i)[0] == str(i)[-1]]
    g = [i for i in t if len(str(i)) == 4 and str(i)[1] == "2"]
    if len(h) == 1 and len(g) == 2:
        c.append(max(t))
print(len(c), sum(c))
