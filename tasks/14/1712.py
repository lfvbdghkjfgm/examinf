# Solved by lfvbdghkjfgm
# https://lfvb.ru


def to_27(num):
    res = []
    while num:
        res.append(num % 27)
        num //= 27

    return res[::-1]


t = to_27(2 * 2187**2020 + 729**2021 - 2 * 243**2022 + 81**2023 - 2 * 27**2024 - 6561)
print(len([i for i in t if i > 9]))

# Solved by Анастасия


def v27(n):
    s = []
    while n > 0:
        s.append(n % 27)
        n //= 27
    return s[::-1]


d = 2 * 2187**2020 + 729**2021 - 2 * 243**2022 + 81**2023 - 2 * 27**2024 - 6561
d = v27(d)
ct = 0
for p in d:
    if p > 9:
        ct += 1
print(ct)

# Solved by Владимир Д.


def to27(n):
    r = []
    while n > 0:
        r.append(n % 27)
        n //= 27
    return r[::-1]


s = to27(2 * 2187**2020 + 729**2021 - 2 * 243**2022 + 81**2023 - 2 * 27**2024 - 6561)
print(len(list(d for d in s if d > 9)))
