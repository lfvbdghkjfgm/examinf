# Solved by lfvbdghkjfgm
# https://lfvb.ru

from string import printable

for x in printable[:23]:
    a = int(f"761{x}035", 23)
    b = int(f"338{x}932", 23)
    if (a + b) % 22 == 0:
        print((a + b) // 22)
        break
