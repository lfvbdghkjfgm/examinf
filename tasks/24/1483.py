# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re

text = open(r"C:\Users\111\Downloads\1483_1.txt").read()
text = text.replace("CDE", "#")

m = re.findall(r"(?=((?:#[^#]){86}#[^E]))", text)
mx = max(m, key=len)
print(len(mx) + 87 * 2)