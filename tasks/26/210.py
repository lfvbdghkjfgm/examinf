# Solved by lfvbdghkjfgm
# https://lfvb.ru

from tqdm import tqdm

text = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\210_1.txt")
]
# text =  [[int(i) for i in x.split()] for x in open(r"1.txt")]

max_peoples = 0
pick_count = 0
is_pick = False
people = []

for minute in tqdm(range(1441)):
    tmp = []
    for a, b in text[1:]:
        if a == minute:
            people.append([a, b])
            tmp.append([a, b])
    for i in tmp:
        text.remove(i)

    if len(people) > max_peoples:
        pick_count = 1
        is_pick = True
        max_peoples = len(people)
    elif len(people) == max_peoples and is_pick == False:
        pick_count += 1
        is_pick = True
    elif len(people) < max_peoples:
        is_pick = False

    tmp = []

    for a, b in people:
        if b == minute:
            tmp.append([a, b])
    for i in tmp:
        people.remove(i)

print(pick_count, max_peoples)
