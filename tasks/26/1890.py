# Solved by lfvbdghkjfgm
# https://lfvb.ru

data = [[int(i) for i in x.split()] for x in open(r"C:\Users\111\Downloads\26.txt")]

cameras_ct = data[0][0]
data = data[1:]

cameras = {}

for number, cam in enumerate(data[:cameras_ct], 1):
    cameras[number] = {"type": cam[0], "volume": cam[1], "queue": [[-1, -1]]}

data = data[cameras_ct:]
data.sort(key=lambda d: (d[0], d[1]))


def find_camera(type, start_time, volume):
    d = [10**6, 10**6]
    for number, cam in cameras.items():
        if (
            cam["type"] == type
            and cam["queue"][-1][1] < start_time
            and cam["volume"] >= volume
        ):
            if cam["volume"] < d[1] or cam["volume"] == d[1] and number < d[0]:
                d = [number, cam["volume"]]

    if d[0] != 10**6:
        return d[0]
    else:
        return 0


people_ct = 0
last_number = [[], 0]

for start, end, volume, type in data:
    cm = find_camera(type, start, volume)
    if not cm:
        continue
    if start > last_number[1]:
        last_number = [[cm], start]
    elif start == last_number[1]:
        last_number[0].append(cm)
    people_ct += 1
    cameras[cm]["queue"].append([start, end])

print(people_ct, min(last_number[0]))
