# Solved by Владимир Д.


with open("other/examinf/24/1090.txt") as f:
    s = f.readline()

    l = 0
    dots = 0
    mx = 0

    for r in range(len(s)):
        if s[r] == ".":
            dots += 1

        while dots > 5:
            if s[l] == ".":
                dots -= 1
            l += 1

        mx = max(mx, r - l + 1)

    print(mx)
