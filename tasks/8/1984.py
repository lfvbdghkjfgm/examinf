# Solved by Аня


import itertools

k = 0
for x in itertools.product(sorted("ОНЕТРУЧКАМИ"), repeat=10):
    x = "".join(x)
    k += 1
    if k % 2 != 0:
        if x[0] != "О":
            if x.count("О") >= 2:
                x = x.replace("Е", "#")
                x = x.replace("У", "#")
                x = x.replace("А", "#")
                x = x.replace("И", "#")
                if x[0] != "#":
                    print(k, x)
