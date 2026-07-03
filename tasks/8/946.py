# Solved by Владислав Ф.


from itertools import product

count = 0
for word in product("ЗИМА", repeat=5):
    s = "".join(word)
    if s[0] in "ЗМ" and s[-1] in "ИА":
        count += 1

print(count)

# Solved by Арина


import itertools

ct = 0
for x in itertools.product(sorted("ЗИМА"), repeat=5):
    x = "".join(x)
    if x[0] in "ЗМ":
        if x[4] in "ИА":
            ct += 1
print(ct)

# Solved by Константин Х.


import itertools

ct = 0
for x in itertools.product(sorted("ЗИМА"), repeat=5):
    x = "".join(x)
    x = x.replace("М", "З")
    x = x.replace("А", "И")
    if x[0] == "З" and x[-1] == "И":
        ct += 1
print(ct)
