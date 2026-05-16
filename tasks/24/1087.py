# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re
with open('/home/student/Загрузки/1087_1.txt') as f:
    text = f.read()

m = re.findall(r'(?:LMN|MN|N)?(?:KLMN)+(?:KLM|KL|K)?',text)

print(len(max(m,key=len)))