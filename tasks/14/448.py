# Solved by Иван П.


for x in range(67):
    a = 3 * 81**3 + x * 81**2 + 2 * 81 + 1 + 1 * 67**3 + 7 * 67**2 + x * 67 + 4
    if a % 35 == 0:
        print(a // 35)
