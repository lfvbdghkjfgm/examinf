# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re

text = open(r"C:\Users\111\Downloads\1483_1.txt").read()
text = text.replace("CDE", "#")

m = re.findall(r"(?=((?:#[^#]){86}#[^E]))", text)
mx = max(m, key=len)
print(len(mx) + 87 * 2)

# Solved by Владимир Д.


import re

s = open("/home/student/Загрузки/1483_1.txt").readline().replace("CDE", "#")
m = re.findall(r"(?=((?:#\w*){86}#[^E]))", s)
print(len(min(m, key=len)) + 2 * 87)
