# Solved by Владимир Д.


# Для какого наименьшего натурального числа А

# (5y < A) ∧ (3x < A) ∨ (139891 < 7y + 3x)
# истинно при любых целых положительных x и у?

# 7y = 139891 - 3x -> y = (139891 - 3x) / 7


def check(A):
    for x in range(1, 50_000):
        y = (139891 - 3 * x) // 7
        if y >= 1:
            f = ((5 * y < A) and (3 * x < A)) or (139891 < 7 * y + 3 * x)
            if not f:
                return 0
    return 1


for A in range(139_000, 10**8):
    if check(A):
        print(A)
        break
