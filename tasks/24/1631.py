# Solved by lfvbdghkfjgm
# https://lfvb.ru

text = open(r"C:\Users\aatop\Downloads\1631_1.txt").read().strip()
from tqdm import tqdm

left = 0
ct_w = 0
ct_2025 = 0
s = ""
res = 10**10

for i in tqdm(range(len(text))):
    s += text[i]
    if text[i] == "W":
        ct_w += 1
    if s[-4:] == "2025":
        ct_2025 += 1

    while ct_w > 90:
        if s[0] == "W":
            ct_w -= 1
        s = s[1:]

    while True:
        if s and s[0] != "W":
            s = s[1:]
        else:
            break

    if s.count("W") == 90 and s.count("2025") >= 110:
        res = min(res, len(s))

print(res)
