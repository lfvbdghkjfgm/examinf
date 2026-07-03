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

# Solved by Владимир Д.


with open("327_1.txt") as f:
    s = f.read()

for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    s = s.replace(char, " ")
numbers = [int(x) for x in s.split() if int(x) % 2 == 0]
print(max(numbers))
