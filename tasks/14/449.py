# Solved by София

for x in range(0, 95):
    for y in range(95):
        a = 5 + x * 95 + y * 95**2 + x * 95**3 + 1 * 95**4
        b = 7 + 1 * 95 + x * 95**2 + y * 95**3 + 6 * 95**4
        if (a + b) % 4221 == 0:
            print(hex((a + b) // 4221)[2:], x)
