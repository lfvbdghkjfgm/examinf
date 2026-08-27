# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


def check(st):
    s = "QWERTY"
    cur = 0
    for i in st:
        if i == s[cur]:
            cur += 1
        if cur == len(s):
            break
    if cur == len(s):
        return True
    return False


res = 0

for x in open(r"C:\Users\aatop\Downloads\1617_1.txt"):
    if check(x):
        res += 1

print(res)
