# Solved by lfvbdghkfjgm
# https://lfvb.ru


def to_27(num):
    res = []
    while num:
        res.append(num % 27)
        num //= 27

    return res[::-1]


t = to_27(2 * 2187**2020 + 729**2021 - 2 * 243**2022 + 81**2023 - 2 * 27**2024 - 6561)
print(len([i for i in t if i > 9]))
