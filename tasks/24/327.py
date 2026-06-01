# Solved by Влад

f = open("test.txt")
s = f.readline()
for c in "QWERTYUIOPASDFGHJKLZXCVBNM":
    s = s.replace(c, "*")
a = s.split("*")
res = []
for i in range(len(a)):
    if a[i] != "":
        res.append(int(a[i]))
print(sorted(res))
