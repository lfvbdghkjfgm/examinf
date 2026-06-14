# Solved by lfvbdghkjfgm
# https://lfvb.ru


def to_36(num):
    res = []
    while num:
        res.append(num % 36)
        num //= 36
    return res[::-1]


t = to_36(5 * 1296**2021 - 4 * 216**2022 + 3 * 36**2023 - 2 * 6**2024 - 2025)

print(len([i for i in t if i % 2 == 0]))

# Solved by София


def f36(n):
    s = []
    while n > 0:
        s.append(n % 36)
        n //= 36
    return s


a = 5 * 1296**2021 - 4 * 216**2022 + 3 * 36**2023 - 2 * 6**2024 - 2025
b = f36(a)
print(b)
ct = 0
for x in b:
    print(x)
    if x % 2 == 0:
        ct += 1
print(ct)
