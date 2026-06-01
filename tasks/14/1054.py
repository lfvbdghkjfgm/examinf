# Solved by Арина

for x in "0123456789ABCDEFGHIJKLM":
    s1 = int(f"11353{x}12", 23)
    s2 = int(f"135{x}21", 23)
    if (s1 + s2) % 22 == 0:
        print((s1 + s2) // 22)

# Solved by София

from string import *

for x in printable[:23]:
    a = int(f"11353{x}12", 23)
    b = int(f"135{x}21", 23)
    if (a + b) % 22 == 0:
        print(x, (a + b) // 22)

# Solved by Анастасия

for x in range(0, 23):
    c1 = (
        1 * 23**7
        + 1 * 23**6
        + 3 * 23**5
        + 5 * 23**4
        + 3 * 23**3
        + x * 23**2
        + 1 * 23
        + 2
    )
    c2 = 1 * 23**5 + 3 * 23**4 + 5 * 23**3 + x * 23**2 + 2 * 23 + 1
    if (c1 + c2) % 22 == 0:
        print(x, (c1 + c2) // 22)
