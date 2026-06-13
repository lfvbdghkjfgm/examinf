# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [[int(i) for i in x.split()] for x in open("1.txt")]

for x in nums:
    if sorted(x)[-2] ** 2 > max(x) * min(x):
        if sum(x) % 2 == 0:
            if sum([i for i in x if i < 90]) % 10 == 4:
                print(sum(x))
                break
