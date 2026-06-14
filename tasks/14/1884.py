# Solved by lfvbdghkjfgm
# https://lfvb.ru

from string import printable

for x in printable[:22]:
    a = int(f"12313{x}57", 22)
    b = int(f"1{x}34561", 22)
    if (a + b) % 21 == 0:
        print((a + b) // 21)
