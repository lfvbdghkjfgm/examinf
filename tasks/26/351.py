# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [int(x) for x in open(r"C:\Users\aatop\Downloads\351_2.txt")]
nums = nums[1:]
nums.sort(reverse=True)

res = [nums[0]]

for i in nums:
    if res[-1] - i >= 8:
        res.append(i)

print(len(res), res[-1])

# Solved by Глеб Г.


l = [int(d) for d in open("1.txt")]
tort = [l[0]]
for x in l:
    if abs(tort[-1] - x) >= 8:
        tort.append(x)
print(len(tort), tort[-1])
