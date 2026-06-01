# Solved by Иван С.

s = open("196_1.txt").readline()
k = 1
mx = 1
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        k += 1
        mx = max(mx, k)
    else:
        k = 1
print(mx)

# Solved by Влад

a = []
f = open("1.txt")
for n in f:
    a.append(n)
s = "".join(a)
m = 0
k = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        k += 1
    else:
        k += 1
        m = max(m, k)
        k = 0
print(m)
