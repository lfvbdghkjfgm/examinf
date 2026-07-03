# Solved by Иса


import itertools

k = 0
for x in itertools.product("0123456789abcde", repeat=8):
    x = "".join(x)
    if (
        x[0] != "0"
        and x.count("0") == 2
        and (x.count("a") + x.count("b") + x.count("c") + x.count("d") + x.count("e"))
        <= 4
    ):
        k += 1
print(k)
