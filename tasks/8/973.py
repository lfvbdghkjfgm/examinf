# Solved by Константин Х.


import itertools

ct = 0
for x in itertools.product(sorted("НИКОЛАЙ"), repeat=4):
    x = "".join(x)
    x = x.replace("О", "И")
    x = x.replace("А", "И")
    if x[0] != "Й" and x.count("И") >= 1:
        ct += 1
print(ct)
