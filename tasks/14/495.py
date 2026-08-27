# Solved by Виктор Г.


for x in range(1, 2030):

    def f(h):
        l = ""
        while h > 0:
            l += str(h % 6)
            h = h // 6
        return l[::-1]

    t = (6**260) + (6**160) + (6**60) - x
    g = f(t)
    if str(g).count("0") == 202:
        print(x)
