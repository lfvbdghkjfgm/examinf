# Solved by София

from string import *

for x in printable[:22]:
    a = int(f"A23{x}AC0", 22)
    b = int(f"GB{x}21670", 22)
    if (a + b) % 21 == 0:
        print(x, (a + b) / 22)
