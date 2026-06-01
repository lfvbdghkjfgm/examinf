# Solved by Влад

from re import *

s = open("986_1.txt").readline()
r = r"([QWRTYPSDFGHJKLZXCVBNM][A-Z][EUIOA])+"
print(max([len(x.group()) for x in finditer(r, s)]))
