# Solved by Аня


import itertools

k = 0
for x in itertools.product(sorted(set("ЧЕРЕМША")), repeat=7):
    x = "".join(x)
    k += 1
    # print(k, x)
    if k % 2 != 0:
        if x[0] != "А" and x[0] != "Е" and x.count("Р") >= 2:
            print(k, x)

# Solved by Анастасия


import itertools

k = 0
for x in itertools.product("АЕМРЧШ", repeat=7):
    x = "".join(x)
    k += 1
    if k % 2 != 0 and x[0] != "А" and x[0] != "Е" and x.count("Р") >= 2:
        print(k, x)
