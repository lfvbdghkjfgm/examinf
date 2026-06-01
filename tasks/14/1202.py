# Solved by Константин Х.

for x in range(0, 41):
    c1 = 19 * 42**4 + 5 * 42**3 + 6 * 42**2 + 9 * 42 + x
    c2 = 1 * 42**3 + x * 42**2 + 18 * 42 + 10
    if (c1 + c2) % 155 == 0:
        print((c1 + c2) / 155, x)

# Solved by Анастасия

# import string
# print(string.ascii_uppercase)
for x in range(0, 42):
    c1 = 19 * 42**4 + 5 * 42**3 + 6 * 42**2 + 9 * 42 + x
    c2 = 42**3 + x * 42**2 + 18 * 42 + 10
    if (c1 + c2) % 155 == 0:
        print(x, (c1 + c2) // 155)

# Solved by Тимур А.

for x in range(1, 42):
    c1 = 19 * 42**4 + 5 * 42**3 + 6 * 42**2 + 9 * 42**1 + x * 42**0
    c2 = 1 * 42**3 + x * 42**2 + 18 * 42**1 + 10 * 42**0
    if (c1 + c2) % 155 == 0:
        print((c1 + c2) // 155)
