# Solved by София


from string import *

for x in printable[:27]:
    a = int(f"3616465{x}", 27)
    b = int(f"99{x}95{x}69", 27)
    if (a + b) % 26 == 0:
        print((a + b) // 26)
