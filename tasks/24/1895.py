# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

text = open(r"C:\Users\111\Downloads\24.txt").readline()

text = text.split("BC")

mx = 0

for i in range(len(text) - 180):
    s = "C" + "BC".join(text[i : i + 181]) + "B"
    mx = max(mx, len(s))

print(mx)

# Solved by Анастасия


s = open("1895.txt").readline()
s = s.split("BC")
mx_ln = []
for x in range(len(s) - 180):
    k = 0
    for y in range(181):
        k += len(s[x + y])
    mx_ln.append(k)
print(max(mx_ln) + 180 * 2)
