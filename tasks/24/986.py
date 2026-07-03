# Solved by Влад


from re import *

s = open("986_1.txt").readline()
r = r"([QWRTYPSDFGHJKLZXCVBNM][A-Z][EUIOA])+"
print(max([len(x.group()) for x in finditer(r, s)]))

# Solved by Владимир Д.


from re import findall

file = open("/home/student/Загрузки/986_1.txt").read()

print(len(max(findall(r"(?:[CDF][ACDFO][AO])+", file), key=len)) // 3)
