# Solved by lfvbdghkjfgm
# https://lfvb.ru


def to_27(num):
    res = []
    while num:
        res.append(num % 27)
        num //= 27
    return res[::-1]


t = to_27(2 * 2187**567 + 729**566 - 2 * 243**565 + 81**564 - 2 * 27**563 - 6561)

print(len([i for i in t if i % 2 == 0 and i > 9]))
