# Solved by Аня


l = [[int(d) for d in x.split()] for x in open("bite.9.9.txt")]
ct = 0
for x in l:
    x = sorted(x)
    if (x[0] + x[-1]) > (x[1] + x[2]):
        if (
            x[0] * x[1] != x[2] * x[3]
            and x[0] * x[2] != x[1] * x[3]
            and x[0] * x[3] != x[2] * x[1]
        ):
            ct += 1
print(ct)

# Solved by Анастасия


l = [[int(d) for d in x.split()] for x in open("9.txt")]
ct = 0
for x in l:
    if (
        (max(x) + min(x)) > (sum(x) - min(x) - max(x))
        and (x[0] * x[1] != x[2] * x[3])
        and (x[0] * x[2] != x[1] * x[3])
        and (x[0] * x[3] != x[1] * x[2])
    ):
        ct += 1
        print(x)
print(ct)
