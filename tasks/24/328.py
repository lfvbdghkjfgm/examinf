# Solved by Анастасия


s = open("328.txt").readline()
s = s.split("CD")
mx_ln = []
for x in range(len(s) - 50):
    k = 0
    for y in range(51):
        k += len(s[x + y])
    mx_ln.append(k)
print(max(mx_ln) + 2 * 50 + 2)

# Solved by Иван П.


s = open("324.txt").readline()
s = s.replace("CD", "C D").split()
maxl = 0
for i in range(len(s) - 50):
    l = 0
    for j in range(51):
        l += len(s[i + j])
    if l > maxl:
        maxl = l
print(maxl)

# Solved by Глеб Г.


s = open("21.txt").readline()
s = s.split("CD")
mx_ln = []
for x in range(len(s) - 50):
    ln = 0
    for y in range(0, 51):
        ln += len(s[x + y])
    mx_ln.append(ln + 102)
print(max(mx_ln))

# Solved by Вадим С.


l = open("328_1.txt").readline().split("CD")
cl = []
for x in range(len(l) - 50):
    c = 0
    for y in range(0, 51):
        c += len(l[x + y])
    cl.append(c + 50 * 2)
print(max(cl))
# Все это время я забыл добавлять по бокам по 1 символу...
