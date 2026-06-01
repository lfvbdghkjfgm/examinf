# Solved by Арина


s = 53**123 + 65**2222 - 172**12
z = ""
k = 0
while s > 0:
    z = z + str(s % 7)
    s = s // 7
z = z[::-1]
z = "".join(z)
print(z)
x = z.count("61") + z.count("62") + z.count("63") + z.count("64") + z.count("65")

print(x)
