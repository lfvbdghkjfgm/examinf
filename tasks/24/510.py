# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re
from tqdm import tqdm

text = open(r"C:\Users\aatop\Downloads\510_1.txt").read()

num = r"(?:0|[1-9][0-9]*)"
zero_prod = rf"(?:{num}\*)*0(?:\*{num})*"
m = re.findall(rf"(?:{zero_prod}\+)+{zero_prod}", text)
print(len(max(m, key=len)))
