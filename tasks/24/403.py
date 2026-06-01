# Solved by lfvbdghkjfgm
# https://lfvb.ru

with open("403_1.txt") as f:
    text = f.read()


active_kombo = ""
last_combo = ""
active_string = ""
max_len = 0

for start in range(len(text)):
    for char in range(start, len(text)):
        if text[char] not in "XYZ":
            break
        elif not active_kombo:
            try:
                if text[char] == last_combo or text[char] != text[char + 1]:
                    break
            except:
                pass
            active_kombo += text[char]
            active_string += text[char]
        else:
            if text[char] != active_kombo:
                break
            active_string += text[char]
            active_kombo = ""
            last_combo = text[char]
    last_combo = ""
    active_kombo = ""
    max_len = max(max_len, len(active_string))
    active_string = ""

print(max_len)
