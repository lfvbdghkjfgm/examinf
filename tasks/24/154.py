# Solved by Влад


from re import *

f = open("test.txt")
s = f.readline()
p = r"((VWXYZ|WXYZ|XYZ|YZ|Z){1}(VWXYZ)+(VWXYZ|VWXY|VWX|VW|V))"
p2 = rf"(?=({p}))"
res = []
for x in finditer(p2, s):
    res.append(len(x.group(1)))
print(max(res))
