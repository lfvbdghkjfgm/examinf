# Solved by Владимир Д.


import re

s = open("other/examinf/24/153.txt").readline()

m = re.findall(r"((?:NPO|PNO)+)", s)
max_len = max(len(m) for m in m)
print(max_len // 3)
