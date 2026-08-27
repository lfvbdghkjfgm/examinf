# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

data = [[int(i) for i in x.split()] for x in open("1.txt")]
data.sort()

dp = [[(-1, -1) for _ in range(3)] for _ in range(len(data))]

for i in range(len(data)):
    dp[i][1] = (1, 0)

for i in range(len(data)):
    a, b = data[i]

    for r in range(3):
        cnt, last_clean = dp[i][r]
        if cnt == -1:
            continue

        for j in range(i + 1, len(data)):
            a1, b1 = data[j]

            if r != 0:
                if a1 >= b:
                    ct = cnt + 1
                    nr = ct % 3
                    new_clean = last_clean
                    state = (ct, last_clean)
                    if (
                        ct > dp[j][nr][0]
                        or ct == dp[j][nr][0]
                        and last_clean > dp[j][nr][1]
                    ):
                        dp[j][nr] = state

            else:
                if a1 >= b + 10:
                    if a1 >= b:
                        ct = cnt + 1
                        nr = ct % 3
                        new_clean = a1 - b
                        state = (ct, new_clean)
                        if (
                            ct > dp[j][nr][0]
                            or ct == dp[j][nr][0]
                            and last_clean > dp[j][nr][1]
                        ):
                            dp[j][nr] = state

res = [0, 0]
for i in range(len(data)):
    for r in range(3):
        if dp[i][r][0] > res[0] or dp[i][r][0] == res[0] and dp[i][r][1] > res[1]:
            res = dp[i][r]
print(*res)
