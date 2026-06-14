# Solved by lfvbdghkjfgm
# https://lfvb.ru

text = open(r"C:\Users\aatop\Downloads\1618_1.txt").readlines()

res = 0
for st in text:
    if st.count("AOA") > st.count("OAO"):
        res += 1

print(res)
