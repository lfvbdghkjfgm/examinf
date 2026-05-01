import re

text = open(r"C:\Users\aatop\Downloads\1600_1.txt").read()

text = text.replace("*", "+")
text = text.split("++")
mx_len = 0
for s in text:
    if s.count("+") < 50:
        mx_len = max(mx_len, len(s))
        continue
    t = s.split("+")
    for i in range(len(t) - 49):
        st = "+".join(t[i : i + 50])
        mx_len = max(mx_len, len(st))
print(mx_len)
