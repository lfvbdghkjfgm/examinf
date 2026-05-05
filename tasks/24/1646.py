import re
from math import log

text = open(r"C:\Users\aatop\Downloads\1646_1.txt").read()

m = re.findall(r"[1-9ABCD][0-9ABCD]*[02468AC]", text)
print(len(max(m, key=len)))
