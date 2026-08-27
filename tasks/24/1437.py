# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


text = open(r"C:\Users\aatop\Downloads\1437_1.txt").read()
mx_len = 0
for start in range(len(text)):
    if text[start] == "0":
        continue
    for end in range(start + 2, len(text)):
        if end - start < mx_len:
            continue
        s = text[start:end]
        if s.count("Z") > 4:
            break
        if s[0] != "0" and s[-1] == "0":
            mx_len = max(mx_len, len(s))

print(mx_len)
