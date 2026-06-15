# Solved by Владимир Д.


import re

s = open("/home/student/Загрузки/1125_1.txt").readline()

m = re.findall(r"[a-z]+@[a-z]+.[a-z]+", s)
print(len(max(m, key=len)))
