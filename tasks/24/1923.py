# Solved by Аня


s = open("24.txt").readline()
s = s.split("X")
mx = []
for x in range(len(s) - 60):
    ln = 0
    ct2026 = 0
    for y in range(61):
        ln += len(s[x + y])
        ct2026 += s[x + y].count("2026")
    if ct2026 >= 75:
        mx.append(ln + 60)
print(max(mx))
