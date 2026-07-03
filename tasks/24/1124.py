# Solved by Владимир Д.


import re

with open("examinf/24/1124.txt") as f:
    s = f.read()

num = r"(?:[1-9]\d*[05]|0)"
matches = re.findall(f"{num}(?:[+*]{num})*", s)

print(max(len(x) for x in matches))
