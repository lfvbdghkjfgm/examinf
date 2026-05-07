data = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\830_1.txt")
]
data = data[1:]


def sum_pol(l: list):
    return sum([i for i in l if i > 0])


def count_answers(l: list):
    return len([i for i in l if i != 0])


students = []
for d in data:
    id = d[0]
    sm = sum(d[1:])
    sm_pl = sum_pol(d[1:])
    ct_ans = count_answers(d[1:])
    students.append([id, sm, sm_pl, ct_ans])

students.sort(key=lambda d: (-d[1], -d[2], -d[3], d[0]))

ct = len(students) // 3
pr = students[:ct]

for i in students:
    if i[1:] == pr[-1][1:] and i != pr[-1]:
        pr.append(i)

last_id = 0
for i in students:
    if i not in pr:
        last_id = i[0]
        break

res = 0
for i in students:
    if i[1:] == students[1499][1:]:
        res += 1
print(last_id, res)
