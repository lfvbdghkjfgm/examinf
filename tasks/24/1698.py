# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re

text = open(r"C:\Users\aatop\Downloads\1698_1.txt").read()

m = re.findall(r"(?=([A-Za-z0-9.]+[A-Za-z0-9]@(?:yandex\.ru|gmail\.com)))", text)


print(len(max(m, key=len)))
