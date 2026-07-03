# Solved by Аня


import itertools

k = 0
sm = []
for x in itertools.product(sorted("АВЕКЛМОРС"), repeat=7):
    k += 1
    x = "".join(x)
    if (
        x[0] != "А"
        and x[0] != "В"
        and x[0] != "Е"
        and x[1] != "А"
        and x[1] != "В"
        and x[1] != "Е"
        and x[2] != "А"
        and x[2] != "В"
        and x[2] != "Е"
    ):
        if x.count("Р") == 3:
            x = x.replace("А", "#")
            x = x.replace("В", "#")
            x = x.replace("Е", "#")
            x = x.replace("К", "#")
            x = x.replace("Л", "#")
            x = x.replace("М", "#")
            x = x.replace("О", "#")
            if "СР#Р##Р" in x or "СР##Р#Р" in x or "СР#Р#Р#" in x:
                sm.append(k)
print(sum(sm))

# Solved by Анастасия


import itertools

k = 0
ct = 0
for x in itertools.product("АВЕКЛМОРС", repeat=7):
    x = "".join(x)
    k += 1
    if (
        x[0] not in "АВЕ"
        and x[1] not in "АВЕ"
        and x[2] not in "АВЕ"
        and x.count("Р") == 3
        and "РР" not in x
        and x.count("С") == 1
    ):
        if x.index("С") < x.index("Р"):
            ct += k
print(ct)
