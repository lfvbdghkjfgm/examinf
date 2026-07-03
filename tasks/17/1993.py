# Solved by Анастасия


l = [int(x) for x in open("17.txt")]
mn = []
ok8 = [y for y in l if str(y)[-1] == "8" and len(str(abs(y))) == 2]
for x in range(len(l) - 2):
    if (
        str(l[x])[-2:] == "52"
        or str(l[x + 1])[-2:] == "52"
        or str(l[x + 2])[-2:] == "52"
    ):
        if (
            max(abs(l[x] - l[x + 1]), abs(l[x] - l[x + 2]), abs(l[x + 1] - l[x + 2]))
        ) <= (sum(ok8) / len(ok8)):
            mn.append(l[x] + l[x + 1] + l[x + 2])
print(len(mn), min(mn))
