# Solved by Константин Х.


import itertools

ct = 0
d = ["1", "3", "5", "7"]
for x in itertools.product("012345678", repeat=6):
    x = "".join(x)
    if x[0] != "0":
        if x[0] not in d:
            if x[-1] != "2" and x[-1] != "3":
                if x.count("1") >= 2:
                    ct += 1
print(ct)

# Solved by Мария


import itertools

ct = 0
for x in itertools.product("012345678", repeat=6):
    x = "".join(x)
    if (
        x[0] != "0"
        and x[0] != "1"
        and x[0] != "3"
        and x[0] != "5"
        and x[0] != "7"
        and x[-1] != "2"
        and x[-1] != "3"
        and x.count("1") >= 2
    ):
        ct += 1
print(ct)
