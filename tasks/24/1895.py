# Solved by lfvbdghkjfgm
# https://lfvb.ru

text = open(r"C:\Users\111\Downloads\24.txt").readline()

text = text.split("BC")

mx = 0

for i in range(len(text) - 180):
    s = "C" + "BC".join(text[i : i + 181]) + "B"
    mx = max(mx, len(s))

print(mx)
