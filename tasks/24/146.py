# Solved by lfvbdghkjfgm
# https://lfvb.ru


def check(num: int):
    s = sum([int(i) for i in str(num)]) ** len(str(num))
    return s == num


text = open("146_1.txt").read()

mx = 0
for start in range(len(text) - 1):
    for end in range(start + 2, len(text)):
        sn = text[start:end]
        if sn.isdigit():
            n = int(sn)
            if check(n):
                mx = max(mx, n)
        else:
            break
print(text.count("2401"))
print(mx)
