# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from collections import Counter

text = open(r"C:\Users\aatop\Downloads\1606_1.txt").readlines()
res = [0, ""]
for st in text:
    st = st.replace("\n", "")
    if st.count("Q") >= res[0]:
        d = dict(Counter(st))
        mn = [10**10, ""]
        for k in sorted(d.keys()):
            if d[k] < mn[0]:
                mn = [d[k], k]
        res = [st.count("Q"), mn[1]]
print(res[1], "".join(text).count(res[1]), sep="")
