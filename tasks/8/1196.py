# Solved by Иса


import itertools

k = 0
for x in itertools.product(sorted(set("ПАВСИКАКИЙ")), repeat=6):
    x = "".join(x)
    if "АА" in x or "ИИ" in x or "ИА" in x or "АИ" in x:
        k += 1
    if x == "КАКААА":
        print(k)
