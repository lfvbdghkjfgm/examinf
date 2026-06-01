# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re

with open("/home/student/Загрузки/988_1.txt") as f:
    text = f.read()

m = re.findall("(?:\.[A-Z]*?){7}", text)

print(len(min(m, key=len)))
