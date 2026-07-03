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

# Solved by Анастасия


def v36(n):
    s = []
    while n > 0:
        s.append(n % 36)
        n //= 36
    return s[::-1]


d = 5 * 1296**2021 - 4 * 216**2022 + 3 * 36**2023 - 2 * 6**2024 - 2025
d = v36(d)
print(
    d.count(0)
    + d.count(2)
    + d.count(4)
    + d.count(6)
    + d.count(8)
    + d.count(10)
    + d.count(12)
    + d.count(14)
    + d.count(16)
    + d.count(18)
    + d.count(20)
    + d.count(22)
    + d.count(24)
    + d.count(26)
    + d.count(28)
    + d.count(30)
    + d.count(32)
    + d.count(34)
)
