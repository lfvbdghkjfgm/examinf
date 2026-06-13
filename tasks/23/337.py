# Solved by lfvbdghkjfgm
# https://lfvb.ru


def f(n, c, last_command="+", check=False):
    if n == c and check:
        return 1
    if n == c:
        return 0
    if n % 10 == 3 or n > c:
        return 0
    if n == 60:
        check = True
    if last_command == "-":
        return f(n + 7, c, "+", check) + f(n * 2, c, "*", check)
    return (
        f(n + 7, c, "+", check)
        + f(n * 2, c, "*", check)
        + f(n - 1, c, "-", check)
        + f(n - 5, c, "-", check)
    )


print(f(9, 84))
