# Solved by Владимир Д.


with open("174_1.txt") as f:
    s = f.read()

max_len = 0
current = ""
for char in s:
    if char in current:
        current = current[current.index(char) + 1 :]
    current += char
    max_len = max(max_len, len(current))
print(max_len)
